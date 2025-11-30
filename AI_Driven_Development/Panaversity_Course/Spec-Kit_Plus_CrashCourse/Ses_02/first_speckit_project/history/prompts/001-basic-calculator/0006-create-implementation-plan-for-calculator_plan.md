---
id: 0006
title: Create Implementation Plan for Calculator
stage: plan
date: 2025-11-29
surface: agent
model: gemini-pro
feature: 001-basic-calculator
branch: 001-basic-calculator
user: User
command: /sp.plan Create: architecture sketch, interfaces, data model, error handling, requirements. Decision needing: list important choices with options and tradeoffs. Testing Strategy: unit + integration tests based on acceptance criteria. Technical Details: - Use a simple function approach where it makes sense. - Use python 3.12+ type hints with | union syntax - Follow TDD: write test first, then implementation. - Organize code and tests according to your constitution rules.
labels: [plan, architecture, tdd, python]
links:
  spec: specs/001-basic-calculator/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-basic-calculator/plan.md
  - specs/001-basic-calculator/research.md
  - specs/001-basic-calculator/data-model.md
  - specs/001-basic-calculator/quickstart.md
tests:
  - none
---

## Prompt

---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

## User Input

```text
Create: architecture sketch, interfaces, data model, error handling, requirements.
Decision needing: list important choices with options and tradeoffs.
Testing Strategy: unit + integration tests based on acceptance criteria.

Technical Details:
- Use a simple function approach where it makes sense.
- Use python 3.12+ type hints with | union syntax
- Follow TDD: write test first, then implementation.
- Organize code and tests according to your constitution rules.
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'm Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType gemini`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

## Response snapshot

The planning phase is complete. I have created the implementation plan and all associated design artifacts. The project is ready to be broken down into tasks.

- **Implementation Plan:** `specs/001-basic-calculator/plan.md`
- **Research & Decisions:** `specs/001-basic-calculator/research.md`
- **Data Model:** `specs/001-basic-calculator/data-model.md`
- **Quickstart Guide:** `specs/001-basic-calculator/quickstart.md`

The next recommended command is `/sp.tasks`.

## Outcome

- ✅ Impact: Created a comprehensive implementation plan and all associated design artifacts.
- 🧪 Tests: No tests were run.
- 📁 Files: 
  - `specs/001-basic-calculator/plan.md`
  - `specs/001-basic-calculator/research.md`
  - `specs/001-basic-calculator/data-model.md`
  - `specs/001-basic-calculator/quickstart.md`
  - `history/prompts/001-basic-calculator/0006-create-implementation-plan-for-calculator.plan.prompt.md`
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: The planning phase went smoothly. The prior clarification phase ensured that there were no ambiguities to resolve. The user's technical constraints were clear and easily incorporated into the plan. The failure of the agent context script was noted, but did not impede the process.

## Evaluation notes (flywheel)

- Failure modes observed: `update-agent-context.ps1` script failed due to a missing template file.
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): Ensure the `.specify/templates` directory is fully populated during project initialization to prevent script failures.
