import os
import shutil
import hashlib
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk, filedialog
from collections import Counter
from datetime import datetime

# =====================================================
# CONFIGURATION
# =====================================================

DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

MAIN_FOLDERS = {
    "Work": "01_Work",
    "Study": "02_Study",
    "Personal": "03_Personal",
    "Media": "04_Media",
    "Archive": "05_Archive"
}

KEYWORDS_WORK = ["resume", "cv", "internship", "hackathon", "project"]
KEYWORDS_STUDY = ["notes", "assignment", "lab", "syllabus"]
MEDIA_EXTENSIONS = [".jpg", ".jpeg", ".png", ".mp4", ".mov", ".mp3"]

UNDO_STACK = []
LAST_DESTINATION = None
LOG_HISTORY = []

# =====================================================
# LOGGING SYSTEM
# =====================================================

def log_message(message, level="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    formatted = f"[{timestamp}] [{level}] {message}"
    LOG_HISTORY.append(formatted)
    output_box.insert(tk.END, formatted + "\n")
    output_box.see(tk.END)

def clear_console():
    output_box.delete(1.0, tk.END)

def export_logs():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            for line in LOG_HISTORY:
                f.write(line + "\n")
        log_message("Log exported successfully.", "SUCCESS")

def open_last_folder():
    if LAST_DESTINATION and os.path.exists(LAST_DESTINATION):
        os.startfile(LAST_DESTINATION)
    else:
        messagebox.showinfo("Info", "No destination folder available.")

def update_status(text):
    status_var.set(f"Status: {text}")

# =====================================================
# FILE CLASSIFICATION
# =====================================================

def classify_file(filename):
    name = filename.lower()
    _, ext = os.path.splitext(name)

    if any(word in name for word in KEYWORDS_WORK):
        return MAIN_FOLDERS["Work"]

    if any(word in name for word in KEYWORDS_STUDY):
        return MAIN_FOLDERS["Study"]

    if ext in MEDIA_EXTENSIONS:
        return MAIN_FOLDERS["Media"]

    return MAIN_FOLDERS["Personal"]

def safe_move(source, destination_folder):
    global LAST_DESTINATION

    try:
        os.makedirs(destination_folder, exist_ok=True)
        filename = os.path.basename(source)
        destination = os.path.join(destination_folder, filename)

        if not os.path.exists(destination):
            shutil.move(source, destination)
            UNDO_STACK.append((destination, source))
            LAST_DESTINATION = destination_folder

            log_message(f"Moved: {filename}", "SUCCESS")
            log_message(f"From: {source}", "INFO")
            log_message(f"To:   {destination}", "INFO")

            return True
        else:
            log_message(f"Skipped (already exists): {filename}", "WARNING")
            return False

    except Exception as e:
        log_message(f"Error moving file: {e}", "ERROR")
        return False

# =====================================================
# FEATURES
# =====================================================

def preview_and_organize():
    update_status("Scanning Desktop...")
    log_message("Scanning Desktop...", "INFO")

    preview_list = []

    for file in os.listdir(DESKTOP_PATH):
        if file.endswith(".lnk"):
            continue

        path = os.path.join(DESKTOP_PATH, file)
        if not os.path.isfile(path):
            continue

        target = classify_file(file)
        preview_list.append((file, target))

    if not preview_list:
        log_message("No files to organize.", "INFO")
        return

    confirm = messagebox.askyesno(
        "Confirm Organization",
        f"{len(preview_list)} files will be moved.\nProceed?"
    )

    if confirm:
        moved = 0
        for file, folder in preview_list:
            src = os.path.join(DESKTOP_PATH, file)
            dest = os.path.join(DESKTOP_PATH, folder)
            if safe_move(src, dest):
                moved += 1

        log_message(f"Organization complete. {moved} files moved.", "SUCCESS")
        update_status("Organization Complete")
    else:
        log_message("Operation cancelled.", "WARNING")
        update_status("Cancelled")

def detect_duplicates():
    log_message("Scanning for duplicates...", "INFO")
    hashes = {}
    duplicates = 0
    archive_folder = os.path.join(DESKTOP_PATH, MAIN_FOLDERS["Archive"])
    os.makedirs(archive_folder, exist_ok=True)

    for file in os.listdir(DESKTOP_PATH):
        if file.endswith(".lnk"):
            continue

        path = os.path.join(DESKTOP_PATH, file)
        if not os.path.isfile(path):
            continue

        try:
            with open(path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
        except:
            continue

        if file_hash in hashes:
            if safe_move(path, archive_folder):
                duplicates += 1
        else:
            hashes[file_hash] = file

    log_message(f"Duplicate scan complete. {duplicates} duplicates moved.", "SUCCESS")

def delete_empty_folders():
    log_message("Scanning for empty folders...", "INFO")
    empty_folders = []

    for item in os.listdir(DESKTOP_PATH):
        path = os.path.join(DESKTOP_PATH, item)
        if os.path.isdir(path) and not os.listdir(path):
            empty_folders.append(path)

    if not empty_folders:
        log_message("No empty folders found.", "INFO")
        return

    confirm = messagebox.askyesno(
        "Confirm Deletion",
        f"{len(empty_folders)} empty folders found.\nDelete them?"
    )

    if confirm:
        for folder in empty_folders:
            os.rmdir(folder)

        log_message(f"Deleted {len(empty_folders)} empty folders.", "SUCCESS")

def show_stats():
    log_message("Generating desktop analytics...", "INFO")

    total_files = 0
    total_folders = 0
    total_size = 0
    ext_counter = Counter()

    for item in os.listdir(DESKTOP_PATH):
        path = os.path.join(DESKTOP_PATH, item)
        if os.path.isfile(path):
            total_files += 1
            total_size += os.path.getsize(path)
            _, ext = os.path.splitext(item)
            ext_counter[ext.lower()] += 1
        elif os.path.isdir(path):
            total_folders += 1

    size_mb = round(total_size / (1024 * 1024), 2)

    log_message(f"Files: {total_files}", "INFO")
    log_message(f"Folders: {total_folders}", "INFO")
    log_message(f"Total Size: {size_mb} MB", "INFO")

    log_message("File Type Distribution:", "INFO")
    for ext, count in ext_counter.items():
        log_message(f"{ext if ext else '[No Extension]'} : {count}", "INFO")

    log_message("Analytics complete.", "SUCCESS")

def undo_last_operation():
    if not UNDO_STACK:
        messagebox.showinfo("Undo", "Nothing to undo.")
        return

    restored = 0
    while UNDO_STACK:
        dest, original = UNDO_STACK.pop()
        if os.path.exists(dest):
            shutil.move(dest, original)
            restored += 1

    log_message(f"Undo complete. {restored} files restored.", "SUCCESS")

# =====================================================
# ENTERPRISE DASHBOARD UI
# =====================================================

root = tk.Tk()
root.title("DeskGenie Pro - Enterprise Dashboard")
root.geometry("1250x850")
root.configure(bg="#f4f6f9")

# TOP BAR
top_bar = tk.Frame(root, bg="#1f2937", height=60)
top_bar.pack(fill="x")

tk.Label(top_bar, text="DeskGenie Pro",
         font=("Segoe UI", 18, "bold"),
         bg="#1f2937", fg="white").pack(side="left", padx=20)

# MAIN FRAME
main_frame = tk.Frame(root, bg="#f4f6f9")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# LEFT PANEL
operations_frame = tk.LabelFrame(
    main_frame,
    text="Operations Panel",
    font=("Segoe UI", 12, "bold"),
    bg="white",
    padx=20, pady=20
)
operations_frame.pack(side="left", fill="y", padx=10)

button_style = {
    "font": ("Segoe UI", 11),
    "width": 25,
    "height": 2,
    "bg": "#2563eb",
    "fg": "white",
    "bd": 0
}

def add_button(text, command):
    tk.Button(
        operations_frame,
        text=text,
        command=command,
        **button_style
    ).pack(pady=8)

add_button("Preview & Organize", preview_and_organize)
add_button("Detect Duplicates", detect_duplicates)
add_button("Delete Empty Folders", delete_empty_folders)
add_button("Desktop Analytics", show_stats)
add_button("Undo Last Operation", undo_last_operation)
add_button("Open Last Moved Folder", open_last_folder)
add_button("Export Logs", export_logs)
add_button("Clear Console", clear_console)

# RIGHT PANEL
console_card = tk.LabelFrame(
    main_frame,
    text="Activity Console",
    font=("Segoe UI", 12, "bold"),
    bg="white",
    padx=10, pady=10
)
console_card.pack(side="right", fill="both", expand=True)

output_box = scrolledtext.ScrolledText(
    console_card,
    font=("Consolas", 10),
    bg="#111827",
    fg="#10b981",
    insertbackground="white"
)
output_box.pack(fill="both", expand=True)

status_var = tk.StringVar()
status_var.set("Status: System Ready")

status_bar = tk.Label(
    root,
    textvariable=status_var,
    bd=1,
    relief="sunken",
    anchor="w",
    bg="#e5e7eb",
    font=("Segoe UI", 10)
)
status_bar.pack(side="bottom", fill="x")

root.mainloop()