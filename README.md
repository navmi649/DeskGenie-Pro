🏢 DeskGenie Pro
Enterprise Desktop Management Dashboard
📖 Overview

DeskGenie Pro is a structured desktop management system designed to automate file organization, enforce workspace hygiene, and provide enterprise-level traceability through timestamped audit logging and undo recovery mechanisms.

The application enables safe and transparent desktop cleanup using intelligent classification, duplicate detection, and structured file movement.

🎯 Problem Statement

Desktop environments frequently become cluttered due to:

Unorganized documents

Duplicate files

Temporary artifacts

Lack of traceability in file movements

Manual and error-prone cleanup

DeskGenie Pro provides a controlled, automated, and reversible solution for maintaining a clean and structured workspace.

🚀 Core Features
📂 Intelligent File Organization

Keyword-based classification

Extension-based categorization

Structured folder creation (Work, Study, Media, Personal, Archive)

Confirmation before execution

🔍 Duplicate Detection

MD5 hash-based identification

Safe archival of duplicates

No filename-only matching

🧹 Empty Folder Cleanup

Detects unused directories

Confirmation before deletion

📊 Desktop Analytics

Total file count

Total folder count

Storage usage (MB)

File type distribution

🔁 Undo System

Restores all moved files

Full recovery capability

Safe rollback of operations

📝 Enterprise Logging System

Timestamped logs

Log levels (INFO / SUCCESS / WARNING / ERROR)

Exportable log file

Clear console functionality

Full file path visibility

📁 Quick Navigation

Open last moved destination folder instantly

🖥 User Interface

The application follows a corporate dashboard layout with:

Operations panel

Structured action buttons

Activity console

Status bar

Enterprise-style visual hierarchy

The interface prioritizes clarity, traceability, and safe execution.

🧠 Technical Architecture

Language: Python
GUI Framework: Tkinter
File Operations: os, shutil
Duplicate Detection: hashlib (MD5 hashing)
Analytics: collections.Counter
Logging: datetime-based timestamping

Core subsystems include:

Classification Engine

File Movement Engine

Logging & Audit Module

Undo Stack Mechanism

Dashboard UI Layer

🛡 Safety & Reliability

Confirmation dialogs before execution

No automatic overwriting

Undo recovery support

Archive-based duplicate management

Full audit logging system

📦 Installation & Usage

Clone the repository:

git clone https://github.com/navmi649/DeskGenie-Pro.git
cd DeskGenie-Pro

Run the application:

python main.py
📌 Future Enhancements

Role-based modes (Developer / Enterprise)

Workspace health scoring

Scheduled automation

Policy-based organization rules

Cloud storage integration

Installer packaging (.exe setup)

📈 Project Status

Version: 1.0.0
Type: Desktop Application
Status: Stable

👩‍💻 Author

Navami Jith
Computer Science Engineering Student

