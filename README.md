DeskGenie Pro is a structured desktop management system designed to automate file organization, enforce workspace hygiene, and provide enterprise-level traceability through timestamped audit logging and undo recovery mechanisms.

The system emphasizes:

Safe file operations

Transparent logging

Undo capability

Structured organization

Enterprise-style dashboard interface

🎯 Problem Statement

Modern desktops often become cluttered due to:

Unorganized files

Duplicate documents

Temporary files

Lack of visibility into file movements

Manual cleanup inefficiencies

DeskGenie Pro provides an automated yet safe solution to manage desktop environments efficiently.

🚀 Features
📂 Intelligent File Organization

Keyword-based classification

Extension-based categorization

Structured folder creation

Confirmation before execution

🔍 Duplicate Detection

MD5 hash-based duplicate identification

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

📝 Enterprise Logging System

Timestamped logs

Log levels (INFO / SUCCESS / WARNING / ERROR)

Exportable log file

Clear console option

Full file path tracking

📁 Open Last Moved Folder

Quickly navigate to latest destination

🖥 User Interface

DeskGenie Pro follows a corporate dashboard design with:

Operations panel

Activity console

Status bar

Structured layout

Enterprise color scheme

🧠 Technical Architecture

Language: Python
GUI Framework: Tkinter
Hashing: hashlib (MD5)
File Operations: os, shutil
Analytics: collections.Counter
Logging: datetime-based timestamping

Core Modules:

Classification Engine

File Movement Engine

Logging System

Undo Stack

Dashboard UI Layer

🛡 Safety & Reliability

No automatic overwriting

Confirmation dialogs

Full undo support

Archive-based duplicate handling

Audit trail system

📦 Installation & Running
1️⃣ Clone the Repository
git clone https://github.com/navmi649/DeskGenie-Pro.git
cd DeskGenie-Pro
2️⃣ Run the Application
python main.py
📹 Demo

(Add your demo video link here after recording)

Example:

https://drive.google.com/your-demo-link
📌 Future Enhancements

Role-based modes (Developer / Enterprise)

Health score system

Scheduled automation

Policy-based organization rules

Cloud integration

Installer packaging (.exe setup)

📈 Project Status

Version: 1.0.0
Status: Stable
Type: Desktop Application

👩‍💻 Author

Navami Jith
Computer Science Engineering Student
GitHub: https://github.com/navmi649
