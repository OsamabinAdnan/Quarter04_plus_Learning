
# 🚀 Claude Code + Gemini Full Setup (Windows Guide)

This guide helps you set up **Claude-Code + Gemini Models** together using  
`claude-code` + `claude-code-router`.

---

## 🔥 STEP 0 — Confirm Node.js

PowerShell open karein → run:

```bash
node --version
```

Agar **18+** version nahi hai → install karein:

👉 https://nodejs.org

---

## 🔥 STEP 1 — GET GOOGLE API KEY

1. Open: https://aistudio.google.com  
2. Click → **Get API Key**  
3. Click → **Create API Key**  
4. Key copy kar len (example):  
   ```
   AIzaSy........
   ```

---

## 🔥 STEP 2 — INSTALL REQUIRED TOOLS

PowerShell (Run as Administrator):

```bash
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router
```

---

## 🔥 STEP 3 — CREATE CONFIG FOLDERS

PowerShell (normal mode):

```bash
mkdir $HOME/.claude-code-router
mkdir $HOME/.claude
```

---

## 🔥 STEP 4 — CREATE CONFIG.JSON (WINDOWS VERSION)

Windows me `cat << EOF` work nahi karta, isliye Notepad method use hoga.

Run:

```bash
notepad $HOME/.claude-code-router/config.json
```

Notepad open hoga → isme ye **exact JSON** paste karein:

```json
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "gemini",
      "api_base_url": "https://generativelanguage.googleapis.com/v1beta/models/",
      "api_key": "$GOOGLE_API_KEY",
      "models": [
        "gemini-2.5-flash",
        "gemini-2.0-flash"
      ],
      "transformer": {
        "use": ["gemini"]
      }
    }
  ],
  "Router": {
    "default": "gemini,gemini-2.5-flash",
    "background": "gemini,gemini-2.5-flash",
    "think": "gemini,gemini-2.5-flash",
    "longContext": "gemini,gemini-2.5-flash",
    "longContextThreshold": 60000
  }
}
```

✔ Save  
✔ Close

---

## 🔥 STEP 5 — SET YOUR API KEY (WINDOWS METHOD)

PowerShell (Run as Admin):

```powershell
[System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY', 'YOUR_KEY_HERE', 'User')
```

Replace:

```
YOUR_KEY_HERE
```

With your actual Google API Key.

Example:

```powershell
[System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY', 'AIzaSyXXXXX...', 'User')
```

### ⚠️ IMPORTANT  
PowerShell **close** karen → new PowerShell open → check:

```bash
echo $env:GOOGLE_API_KEY
```

Agar value show ho jaye → **Perfect! 🔥**

---

## 🔥 STEP 6 — VERIFY EVERYTHING

Run:

```bash
claude --version
ccr version
echo $env:GOOGLE_API_KEY
```

Agar sab commands ka output aa jaye → ✔ Setup success

---

## 🔥 STEP 7 — DAILY WORKFLOW

### Terminal 1:

```bash
ccr start
```

Wait until you see:

```
✔ Service started successfully
```

### Terminal 2:

```bash
cd your-project-folder
ccr code
```

OR:

```bash
eval "$(ccr activate)"
claude
```

---

## 🔥 VERIFICATION TEST

Terminal:

```bash
ccr code
```

Then type:

```
hi
```

Agar **Claude reply** kare →  
🎉 **Congratulations! FREE CLAUDE CODE + GEMINI WORKING! 🚀💯**