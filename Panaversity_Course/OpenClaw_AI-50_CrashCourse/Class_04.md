# [Memory & Commands](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/memory-and-commands)

## How the Memory System Works

Now that you have experienced one row of it (saving a preference, verifying it on disk, recalling it in a new session), here is the bigger picture. Your agent's memory mirrors the way you remember: each kind of human memory has a counterpart your agent uses every day.

![How the Memory System Works](/assets/Class04-01.png "How the Memory System Works")

Each row on the right is a real file or a real piece of code, not a metaphor. The rest of this lesson walks through them. Start with where they live in `~/.openclaw/workspace/`:

| Location | What It Stores | When It Loads |
| --- | --- | --- |
| **MEMORY.md** | Curated long-term memory: preferences, facts, key decisions | Every session start |
| **memory/YYYY-MM-DD.md** | Daily logs: session notes, conversation summaries | Today + yesterday at session start |

### When New Session Starts
- On every new session, OpenClaw loads all workspace context files.
- For memory specifically, it auto-loads:
  - `MEMORY.md` (your curated long-term notes and preferences)
  - Today's file in `memory/YYYY-MM-DD.md`
  - Yesterday's file in `memory/YYYY-MM-DD.md`

- `MEMORY.md` acts like a curated notebook:
  - You edit it intentionally with important preferences, facts, and decisions.
  - Because it loads every session, the agent can reliably reuse those preferences.

- `memory/` acts like a daily journal:
  - OpenClaw writes session summaries and observations there automatically.
  - Files are date-based, so you usually get one log file per active day.

- Older memory files are not auto-loaded at startup:
  - Only today + yesterday are loaded by default.
  - Older logs stay on disk until needed.

- How older notes are accessed:
  - `memory_search` finds relevant old snippets using meaning + keyword matching.
  - `memory_get` opens a specific file or line range when path/context is known.

- Quick mental model:
  - `memory_search` = find the right note/snippet.
  - `memory_get` = open and read exact content.

**Example: How OpenClaw searches memory**
If you ask: *"How to do accounting?"*
1. OpenClaw checks the loaded `MEMORY.md`, today's and yesterday's logs.
2. If not found, it runs `memory_search` to locate relevant older snippets.
3. Once a snippet is identified, `memory_get` retrieves the full file/content.

![When New Session Starts](/assets/Class04-02.png "When New Session Starts")

### [memory_search and memory_get: Finding and Reading Old Notes](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/memory-and-commands#memory_search-and-memory_get-finding-and-reading-old-notes)

- Today's and yesterday's logs load automatically at session start.
- Older logs stay on disk but don't load automatically.
- When the agent needs something from older notes, it uses two tools from the active memory plugin (default: `memory-core`):

**`memory_search`**
- Finds relevant notes using hybrid retrieval:
  - Vector similarity (matches meaning)
  - Keyword matching (matches exact terms, IDs, or code symbols)
- Returns a ranked list of snippets.
- OpenClaw auto-detects embedding provider from available API keys (OpenAI, Gemini, Voyage, or Mistral).
- No configuration needed if you already have an API key.

**`memory_get`**
- Reads a specific memory file or line range.
- Used when the agent already knows the path (e.g., today's daily log).
- Also used to get full context of a snippet returned by `memory_search`.

**Simple mental model:**
- `memory_search` = finds the needle in the haystack.
- `memory_get` = reads the page once you know which page.

![memory_search and memory_get: Finding and Reading Old Notes](/assets/Class04-04.png "memory_search and memory_get: Finding and Reading Old Notes")

### [Three Paths to MEMORY.md](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/memory-and-commands#three-paths-to-memorymd)

`Save in memory:` is one of three ways content lands in `MEMORY.md`. The other two are automatic:

**1. Manual (You Control)**
- You say `Save in memory:` and the agent writes to `MEMORY.md` immediately.
- You can verify the content on disk.

**2. Compaction Memory Flush (Automatic)**
- When a conversation runs long, the gateway runs a silent turn before summarizing older messages.
- In that turn, the agent saves anything important from the conversation to `MEMORY.md` or today's daily log.

**3. Dreaming Deep Phase (Opt-in, Scheduled)**
- A background sweep that scores candidates from your daily logs.
- Promotes only those that pass score, recall-frequency, and query-diversity thresholds.
- Must be enabled; not automatic by default.

**Note:** If notes appear in `MEMORY.md` without you typing `Save in memory:`, paths 2 or 3 put them there.

### The Loading Summary

```
Session starts:
  ├── MEMORY.md          → always loads (curated, long-term)
  ├── memory/today.md    → always loads (today's journal)
  ├── memory/yesterday.md → always loads (yesterday's journal)
  └── memory/older/*.md  → available via memory_search only
```

### [When You Outgrow the Builtin Engine](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/memory-and-commands#when-you-outgrow-the-builtin-engine)

All four memory backends speak the same `memory_search` and `memory_get` tools. Your skills and prompts do not change when you swap. Switch in config; the tool calls stay identical.

| Backend | What It Adds | When to Pick It |
| --- | --- | --- |
| **Builtin** (default) | SQLite with vector + keyword search | Most personal setups. Already what you are using. |
| **QMD** | BM25 + vector + reranking, indexes external directories, can index session transcripts | You want higher-quality results, search beyond your workspace, or fully local with no API keys. |
| **Honcho** | AI-native service that auto-builds user profiles, cross-session memory, multi-agent tracking | You want automatic profile building or memory shared across multiple agents. |
| **LanceDB** | Local embeddings, Ollama-friendly | Fully local with Ollama; no external API at all. |

You do not need to switch today. When the builtin engine starts feeling slow or limited, the [memory concepts docs](https://docs.openclaw.ai/concepts/memory) walk through configuration for each backend.

### [Compaction and the Silent Memory Flush](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/memory-and-commands#compaction-and-the-silent-memory-flush)

- **Compaction** happens when a conversation runs long and the context window fills up.
- Older turns get summarized into a compressed version to free space for new turns.
- The summary preserves the gist but loses precise wording.
- Risk: anything important never written to a file may be compressed away and lost.

**Silent Memory Flush**
- Before compaction runs, OpenClaw runs a silent turn to protect important context.
- The agent receives a system reminder to write anything important to memory files.
- Important items (decisions, facts, key context) get saved to `MEMORY.md` or today's daily log.
- Then compaction happens — the summary replaces older turns, but durable bits are already on disk.
- This is enabled by default; no configuration needed.

**Manual Compaction**
- If the conversation feels sluggish or the agent loses track, trigger compaction manually:
  ```
  /compact
  ```
- This runs the same memory flush, then summarizes older turns, then continues.

![Compaction and the Silent Memory Flush](/assets/Class04-03.png "Compaction and the Silent Memory Flush")

# Agents Skills

## [Install Skills & Discover the Ecosystem](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem)

## Three Ways to Extend Your Agent (Inside the Gateway)

Your agent runs inside a gateway started in Lesson 2. Three things can be installed to extend the agent inside that gateway:

**1. Skill**
- Knowledge the agent reads on demand.
- A folder containing a `SKILL.md` file with instructions.
- Cross-platform standard: works in OpenClaw, Claude Code, and other agent platforms.
- Think of it as a textbook the agent picks up when the topic comes up.
- Install skills from `ClawHub`.

**2. Native Plugin**
- A gateway capability written in TypeScript that runs in-process inside the gateway.
- Examples: channels (WhatsApp, Discord), model providers (Google, Anthropic), voice plugins.
- Already bundled with your install; most load by default.
- Think of it as a new in-process feature welded to the gateway itself.

**3. Bundle Plugin**
- A gateway capability written as files only, no TypeScript.
- Uses the `.claude-plugin/` directory format (same as Claude Code and Cowork).
- Packages domain workflows (marketing, finance, legal, customer support) as skills, commands, and connectors.
- Think of it as a new department added to your agent without writing code.
- Install from a repo or from ClawHub.

**Note:** There is a fourth way to extend your agent: connecting to external services through MCP servers (covered in Lesson 7). This lesson covers what runs inside the gateway.

## [ClawHub: The Skill Marketplace](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem#clawhub-the-skill-marketplace)

- **ClawHub** = npm for agent skills: public registry, vector-search, versioning.
- Search with `openclaw skills search <term>` (e.g., `openclaw skills search booking`).
- Install with `openclaw skills install <skill>` → lands in `workspace/skills/` (gateway restart required).
- Update all installed skills with `openclaw skills update --all`.
- Skills are bundles that can be dropped into your agent's skill set.

### [Use the Skill You Just Installed](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem#use-the-skill-you-just-installed)

- Restart gateway after install: `openclaw gateway restart`.
- Verify installation: `openclaw skills list` — your skill (e.g., `service-booking`) should appear.
- If not listed, re-install and restart again.
- To use the skill: ask the agent (e.g., *"Use the service-booking skill to find a plumber near me"*).
- The agent loads the skill's instructions and follows its workflow; if it connects to MCP servers, real tools are invoked.
- **Teach your agent where to look**: add `Skills are installed in ~/.openclaw/workspace/skills/` to `~/.openclaw/workspace/AGENTS.md` so every session knows where skills live.
- **Model quality matters**: free-tier models (e.g., `gemini-3.1-flash-lite`) may skip skill use. Verify readiness in dashboard → Skills tab; upgrade model if needed.
