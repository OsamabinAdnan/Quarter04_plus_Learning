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