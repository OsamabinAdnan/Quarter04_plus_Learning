# AI/Spec-Driven Book Project Constitution
<!-- Sync Impact Report:
Version change: 1.0.0 → 1.1.0
List of modified principles:
- I. Automated Content Generation
- II. Docusaurus-First Design
- III. Test-First (NON-NEGOTIABLE)
- IV. Hierarchical Content Structure
- V. Observability & Maintainability
- VI. Versioning & Deployability
- VII. Integrated RAG Chatbot (Added)
- VIII. Reusable Intelligence (Bonus) (Added)
Added sections: None
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending
- .specify/templates/spec-template.md: ⚠ pending
- .specify/templates/tasks-template.md: ⚠ pending
- .specify/templates/commands/sp.constitution.md: ✅ updated
- .specify/templates/commands/sp.phr.md: ⚠ pending
- .specify/templates/commands/sp.specify.md: ⚠ pending
- .specify/templates/commands/sp.plan.md: ⚠ pending
- .specify/templates/commands/sp.tasks.md: ⚠ pending
- .specify/templates/commands/sp.implement.md: ⚠ pending
- .specify/templates/commands/sp.git.commit_pr.md: ⚠ pending
- .specify/templates/commands/sp.clarify.md: ⚠ pending
- .specify/templates/commands/sp.checklist.md: ⚠ pending
- .specify/templates/commands/sp.analyze.md: ⚠ pending
- .specify/templates/commands/sp.adr.md: ⚠ pending
Follow-up TODOs: None
-->

## Core Principles

### I. Automated Content Generation
All book content MUST be primarily generated and managed using Claude Code and Spec-Kit Plus,
aiming for a hands-off, fully automated content creation and update process.

### II. Docusaurus-First Design
The book will leverage Docusaurus for its framework, incorporating features such as
search functionality, versioned documentation, a blog section, and customizable theming/styling
to ensure a rich and interactive user experience.

### III. Test-First (NON-NEGOTIABLE)
TDD is mandatory: Tests MUST be written and approved before implementation;
Red-Green-Refactor cycle MUST be strictly enforced for all code development.

### IV. Hierarchical Content Structure
The book's content MUST be organized in a clear, hierarchical (nested categories)
structure to facilitate easy navigation and understanding of complex topics.

### V. Observability & Maintainability
All components, including the book generation process and the RAG chatbot,
MUST incorporate structured logging and monitoring to ensure debuggability,
performance tracking, and long-term maintainability.

### VI. Versioning & Deployability
The book content and its associated codebase MUST support versioning for consistent updates.
Deployment to GitHub Pages MUST be automated and reliable.

### VII. Integrated RAG Chatbot
The book MUST include an embedded RAG chatbot powered by OpenAI Agents/ChatKit SDKs, FastAPI,
Neon Serverless Postgres, and Qdrant Cloud Free Tier, capable of answering questions about the book content,
including selected text.

### VIII. Reusable Intelligence (Bonus)
The project will actively pursue the creation and utilization of reusable intelligence
via Claude Code Subagents and Agent Skills for bonus points and enhanced functionality.

## Additional Constraints

Technology stack requirements: Docusaurus, Node.js, TypeScript for book generation.
RAG chatbot specific technologies: OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres, Qdrant Cloud Free Tier.
Compliance standards: Adhere to GitHub Pages deployment policies.
Point System: Base functionality (book + chatbot) is worth 100 points;
reusable intelligence (Subagents/Agent Skills) is worth up to 50 bonus points.

## Development Workflow

Code review requirements: All code and significant content changes MUST be reviewed by a human.
Testing gates: All automated tests (unit, integration, E2E where applicable) MUST pass before deployment.
Deployment approval process: Automated deployment to GitHub Pages upon successful build and test.

## Governance
This Constitution supersedes all other project practices; Amendments MUST be documented,
approved, and include a migration plan. All PRs/reviews MUST verify compliance;
Complexity MUST be justified; Use the SpecKit Plus documentation for runtime development guidance.

**Version**: 1.1.0 | **Ratified**: 2025-12-01 | **Last Amended**: 2025-12-01<!-- Example: Version: 2.1.1 | Ratified: 2025-06-13 | Last Amended: 2025-07-16 -->
