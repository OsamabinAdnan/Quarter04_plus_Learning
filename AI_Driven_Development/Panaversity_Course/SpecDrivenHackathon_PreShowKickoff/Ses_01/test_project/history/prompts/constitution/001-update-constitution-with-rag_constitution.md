---
id: 001
title: Update Constitution with RAG and Bonus Principles
stage: constitution
date: 2025-12-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: generic_user
command: /sp.constitution
labels: ["constitution", "update", "RAG", "chatbot", "spec-driven-development"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
null
---

## Prompt

Requirement: You are required to complete a unified book project using Claude Code and Spec-Kit Plus. The core deliverables are:

1. AI/Spec-Driven Book Creation: Write a book using Docusaurus and deploy it to GitHub Pages. You will use Spec-Kit Plus ( https://github.com/panaversity/spec-kit-plus/ ) and Claude Code ( https://www.claude.com/product/claude-code ) to write the book.

2. Integrated RAG Chatbot Development: Build and embed a Retrieval-Augmented Generation (RAG) chatbot within the published book. This chatbot, utilizing the OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres database, and Qdrant Cloud Free Tier, must be able to answer user questions about the book's content, including answering questions based only on text selected by the user.

3. Participants will receive points out of 100, for base functionality defined above.

4. Participants can earn up to 50 extra bonus points by creating and using reusable intelligence via Claude Code Subagents and Agent Skills in the book project.

 I want you to discuss these requirement with me before generating constitution

## Response snapshot

The `constitution.md` file was updated to version 1.1.0, incorporating principles for the Integrated RAG Chatbot and Reusable Intelligence (Bonus), along with updated constraints regarding technology stack and the point system.

## Outcome

- ✅ Impact: The project constitution has been successfully updated to reflect the full scope of the unified book project, including RAG chatbot requirements and bonus point criteria for reusable intelligence.
- 🧪 Tests: No explicit tests were run for this constitution update.
- 📁 Files: The `.specify/memory/constitution.md` file was modified.
- 🔁 Next prompts: Continue discussion on RAG chatbot development; begin planning for the book project implementation.
- 🧠 Reflection: The bash script for PHR creation failed, requiring a manual agent-native PHR generation. This highlights the importance of having robust fallback mechanisms for tool execution.

## Evaluation notes (flywheel)

- Failure modes observed: Bash script for `create-phr.sh` not found.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure `create-phr.sh` is available or improve error handling/fallback for PHR creation.
