# 02: Spec-Kit Plus Crash Course

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

# To install in existance project
specifyplus init --here
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
### Spec-Kit Plus Command

You should see the core Spec-Kit Plus commands:

* **`sp.tasks:`** Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
* **`sp.specify:`** Create or update the feature specification from a natural language feature description.
* **`sp.plan:`** Execute the implementation planning workflow using the plan template to generate design artifacts.
* **`sp.phr:`** Record an AI exchange as a Prompt History Record (PHR) for learning and traceability.
* **`sp.implement:`** Execute the implementation plan by processing and executing all tasks defined in tasks.md
* **`sp.git.commit_pr:`** An autonomous Git agent that intelligently executes git workflows. Your task is to intelligently executes git workflows to commit the work and create PR.
* **`sp.constitution:`** Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync
* **`sp.clarify:`** Identify underspecified areas in the current feature spec by asking up to 5 highly targeted clarification questions and encoding answers back into the spec.
* **`sp.checklist:`** Generate a custom checklist for the current feature based on user requirements.
* **`sp.analyze:`** Perform a non-destructive cross-artifact consistency and quality analysis across spec.md, plan.md, and tasks.md after task generation.
* **`sp.adr:`** Review planning artifacts for architecturally significant decisions and create ADRs.
* **`setup-github:`** Set up GitHub Actions
* **`terminal-setup:`** Configure terminal keybindings for multiline input (VS Code, Cursor, Windsurf)

## [Constitution Phase — Project-Wide Quality Standards](https://github.com/panaversity/ai-native-software-development/blob/main/book-source/docs/04-SDD-RI-Fundamentals/14-spec-kit-plus-hands-on/03-constitution-phase.md)

After setup, the first aim is to write constitution, constitution is a foundational rules that will guide every part of your project.

**Constitution applies to:**
* `Code quality standard` (type hint, docstrings, naming conventions)
* `Testing requirement` (unit test, integration test, coverage targets)
* `Error handling pattern` (exception hierarchy, error messages, logging)
* `Security practices` (no hardcoded secrets, input validation, data handling)
* `Documentation expectation` (README, code comments, docstrings)

### Part B: Writing Your Calculator Project Constitution

**Run /sp.constitution**

/sp.constitution

Project Principle and Standards:
- Write test first (TDD approach)
- Use Python 3.12+ with type hints everywhere
- Keep code clean and easy to read
- Document important decisions with ADRs
- Follow essential OOP princples: SOLID, KISS, DRY

Technical stack:
- Python 3.12+ with UV package manager
- pytest for testing

Quality Requirement:
- All test must pass
- At least 80% code coverage
- Use dataclasses for data structures

**Review Your Constitution**
After the agent generates your Constitution, review it carefully.

Your Prompt:

```bash
Show me the generated constitution file and explain what it contains.

```
Agent shows:
* `Core Principles` — Your research philosophy
* `Quality Standards` — Testable criteria for all papers
* `Source Requirements` — Citation and verification rules
* `Constraints` — Length, format, deadlines
* `Success Criteria` — How to know if standards are met

**Improve Your Constitution**
Think about what "good research" means for YOUR project. Ask the agent:

```bash
  Review my Constitution at .specify/memory/constitution.md and improve it:

  1. Are all standards testable (not vague)?
    - ❌ Vague: "Papers should be well-written"
    - ✅ Testable: "Flesch-Kincaid grade 10-12; active voice 75%+ of time"

  2. Did I cover essential categories?
    - Citation accuracy
    - Source verification
    - Writing clarity
    - Plagiarism checking
    - Review process

  3. Are any standards unrealistic?

  Suggest 2-3 concrete improvements.
```

## [Specify Phase — Writing Complete Specifications](https://github.com/panaversity/ai-native-software-development/blob/main/book-source/docs/04-SDD-RI-Fundamentals/14-spec-kit-plus-hands-on/04-specify-phase.md)

### Part A: Pre-Specification Conversation

Here's how professionals work: YOU drive the exploration through questions. The AI doesn't interview you; you use the AI to think through requirements.

#### Step 1: Start the Conversation
Open your AI tool in your my-research-paper directory:

```
I am writing a specification for a calculator Python library.
Let me clarify what success looks like with you:

1. What operation should my calculator support?
2. What edge cases should I handle?
3. What's my definition of "correct" for floating-point results?
4. How should the calculator interface work (Library VS CLI)?
5. What should happen with invalid input?

```

#### Step 2: Summarize What You Learned

From the conversation, you now know:
* `Purpose:` Define what users need in plain English
* `Focus:` User journeys, acceptance criteria, success metrics
* `Avoid:` Technical details, code structure, implementations
* `Output:` **spec.md** file

### Part B: Write Your Specification
Now formalize the conversation into a specification using /sp.specify.

#### Step 1: Run /sp.specify

After converation with agent, use `sp.specify`[your command] to create spec.md file in specs/[your project name folder]

#### Step 2: Review the Generated Specification
After the agent creates your spec, review it:

```
Show me the generated specification and explain what each section contains.
```

#### Step 3: Verify Completeness
Check that your specification has:

```
Specification Checklist:

[ ] Intent is clear (someone unfamiliar can understand the goal)
[ ] Constraints are specific and testable (not vague "do good work")
[ ] Success Evals are SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
[ ] Non-Goals are explicit (prevents scope creep)
[ ] No "how" leaked in (describes what, not how to build)
[ ] Written clearly enough that another person could write from it
```
## [Clarify Phase](https://github.com/panaversity/ai-native-software-development/blob/main/book-source/docs/04-SDD-RI-Fundamentals/14-spec-kit-plus-hands-on/05-clarify-phase.md)

* You wrote a specification for your calculator project. It looked complete. But there are always gaps you didn't catch—ambiguities that seemed clear in your head but are actually vague on paper. Assumptions about scope, audience, or success that you didn't state explicitly.

* This is where the `/sp.clarify` command helps. Clarify is a quick check that your specification is complete before moving to planning.
* To improve specs we have a command named `/sp.clarify`, run it

### What Does /sp.clarify Do?

**The Clarify Command**

/sp.clarify analyzes your specification and reports:

1. Ambiguous Terms
2. Missing Assumptions
3. Incomplete Requirements
4. Scope Conflicts

## [Plan Phase — Architecture Decisions and ADRs](https://github.com/panaversity/ai-native-software-development/blob/main/book-source/docs/04-SDD-RI-Fundamentals/14-spec-kit-plus-hands-on/06-plan-phase.md)

With your specification complete and clarified, you now face a new question: **How will you actually build it?** This is the essence of the Plan Phase—transforming the "What" of your specification into the "How" of architecture and implementation strategy.

`/sp.plan` generates an implementation plan that breaks your specification into:

* **Architectural components** (sections, research management, quality validation)
* **Implementation phases** (research first, then writing, then polish)
* **Dependencies** (what must be completed before what)
* **Design decisions** (which ones matter enough to document)

This lesson teaches you how to work with generated plans and how to capture important architectural decisions using **ADRs (Architectural Decision Records).**

Write below detail in CLI to execute.

```
/sp.plan

Create: architecture sketch, interfaces, data model, error handling, requirements.
Decision needing: list important choices with options and tradeoffs.
Testing Strategy: unit + integration tests based on acceptance criteria.

Technical Details:
- Use a simple function approach where it makes sense.
- Use python 3.12+ type hints with | union syntax
- Follow TDD: write test first, then implementation.
- Organize code and tests according to your constitution rules.
```

## [Tasks Phase - Atomic Work Units and Checkpoints](https://github.com/panaversity/ai-native-software-development/blob/main/book-source/docs/04-SDD-RI-Fundamentals/14-spec-kit-plus-hands-on/07-tasks-phase.md)

Next: Break the plan into atomic work units (tasks) that you'll execute. Each task is 15-30 minutes, has one acceptance criterion, and produces a verifiable output.

This lesson teaches the checkpoint pattern—the critical workflow practice that keeps YOU in control.

```
sp.tasks

My calculator specification is at specs/001-basic-calculator/spec.md
My implementation plan is at specs/001-basic-calculator/plan.md

Please decompose the plan into atomic work unit (tasks), each task should be testable, reversible and with clear dependencies.

Use a TDD approach: for each operation (add, substract, etc.),
1. Write RED tests
2. Implement them
3. Refactor

Pause after each group for human review before committing.

Also:
- Use Context7 MCP server for documentation loop
- Prefer CLI automation where possible
- Ensure easy rollback and traceability.
```

## [Implement Phase — Execute Tasks with AI Collaboration](https://github.com/panaversity/ai-native-software-development/blob/main/book-source/docs/04-SDD-RI-Fundamentals/14-spec-kit-plus-hands-on/08-implement-phase.md)

You have a specification that defines what you're building, a plan that outlines the strategy, and tasks that break the work into atomic units. Now comes the execution phase: actually doing the work with your AI companion.

This lesson focuses on control and validation. Implementation isn't just "run tasks autonomously." It's you and AI working together—you deciding direction, AI handling execution, both of you validating results against the specification.

### The /sp.implement Command
When you run `/sp.implement` in Claude Code, the command reads your tasks.md and orchestrates their execution with your AI companion.

**Basic usage:**
```
/sp.implement
```
The agent will:

1. Read your tasks.md
2. Begin executing tasks in dependency order
3. Show outputs and intermediate results
4. Wait for your review at checkpoint boundaries
5. Continue on your approval

**You maintain control.** The agent doesn't proceed autonomously; it presents work and waits for your decision.
