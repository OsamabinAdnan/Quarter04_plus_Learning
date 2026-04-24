# OpenClaw Commands (Class 01 + Class 02 + Class 03)

| Command | Functionality |
|---|---|
| `wsl --install -d Ubuntu` | Enables WSL, installs WSL2 kernel, and installs Ubuntu on Windows. |
| `wsl -d Ubuntu` | Starts Ubuntu distribution in WSL. |
| `curl -fsSL https://openclaw.ai/install.sh | bash` | Installs OpenClaw (and Node.js if needed) inside Linux/WSL. |
| `openclaw --version` | Shows installed OpenClaw version and verifies installation. |
| `openclaw onboard --install-daemon` | Starts onboarding wizard and installs gateway daemon/service. |
| `openclaw config get agents.defaults.model` | Displays current default model configuration. |
| `openclaw config set agents.defaults.model.primary "google/gemini-2.5-flash"` | Sets the primary default model. |
| `openclaw gateway restart` | Restarts the OpenClaw gateway service. |
| `openclaw dashboard` | Opens/copies dashboard URL for agent monitoring and management. |
| `openclaw channels status --probe` | Checks channel connectivity and gateway/channel health. |
| `openclaw doctor` | Runs diagnostics on environment, config, network, and service status. |
| `openclaw tui` | Launches terminal UI to interact with the AI Employee from CLI. |
| `openclaw gateway status` | Shows current gateway health/status and runtime state. |
| `openclaw logs` | Shows OpenClaw runtime/gateway logs for debugging. |
| `openclaw doctor --repair` | Attempts automatic detection and repair of common issues. |
| `openclaw config get gateway.mode` | Checks configured gateway mode (e.g., `local`). |
| `openclaw config set gateway.mode local` | Sets gateway mode to local (common crash-loop fix). |
| `openclaw configure --section model` | Opens model/provider configuration section (useful for quota/provider switch). |
| `openclaw plugins list` | Lists available/bundled plugins. |
| `openclaw config set plugins.entries.<id>.enabled true` | Enables a specific plugin by ID. |
| `openclaw configure --section channels` | Opens channel configuration section (WhatsApp/Telegram/Discord setup). |
| `openclaw config get tools.profile` | Shows the active tool profile (e.g., coding, messaging). |
| `/reset` | Resets the current session, reloading workspace/system prompt context. |
| `/context` | Explains how context is built and used in the session. |
| `/context list` | Shows which workspace files are injected into the current session and their token sizes. |
| `/context detail` | Shows detailed content of the injected workspace files in the current session. |
| `ls ~/.openclaw/workspace/` | Lists all files in the workspace directory (agent brain files). |
| `cat ~/.openclaw/workspace/SOUL.md` | Displays contents of SOUL.md file (voice/style configuration). |
| `wc -c ~/.openclaw/workspace/SOUL.md` | Shows character/byte count of SOUL.md file (size check). |
| `tail -f ~/.openclaw/logs/gateway.log` | Live-streams gateway logs for real-time debugging. |
| `launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist` | Unloads macOS LaunchAgent to stop persistent crash-loop restarts. |
| `rm ~/.openclaw/agents/main/agent/auth-profiles.json` | Clears cached auth profiles so fresh provider credentials can be used. |
| `sed -i.bak '/Respond only in pirate speak/d' ~/.openclaw/workspace/SOUL.md` | Removes the test pirate-rule line from SOUL.md and keeps a backup. |
| `cd ~/.openclaw/workspace && git init && git add . && git commit -m "Initial brain"` | Initializes local git backup for workspace files and creates first snapshot commit. |
| `cp -r ~/.openclaw/workspace/ ~/.openclaw/workspace-backup/` | Creates a full backup copy of the workspace directory. |