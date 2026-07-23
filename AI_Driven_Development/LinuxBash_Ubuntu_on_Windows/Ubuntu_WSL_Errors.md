# Ubuntu / WSL Complete Development Setup Guide

**`If you are using WSL (Windows Subsystem for Linux) on Windows, you may face some common issues when setting up a development environment.`**

This document covers the **complete setup of a development environment in Ubuntu (WSL)**, including **Node.js (via NVM)**, **npm**, **Python**, and **pip**. It is based on the exact steps we followed and common issues we resolved.

* * *

## 1\. Install Node.js inside WSL (Recommended)

Update packages

```bash
sudo apt update
```

Install Node.js (LTS)

```bash
sudo apt install -y nodejs npm
```

Verify installation

```bash
node -v
npm -v
```

## 2\. Installing Node.js 20 Using NVM (Best Practice)

We use **NVM (Node Version Manager)** because it allows easy switching between Node versions.

### Step 2.1: Install NVM

```bash
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# For better version
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

### Step 2.2: Reload Terminal

```bash
source ~/.bashrc
```

### Step 2.3: Verify NVM Installation

```bash
nvm --version
```

## 3\. Install & Upgrade Node.js to Version 20

### Step 3.1: Install Node.js v20

```bash
nvm install 20

# For Latest LTS version 24.18.0
nvm install 24.18.0

```

### Step 3.2: Use Node.js v20

```bash
nvm use 20

# Use it
nvm use 24.18.0
```

### Step 3.3: Set Node.js 20 as Default

```bash
nvm alias default 20

# Set as default 24.18.0
nvm install 24.18.0
```

### Step 3.4: Verify Node & npm

```bash
node -v
npm -v
```

## 4\. Installing Python, pip, and Virtual Environment

Ubuntu does not always come with Python and pip pre-installed.

### Step 4.1: Install Python & pip

```bash
sudo apt install -y python3 python3-pip python3-venv
```

### Step 4.2: Verify Python & pip

```bash
python3 --version
pip3 --version
```

### Step 4.3: Create virtual environment

```bash
python3 -m venv venv
```
### Step 4.4: Activate

```bash
source venv/bin/activate
```

## 5\. Enable `python` and `pip` Commands (Optional but Recommended)

By default, Ubuntu uses `python3` and `pip3`. To enable `python` and `pip`:

```bash
sudo apt install -y python-is-python3
```

### Verify

```bash
python --version
pip --version
```

## 6\. Fixing Common Errors

### ❌ `command not found: node`

✔ Node.js was not installed or NVM was not loaded

Solution:

```bash
source ~/.bashrc 
nvm use 20
```

---

### ❌ `pip: command not found`

✔ pip was not installed or only `pip3` exists

Solution:

```bash
sudo apt install python3-pip
sudo apt install python-is-python3
```

### ✅ Correct way to access Windows drives in WSL

In WSL, **Windows drives are mounted under `/mnt`**.

#### Drive mapping:

| Windows | WSL |
| --- | --- |
| `C:\\` | `/mnt/c/` |
| `D:\\` | `/mnt/d/` |
| `G:\\` | `/mnt/g/` |

### ✅ Correct command for your path

Your Windows path:

```bash
G:\osamabinadnan_files\giaic\quarter_04_plus\dummy
```
Correct WSL command:

```bash
cd /mnt/g/osamabinadnan_files/giaic/quarter_04_plus/dummy
```
✅ This **will work** if the folder exists.


## 7\. Copy & Paste in Ubuntu Terminal

### Paste

-   `Ctrl + Shift + V`
-   Right-click → Paste

### Copy

-   `Ctrl + Shift + C`

> In **Windows Terminal (WSL)**, `Ctrl + V` also works.

## 8\. Final Verification Checklist

Run these commands to confirm everything is set up correctly:

```bash
node -v
npm -v
nvm --version
python --version
pip --version
```

If all commands return versions → ✅ setup is complete.

---

## 9\. Recommended Tools

-   **Windows Terminal** (Best for WSL)
-   **VS Code + WSL Extension**
-   **NVM** for Node version control
-   **python-venv** for Python projects

---

## ✅ Setup Completed Successfully

Your Ubuntu (WSL) environment is now fully ready for:

-   Frontend (Next.js, React)
-   Backend (FastAPI, Node.js)
-   Python development
-   npm & pip package management

---

Happy Coding 🚀
