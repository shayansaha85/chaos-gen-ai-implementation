# Python Installation and Library Management Guide
## Installing Python:

### Windows:

1. **Download Python:**
   - Visit [Python.org](https://www.python.org/downloads/)
   - Download the latest Python installer for Windows.
   
2. **Run Installer:**
   - Double-click the downloaded installer.
   - Follow the installation wizard instructions.
   - Check the box 'Add Python X.X to PATH' during installation.

3. **Verify Installation:**
   - Open Command Prompt (cmd) or PowerShell.
   - Type `python --version` to verify Python installation.
   
### macOS:

1. **Homebrew (Recommended):**
   - Open Terminal.
   - Install Homebrew (if not installed):
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Install Python:
     ```bash
     brew install python
     ```

2. **Verify Installation:**
   - Open Terminal.
   - Type `python3 --version` to verify Python installation.

### Linux:

1. **Package Manager (e.g., apt, yum):**
   - Open Terminal.
   - Install Python:
     - Debian/Ubuntu:
       ```bash
       sudo apt-get update
       sudo apt-get install python3
       ```
     - CentOS/Fedora:
       ```bash
       sudo yum install python3
       ```

2. **Verify Installation:**
   - Open Terminal.
   - Type `python3 --version` to verify Python installation.

## Managing Python Libraries (using pip):

### Installing Libraries:

- **Install a Library:**
  ```bash
  pip install library_name
