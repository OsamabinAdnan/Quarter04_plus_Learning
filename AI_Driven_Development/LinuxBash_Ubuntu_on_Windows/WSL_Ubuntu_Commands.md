# 🐧 WSL + Ubuntu Command Reference (with Functionality)

## 🧩 **WSL-Specific Commands (run from Windows CMD / PowerShell)**

| Command                               | Function                  |
| ------------------------------------- | ------------------------- |
| `wsl`                                 | Start default WSL distro  |
| `wsl -l`                              | List installed distros    |
| `wsl -l -v`                           | List distros with version |
| `wsl --install`                       | Install WSL               |
| `wsl --install -d Ubuntu`             | Install Ubuntu            |
| `wsl --set-version Ubuntu 2`          | Convert to WSL 2          |
| `wsl --set-default Ubuntu`            | Set default distro        |
| `wsl -d Ubuntu`                       | Start specific distro     |
| `wsl --shutdown`                      | Stop all WSL instances    |
| `wsl --terminate Ubuntu`              | Stop a specific distro    |
| `wsl --update`                        | Update WSL kernel         |
| `wsl --status`                        | Show WSL status           |
| `wsl --export Ubuntu backup.tar`      | Backup distro             |
| `wsl --import Ubuntu path backup.tar` | Restore distro            |
| `wsl --unregister Ubuntu`             | Delete distro             |

## 📁 **File & Directory Management**

| Command  | Function               |
| -------- | ---------------------- |
| `ls`     | List files             |
| `ls -la` | List with permissions  |
| `pwd`    | Show current directory |
| `cd`     | Change directory       |
| `tree`   | Directory tree         |
| `mkdir`  | Create directory       |
| `rmdir`  | Delete empty directory |
| `cp`     | Copy files             |
| `mv`     | Move/rename            |
| `rm`     | Delete files           |
| `rm -rf` | Force delete           |
| `stat`   | File info              |
| `file`   | File type              |
| `du -sh` | Directory size         |
| `df -h`  | Disk usage             |

## 🔍 **Search & Text Processing**

| Command   | Function              |
| --------- | --------------------- |
| `grep`    | Search text           |
| `grep -r` | Recursive search      |
| `find`    | Find files            |
| `locate`  | Fast search (indexed) |
| `awk`     | Pattern scanning      |
| `sed`     | Stream editor         |
| `cut`     | Extract columns       |
| `sort`    | Sort output           |
| `uniq`    | Remove duplicates     |
| `wc`      | Word/line count       |
| `xargs`   | Build arguments       |

## 📄 **File Viewing & Editing**

| Command   | Function        |
| --------- | --------------- |
| `cat`     | View file       |
| `less`    | Scroll file     |
| `more`    | Basic pager     |
| `head`    | First lines     |
| `tail`    | Last lines      |
| `tail -f` | Live logs       |
| `nano`    | Simple editor   |
| `vim`     | Advanced editor |
| `vi`      | Classic editor  |

## 🔐 **Permissions & Ownership**

| Command   | Function            |
| --------- | ------------------- |
| `chmod`   | Change permissions  |
| `chown`   | Change owner        |
| `chgrp`   | Change group        |
| `umask`   | Default permissions |
| `getfacl` | View ACL            |
| `setfacl` | Set ACL             |

## 👤 **User & Group Management**

| Command   | Function         |
| --------- | ---------------- |
| `whoami`  | Current user     |
| `id`      | User info        |
| `groups`  | Group list       |
| `adduser` | Create user      |
| `deluser` | Delete user      |
| `passwd`  | Change password  |
| `su`      | Switch user      |
| `sudo`    | Admin privileges |
| `login`   | Login session    |
| `logout`  | End session      |

## 📦 **Package Management (APT)**

| Command            | Function            |
| ------------------ | ------------------- |
| `apt update`       | Update package list |
| `apt upgrade`      | Upgrade packages    |
| `apt install pkg`  | Install package     |
| `apt remove pkg`   | Remove package      |
| `apt purge pkg`    | Remove + config     |
| `apt autoremove`   | Remove unused       |
| `apt search pkg`   | Search packages     |
| `apt show pkg`     | Package info        |
| `dpkg -i file.deb` | Install .deb        |
| `dpkg -l`          | List packages       |

## ⚙️ **Process & System Monitoring**

| Command        | Function         |
| -------------- | ---------------- |
| `top`          | Process monitor  |
| `htop`         | Enhanced monitor |
| `ps aux`       | List processes   |
| `kill PID`     | Kill process     |
| `killall name` | Kill by name     |
| `uptime`       | System time      |
| `free -h`      | Memory usage     |
| `vmstat`       | Memory stats     |
| `watch`        | Run repeatedly   |
| `time`         | Execution time   |

## 🌐 **Networking**

| Command      | Function           |
| ------------ | ------------------ |
| `ip a`       | Network interfaces |
| `ip r`       | Routing table      |
| `ping`       | Test connection    |
| `curl`       | HTTP requests      |
| `wget`       | Download files     |
| `ss -tuln`   | Open ports         |
| `netstat`    | Network stats      |
| `traceroute` | Route trace        |
| `nslookup`   | DNS lookup         |
| `hostname`   | Host info          |

## 🗜️ **Compression & Archives**

| Command    | Function    |
| ---------- | ----------- |
| `tar -xvf` | Extract tar |
| `tar -cvf` | Create tar  |
| `gzip`     | Compress    |
| `gunzip`   | Decompress  |
| `zip`      | Zip files   |
| `unzip`    | Unzip       |
| `7z`       | 7zip tool   |

## 🖥️ **Shell & Environment**

| Command       | Function        |
| ------------- | --------------- |
| `bash`        | Start bash      |
| `zsh`         | Start zsh       |
| `env`         | Env variables   |
| `export`      | Set variable    |
| `alias`       | Create alias    |
| `unalias`     | Remove alias    |
| `history`     | Command history |
| `clear`       | Clear screen    |
| `reset`       | Reset terminal  |
| `source file` | Reload config   |

## 🔄 **WSL ↔ Windows Interop**

| Command            | Function               |
| ------------------ | ---------------------- |
| `/mnt/c`           | Access C: drive        |
| `explorer.exe .`   | Open folder in Windows |
| `notepad.exe file` | Edit in Notepad        |
| `cmd.exe /c dir`   | Run Windows cmd        |
| `powershell.exe`   | Run PowerShell         |
| `code .`           | Open VS Code           |

## 🛠️ **Development & Build Tools**

| Command          | Function         |
| ---------------- | ---------------- |
| `gcc`            | C compiler       |
| `g++`            | C++ compiler     |
| `make`           | Build automation |
| `cmake`          | Build system     |
| `python3`        | Python           |
| `pip`            | Python packages  |
| `node`           | Node.js          |
| `npm`            | Node packages    |
| `git`            | Version control  |
| `docker`         | Containers       |
| `docker-compose` | Multi containers |

## 📜 **Logs & System Info**

| Command          | Function            |
| ---------------- | ------------------- |
| `uname -a`       | Kernel info         |
| `lsb_release -a` | OS info             |
| `dmesg`          | Kernel logs         |
| `journalctl`     | System logs         |
| `uptime`         | System running time |

## 🧠 **Help & Documentation**

| Command           | Function        |
| ----------------- | --------------- |
| `man command`     | Manual          |
| `command --help`  | Help            |
| `info command`    | GNU docs        |
| `whatis cmd`      | Short desc      |
| `apropos keyword` | Search commands |

## ⚡ Power Tip (WSL users)

```bash
alias winopen="explorer.exe ."
alias ll="ls -lah"
```
