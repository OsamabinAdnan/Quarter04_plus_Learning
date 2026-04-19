# OpenClaw Commands (Class 01 + Class 02)

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
| `tail -f ~/.openclaw/logs/gateway.log` | Live-streams gateway logs for real-time debugging. |
| `openclaw tui` | Launches terminal UI to interact with the AI Employee from CLI. |
| `openclaw gateway status` | Shows current gateway health/status and runtime state. |
| `openclaw doctor` | Runs diagnostics on environment, config, network, and service status. |
| `openclaw logs` | Shows OpenClaw runtime/gateway logs for debugging. |
| `openclaw doctor --repair` | Attempts automatic detection and repair of common issues. |
| `openclaw config get gateway.mode` | Checks configured gateway mode (e.g., `local`). |
| `openclaw config set gateway.mode local` | Sets gateway mode to local (common crash-loop fix). |
| `launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist` | Unloads macOS LaunchAgent to stop persistent crash-loop restarts. |
| `rm ~/.openclaw/agents/main/agent/auth-profiles.json` | Clears cached auth profiles so fresh provider credentials can be used. |
| `openclaw configure --section model` | Opens model/provider configuration section (useful for quota/provider switch). |
| `openclaw plugins list` | Lists available/bundled plugins. |
| `openclaw config set plugins.entries.<id>.enabled true` | Enables a specific plugin by ID. |
| `openclaw configure --section channels` | Opens channel configuration section (WhatsApp/Telegram/Discord setup). |