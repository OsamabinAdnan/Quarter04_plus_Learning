# OpenClaw Commands (Class 01 + Class 02 + Class 03 + Class 04 + Class 05)

| Command | Functionality |
|---|---|
| `wsl --install -d Ubuntu` | Enables WSL, installs WSL2 kernel, and installs Ubuntu on Windows. |
| `wsl -d Ubuntu` | Starts Ubuntu distribution in WSL. |
| `curl -fsSL https://openclaw.ai/install.sh bash` | Installs OpenClaw (and Node.js if needed) inside Linux/WSL. |
| `openclaw --version` | Shows installed OpenClaw version and verifies installation. |
| `openclaw onboard --install-daemon` | Starts onboarding wizard and installs gateway daemon/service. |
| `openclaw onboard` or `openclaw setup --useit` | Starts interactive onboarding wizard. |
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
| `ls ~/.openclaw/workspace/memory/` | Lists daily memory log files stored in the workspace memory directory. |
| `/compact` | Manually triggers compaction; OpenClaw flushes important memory first, then summarizes older turns. |
| `openclaw skills search booking` | Searches ClawHub for skills related to booking. |
| `openclaw skills install service-booking` | Installs the `service-booking` skill into the workspace `skills/` directory. |
| `openclaw skills update --all` | Updates all installed skills to their latest versions. |
| `openclaw skills list` | Lists installed skills currently available to the gateway. |
| `npx skills add <repo-url>` | Installs an Agent Skill from a repository URL for both Claude Code and OpenClaw. |
| `ls .claude/skills/` | Lists skills installed for Claude Code in the current project. |
| `ls skills/` | Lists skills installed for OpenClaw in the current project. |
| `cat .claude/skills/<name>/SKILL.md` | Displays the SKILL.md file for a Claude Code skill. |
| `cat skills/<name>/SKILL.md` | Displays the SKILL.md file for an OpenClaw skill. |
| `rm -rf .claude/skills/<name> skills/<name>` | Removes a skill from both Claude Code and OpenClaw project directories. |
| `claude` | Starts Claude Code interactive session in the terminal. |
| `/<skill-name> <input>` | Explicitly invokes a skill in Claude Code/OpenCode with input. |
| `/skill <name>` | Explicitly invokes a skill in OpenClaw DM. |
| `npx skills add https://github.com/anthropics/skills --skill skill-creator` | Installs the skill-creator tool for authoring custom skills. |
| `/skill-creator` | Invokes the skill-creator tool in Claude Code to author a new skill. |
| `openclaw pairing approve whatsapp <code>` | Approves a pairing request for WhatsApp direct messages (used with dmPolicy: "pairing"). |
| `openclaw config set channels.whatsapp.groupPolicy "open"` | Sets WhatsApp group policy to "open" (anyone can @mention), "allowlist" (whitelist only), or "disabled" (no groups). |
| `openclaw config set channels.whatsapp.dmPolicy "pairing"` | Sets WhatsApp DM policy to "pairing" (requires approval), "allowlist" (pre-approved only), "open" (anyone), or "disabled" (no DMs). |
| `openclaw config set channels.whatsapp.ackReaction.group "always"` | Sets WhatsApp to send full replies in groups (not just reaction emojis). |