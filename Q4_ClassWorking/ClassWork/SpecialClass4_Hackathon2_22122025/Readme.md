# Hackathon 2: The Evolution of TODO - 22nd December 2025 (Sir Ameen Alam)

We have to make a console based todo app in hackathon 2.

1. **Phase: 1 (CLI based)**

- First, we have to make a console based todo app covering all `Basic level` (Core Essentials).
- Then sumbit that project
- Then we have to upgrate that project to `Intermediate level`  (Organization & Usability) and `Advanced level` (Intelligent Features). Details are mentioned in [Hackathon 2 file, page 2](Hackathon%20II%20-%20Todo%20Spec-Driven%20Development.pdf)

2. **Phase: 2 (Full Stack based)**
- 3 tiers application
    - Client Tier (frontend) + Application tier (backend or API or Business layer) + Database tier (where data is stored)
    - *For client side:* We will use Next.js
    - *For backend/application tier:* We will use FastAPI 
        - Actually frontend calling function on backend, on that function we will use decorators of FastAPI and for calling function frontend use http protocol, backend expose it function on http.
        - Using http protocol, there is a REST protocol, while using that REST protocol, we are calling function on backend
        - REST API protocol is stateless (function in this case), developer make it stateful (suppose by storing variable in variable).
        - To make it stateful, we use `Sockets`, `event streaming` which are updated version to make it stateful. Like for WA chats we need **sockets**, it will not work only using REST API. For MCP servers we need **event streaming** aka `server send events (SSE)`
        - **SQL Model:** Use for user's input validation. Process is called `Validation or Sanitization`. FastAPI will talk to SQL Model and SQL Model will talk to database.
        - In the presence of SQL Model, we dont call Postgres directly from FastAPI, SQL Model will call Postgres (Neon DB). SQL Model are python classes.
    - *For database:* We will use Neon DB
- For Phase 2, you should make skills and subagents using Claude CLI, below are few github links for ready made agents:
    1. [Oxfurai](https://github.com/0xfurai/claude-code-subagents)
    2. [Panaversity Skills](https://github.com/panaversity/claude-code-skills-lab)
- For skills, you can clone this anthropic repo [Anthropic Skills](https://github.com/anthropics/skills), go to skills folder after cloning where you will find skill called `skill-creator`, copy paste this file in .claude global file, make folder by the name skills and copy paste this file in that folder. Then write prompt that using skill-creator skill write prompt for [your topic].
- Then when you make subagent, you will add relevant skills which subagent will use within YAML tag.
- After making agents and skills, review them multiple times



