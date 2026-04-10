# 01: Spec-Kit Plus Crash Course

* We can implement AI in 3 ways in development
    1. AI Assisted Development
        * Getting little help from AI as an assitant during coding 
    2. AI Driven Development
        * We specify requirement to AI and it make up stuff according to it, like make TODO app
    3. AI Native Development
        * We make agent from AI agent, it likes coding agent is making consumer agent

## Claude Code Installtion Guide
[Chapter 5: How It All Started — The Claude Code Phenomenon](https://ai-native.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows)

## Gemini CLI Installation Guide
[Chapter 6: Google Gemini CLI: Open Source and Everywhere](https://ai-native.panaversity.org/docs/AI-Tool-Landscape/gemini-cli-installation-and-basics)

## Spec-Kit Plus Setup
* For Spec-Kit Plus Setup from website
[Part 04 | Chap # 14 Installation and Setup](https://ai-native.panaversity.org/docs/SDD-RI-Fundamentals/spec-kit-plus-hands-on/installation-and-setup)

* For Spec-Kit Plus Setup from Github
[04-SDD-RI-Fundamentals/14-spec-kit-plus-hands-on](https://github.com/panaversity/ai-native-software-development/tree/main/book-source/docs/04-SDD-RI-Fundamentals/14-spec-kit-plus-hands-on)

### Step 1: Install Spec-Kit Plus

With Python 3.12+ confirmed, install Spec-Kit Plus:

```bash
# Install the framework
pip install specifyplus

# Verify installation
specifyplus --version
```

**What you just installed:**

- **specifyplus** — The Spec-Kit Plus framework with slash commands, templates, and project scaffolding
- This is SEPARATE from your AI tool (Claude Code or Gemini CLI)

**Important distinction:** Spec-Kit Plus is a framework. Claude Code/Gemini CLI is the AI tool that executes the framework's commands. You need BOTH.

---

### Step 2: Initialize Your First Project

Create a new Spec-Kit Plus project for your research paper:

```bash
# Create a new project
specifyplus init my-research-paper
```

**Interactive prompts:**

During initialization, you'll see:

```
? Select AI Tool:
  > Claude Code
    Gemini CLI

? Select Terminal:
  > bash
    powershell (Windows only)
```

**Recommendations:**
- **AI Tool**: Choose Claude Code (recommended for this book)
- **Terminal**: Choose bash (or powershell if on Windows without WSL)

---

### Step 3: Navigate to Your Project

```bash
cd my-research-paper
```

---

### Step 4: Verify Project Structure

After initialization, you should see this directory structure:

```
my-research-paper/
├── .claude/
│   └── commands/                    # Slash commands for SDD workflow
│       ├── sp.adr.md                # Document architectural decisions
│       ├── sp.analyze.md            # Cross-artifact consistency checks
│       ├── sp.checklist.md          # Generate custom checklists
│       ├── sp.clarify.md            # Refine specifications
│       ├── sp.constitution.md       # Create project constitution
│       ├── sp.git.commit_pr.md      # Commit and create PRs
│       ├── sp.implement.md          # Execute tasks with AI
│       ├── sp.phr.md                # Record prompt history
│       ├── sp.plan.md               # Generate implementation plans
│       ├── sp.specify.md            # Create specifications
│       └── sp.tasks.md              # Break plans into atomic tasks
│
├── .specify/
│   ├── memory/
│   │   └── constitution.md          # Project-wide rules and principles
│   │
│   ├── scripts/
│   │   └── bash/                    # Automation scripts
│   │       ├── check-prerequisites.sh
│   │       ├── common.sh
│   │       ├── create-adr.sh
│   │       ├── create-new-feature.sh
│   │       ├── create-phr.sh
│   │       ├── setup-plan.sh
│   │       └── update-agent-context.sh
│   │
│   └── templates/                   # Templates for specs, plans, tasks
│       ├── adr-template.md
│       ├── agent-file-template.md
│       ├── checklist-template.md
│       ├── phr-template.prompt.md
│       ├── plan-template.md
│       ├── spec-template.md
│       └── tasks-template.md
│
├── .git/                            # Git repository (auto-initialized)
├── CLAUDE.md                        # Agent instructions and guidelines
├── README.md                        # Project documentation
└── .gitignore                       # Git ignore rules
```

**Note:** The `specs/`, `history/prompts/`, and `history/adr/` directories will be created automatically when you start your first feature.

---

### Understanding Key Directories

| Directory | Purpose |
|-----------|---------|
| `.claude/commands/` | Slash commands you'll use throughout the SDD workflow (`/sp.specify`, `/sp.plan`, etc.) |
| `.specify/memory/` | Your project constitution (created once, referenced always) |
| `.specify/scripts/` | Automation scripts for PHRs, ADRs, and feature setup |
| `.specify/templates/` | Templates that guide spec, plan, task, ADR, and PHR creation |
| `CLAUDE.md` | Agent instructions that guide your AI collaborator's behavior |
| `specs/` | (Created later) Your feature specifications |
| `history/` | (Created later) ADRs and PHRs for knowledge capture |

---

### Step 5: Verify Commands Work

Now test that everything is connected.

**Launch your AI tool** in the project directory:

```bash
# From my-research-paper directory
claude
```

(Or `gemini` if using Gemini CLI)

**Test slash command access:**

Inside your AI tool, type:

```
/sp.
```

You should see the core Spec-Kit Plus commands:

- `/sp.constitution` — Build your constitution
- `/sp.specify` — Launch specification workflow
- `/sp.clarify` — Refine and validate specs
- `/sp.plan` — Generate implementation plan
- `/sp.adr` — Document architectural decisions
- `/sp.tasks` — Decompose plan into tasks
- `/sp.implement` — Execute tasks with AI
- `/sp.phr` — Record prompt history

If commands appear, your installation is complete!

---

### Common Mistakes

#### Mistake 1: Confusing Spec-Kit Plus with Claude Code

**The error:** "I installed Claude Code, so I have Spec-Kit Plus now."

**Why it's wrong:** Spec-Kit Plus is a separate framework. Claude Code is just the AI tool that executes Spec-Kit Plus commands.

**The fix:** Install BOTH:
- `pip install specifyplus` (framework)
- Configure Claude Code or Gemini CLI (AI tool)

#### Mistake 2: Skipping Project Initialization

**The error:** Creating folders manually instead of running `specifyplus init`

**Why it's wrong:** You miss critical infrastructure (`.specify/` templates, slash commands, configuration files).

**The fix:** Always run `specifyplus init <project-name>` to set up proper structure.

#### Mistake 3: Wrong Python Version

**The error:** `pip install specifyplus` fails or commands don't work

**Why it's wrong:** Spec-Kit Plus requires Python 3.12+

**The fix:** Check `python --version` and upgrade if needed. See [Chapter 11](/docs/05-Python-Foundations/15-setting-up-python/README.md) for installation instructions.

---

### Try With AI

Verify your installation is complete with these prompts:

**Verify Project Structure:**

> "I just installed Spec-Kit Plus and ran `specifyplus init my-research-paper`. Walk me through the directory structure: What's the purpose of `.specify/`, `.claude/commands/`, and `specs/`? How do these directories support the SDD-RI workflow?"

**Test Command Access:**

> "Help me verify my Spec-Kit Plus installation is complete. I'll type `/sp.` and show you what commands appear. Which command should I test first to confirm everything works?"

**Understand Framework vs Tool:**

> "Explain the difference between Spec-Kit Plus (framework) and Claude Code (AI tool). If I switch from Claude Code to Gemini CLI later, what changes and what stays the same?"

**Preview Next Steps:**

> "Based on my project structure, what should I do next to start my research paper? Walk me through the workflow: Which `/sp.` commands in which order?"

