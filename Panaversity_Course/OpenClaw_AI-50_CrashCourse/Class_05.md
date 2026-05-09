# Agent Skills (cont.)

## [Install & Author Agent Skills](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem)

We will use claude or any other tool to automate working in claude code for that we downloaded this folder [openclaw-employee](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-and-connect#let-a-coding-agent-do-the-install) from Agent Factory book website. see folder in this project at root level.

## What is an Agent Skill?

- **Definition (agentskills.io):** A lightweight, open format for extending AI agents with specialized knowledge + workflows.
- **Origin:** Created by Anthropic and released as an open standard; many agent products support it.
- **Mental model:** Skills are like **laminated playbooks** on a shelf.
  - Each playbook has a **title** (when to use it).
  - A **procedure/workflow** (what steps to follow).
  - Optional **tools/scripts** bundled for steps that need automation.
- **How an agent uses skills:**
  - It does **not** read every skill every time.
  - It scans titles, selects the best match, opens that one, follows it, then moves on.
- **Key idea:** You install skills once; the agent chooses and uses the right one on demand.
- **Example:** refund handling, meeting summaries, currency conversion (USD → PKR), etc.
- **Note:** Skills are stored in your workspace skills directory and loaded by gateway after restart.
- Skills are open format and portable across platforms (OpenClaw, Claude Code, etc.).
- They help agents do consistent and repeatable tasks.

![Agent Skills](/assets/Class05-01.png "What is Agent Skill")

## [Section 1: Pick a real wish on skills.sh](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem#section-1-pick-a-real-wish-on-skillssh)

- Open https://skills.sh/ in your browser.
- In the search box, type a **real wish**: something you actually want your AI Employee to do that it cannot do yet.
- Good starter wishes:
  - meeting summary
  - customer reply draft
  - marketing campaign brief
  - code review checklist
  - expense classification
  - daily standup summary
  - one-page research summary

![Skills.sh](/assets/Class05-02.png "Pick a real wish on skills.sh")

Simply copy and paste installation command from skills.sh and install that skill in your project. I have installed it on global level.

## [Section 2: Install across both runtimes](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem#section-2-install-across-both-runtimes)

- Open terminal in `openclaw-employee/` folder (your workspace for this lesson).
- Paste the install command from Section 1.
- CLI opens interactive multi-select:
  - "Universal targets" group is pre-checked (~13 runtimes: Amp, Antigravity, Cline, Codex, Cursor, OpenCode, etc.).
  - **Manually check Claude Code AND OpenClaw**, then confirm.
- Next prompt: **Project vs Global scope**
  - **Project**: installs to `.claude/skills/` (Claude Code) and `skills/` (OpenClaw) in current folder only.
  - **Global**: installs to `~/.claude/skills/` and `~/.openclaw/skills/` for all sessions/folders.
- **Pick Project for now** (to see SKILL.md next to AGENTS.md/CLAUDE.md in `openclaw-employee/`).

**Verify installation:**
```bash
ls .claude/skills/
ls skills/
```
You should see the skill folder in both locations.

**Promoting Project → Global later:**
```bash
npx skills add <same-repo-url>
# multi-select: Claude Code + OpenClaw
# scope: Global this time
```
Fresh copies land in `~/.claude/skills/<name>/` and `~/.openclaw/skills/<name>/`.

**Optional cleanup (remove Project copies):**
```bash
rm -rf .claude/skills/<name> skills/<name>
```

**Notes:**
- OpenClaw's skill watcher (`skills.load.watch`, 250ms debounce) picks up Global drops automatically; no restart needed.
- Workspace beats Global on collisions (6 tiers covered in Section 8).
- If both exist, Project copy takes precedence from `openclaw-employee/`.

## [Section 3: Try in Claude Code first](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem#section-3-try-in-claude-code-first)

- Fastest cross-runtime proof is in the terminal where your coding agent runs.
- Claude Code (or OpenCode) shows structurally different output immediately when skill fires.

**Start your coding agent:**
```bash
claude or Opencode
```

**Invoke the skill:**
```bash
/<skill-name> <real input from your domain>
```
(Use the skill's slug from install; check `.claude/skills/` folder names if unsure.)

**Three ways to use a skill:**

1. **Auto-activation (default)**
   - Gateway compares your message to every installed skill's description.
   - If one matches, skill loads automatically.
   - No slash needed; best for everyday use.

2. **Explicit `/<skill-name>` (what you just did)**
   - Forces skill to load regardless of description match.
   - Useful for testing, authoring, or when you know exactly which playbook applies.
   - In Claude Code/OpenCode: `/<skill-name>`
   - In OpenClaw DM: `/skill <name>`

3. **Pinned to Employee's brain**
   - Add to `MEMORY.md`, `IDENTITY.md`, or `USER.md`:
     - Example: *"When I ask for a meeting summary, always use the meeting-summary skill."*
   - Skill becomes part of who the Employee is.

**Troubleshooting: Employee not using installed skill?**
- **Cause 1:** Description doesn't match your phrasing.
  - Fix: Read `SKILL.md` description and rephrase your request, OR sharpen the description if you authored it.
- **Cause 2:** You want always-on but never told the Employee.
  - Fix: Pin it via brain customization (edit `MEMORY.md`, `USER.md`, or `IDENTITY.md`).
- **Cause 3:** Use explicit invocation: `/<skill-name>` always works.

**Done when:** Claude Code's response is structurally different from no-skill response, and you can describe in one sentence what the skill changed.

## [Section 4: Read the SKILL.md by hand](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem#section-4-read-the-skillmd-by-hand)

**Skill folder structure:**
```
my-skill/
├── SKILL.md       # required: metadata + instructions
├── scripts/       # optional: executable code
├── references/    # optional: extra documentation
└── assets/        # optional: templates, resources
```

**Open the SKILL.md:**
```bash
cat .claude/skills/<name>/SKILL.md
# or for OpenClaw:
cat skills/<name>/SKILL.md
```
(Global paths: `~/.claude/skills/<name>/SKILL.md` and `~/.openclaw/skills/<name>/SKILL.md`)

### The Frontmatter

**Required fields:**
```yaml
---
name: research-brief
description: "Use this skill when the user asks for a one-page research summary, a paper digest, or a literature brief. Produces a structured output with key findings, methodology, and limitations."
---
```

- `name`: lowercase hyphen-case
- `description`: the trigger — gateway compares user message against all skill descriptions and loads only relevant ones
- Sharp description = fires exactly when needed; vague = never fires

**Optional OpenClaw-specific gates (single-line JSON):**
```yaml
metadata: { "openclaw": { "requires": { "bins": ["jq", "curl"] }, "os": ["darwin", "linux"], "primaryEnv": "ANTHROPIC_API_KEY" } }
```

**Common gates:**
- `requires.bins`: binaries that must exist (e.g., `["jq", "curl"]`)
- `requires.anyBins`: any one of a list
- `requires.env`: environment variables
- `requires.config`: OpenClaw config keys
- `os`: `["darwin", "linux", "win32"]`
- `primaryEnv`: env var the skill warns about if missing
- `user-invocable: false`: hides from slash-command menus (model-only)
- `disable-model-invocation: true`: inverse (user-only)

Skills failing any gate don't load at startup.

### The Body Structure

Below frontmatter = markdown with:
- Operational instructions
- Decision rules
- Output format

**Optional folders:**
```
research-brief/
├── SKILL.md          # required
├── scripts/          # optional: code the agent can call
└── references/       # optional: docs the agent reads on demand
```

- `scripts/`: executable code (Python, Bash, JS) for deterministic work
- `references/`: extra documentation linked from body
- Most skills only need markdown

**Agent-native thinking:**
- **Description** = trigger (gateway compares to user message, loads body if relevant)
- **Body** = recipe (instructions, decision rules, output format)
- **scripts/** = deterministic helpers (bash/Python/Node) from 7 principles
- This is **programming in English**; the agent is the runtime

**Done when:** You can name 3 frontmatter fields without looking AND explain why description is separated from body.

## [Section 5: See progressive disclosure live](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem#section-5-see-progressive-disclosure-live)

**Test progressive disclosure in Claude Code (or OpenCode):**

1. **Send a generic question** that does NOT match the skill's description.
   - Reply is generic; playbook stays on shelf.

2. **Send a question that DOES match** the description (same type as Section 3).
   - Reply is skill-shaped: specific sections, decision rules, format.
   - Body loaded for that turn only and steered the response.

**Progressive disclosure = spine read every turn, body opens only when needed.**

### Three Stages (Official Spec)

1. **Discovery (Session Start)**
   - Only name + description of every skill loads.
   - Agent knows when each skill might be relevant.
   - Agent is "reading the spines."

2. **Activation (Message Match)**
   - When user message matches description, full SKILL.md instructions load into context.
   - Agent "pulls playbook off the shelf."

3. **Execution (Follow Instructions)**
   - Agent follows instructions, optionally executing bundled code or loading referenced files.
   - Agent is "working through the procedure."

### Cost at Session Start

- System prompt baseline: **195 characters**
- Each skill adds: **~97 characters** (name + description + location)
- **~24 tokens per skill** at startup
- Bodies stay asleep until message wakes them

![Progressive Disclosure](/assets/Class05-03.png "Progressive Disclosure")

## [Section 6: Author your own with skill-creator](https://agentfactory.panaversity.org/docs/Building-OpenClaw-Apps/meet-your-personal-ai-employee/install-skills-discover-ecosystem#section-6-author-your-own-with-skill-creator)

**skill-creator** = Anthropic's conversational authoring tool (itself a SKILL.md).
- Rough intent in → tested SKILL.md out
- Ships with ~18 reference skills at [github.com/anthropics/skills](https://github.com/anthropics/skills)

**Install skill-creator:**
```bash
npx skills add https://github.com/anthropics/skills --skill skill-creator
```
- Multi-select: Claude Code AND OpenClaw
- Scope: **Project** (iterate without polluting Global)

**Pick a real recurring workflow:**
- Daily standup notes
- Customer reply template
- Code review checklist
- Expense classification
- Meeting summary
- Weekly status report

**Invoke skill-creator:**
```bash
claude
# then:
/skill-creator
```

**Authoring sequence:**
1. State the intent (when should this skill trigger?)
2. Draft the description (the matcher — decides if skill triggers)
3. Draft the body
4. Write 3 real example inputs
5. Run examples through draft
6. Refine description so it triggers reliably
7. Ship

**What happens:**
- skill-creator asks intent → you state it
- Drafts description → you refine
- Drafts body
- Asks for 3 real examples (meeting notes, customer messages, expense receipts)
- Runs examples through draft → shows output
- You correct what's wrong
- Description gets sharpened, body gets missing steps added
- 2-3 rounds usually converges

**Final output:**
- SKILL.md materializes in BOTH:
  - OpenClaw workspace `skills/` directory
  - Claude Code `.claude/skills/` directory
- skill-creator writes to both locations on ship

**Test once more in Claude Code** with real input to confirm:
- Description triggers cleanly
- Body produces expected structure

**Key insight:** You wrote one folder → two agent platforms read it the same way.

**Done when:** Your authored skill produces consistent structured output for real input in Claude Code, AND SKILL.md folder exists in both Claude Code and OpenClaw skills directories.

