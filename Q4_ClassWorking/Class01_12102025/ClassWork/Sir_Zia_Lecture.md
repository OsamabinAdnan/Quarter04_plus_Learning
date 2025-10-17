# **Agents**

- LLMs are the brain of agents
- `Actions` agents take on our behave is called `Function/Tool calling` in **Agentic AI**
- Function calling has standard which is called `MCPs (Model Context Protocols)`
- We wrap APIs on MCP, so LLMs understand it better

- Our goal is used coding agents which write/make other agents
    - We give command to make agents, coding agent will make it and deploy it

Todays topic is [**`Seven Pillars of Agent Driven Development`**](https://github.com/panaversity/spec-kit-plus/blob/main/docs-plus/readme.md#the-seven-pillars-framework)

## **Seven Pillars of Agent Driven Development**

This documentation presents The Seven Pillars of AI-Driven Development—a comprehensive methodology that synthesizes the best practices emerging from the AI coding revolution. These seven pillars form an integrated system where each component reinforces the others:

---

### **Pillar 1: Markdown as Programming Language:**
- Right now, three formats are standard: XML, Markdown and JSON
- But easiest format is `Markdown`
- Standard way of input is `Markdown` and output will be voice, folder or any other way

---

### **Pillar 2: Linux-Based Development Environment:**
- We have to do development on `WSL (Windows Subsystem for Linux)`
- `WSL (Windows Subsystem for Linux)` is a compatibility layer developed by Microsoft that allows users to run Linux binaries natively on Windows, without needing a virtual machine or dual-boot setup.
    * **First Introduced:** Announced in 2016 with Windows 10.
    * **Purpose:** To provide developers with a Linux-like environment directly within Windows, mainly for web development, DevOps, and open-source tools.
    * **Proposed/Developed by:** Microsoft, in collaboration with Canonical (the company behind `Ubuntu`) for initial Linux distribution support.
    * **Versions:**
        - **WSL 1 (2016):** Used a translation layer to convert Linux system calls into Windows kernel calls.
        - **WSL 2 (2019):** Introduced a real Linux kernel running inside a lightweight virtual machine, improving performance and compatibility.
    * **Current Status:** Continues to evolve, with WSLg adding GUI app support and WSL available via the Microsoft Store for easier installation.

- In short, WSL bridges Windows and Linux, enabling developers to use Linux tools seamlessly inside Windows.

---

### **Pillar 3: AI CLI Agents**
- The way you talk to Linus via WSL, that is command line interface (CLI) which is called `Bash` in Linux which talk which you OS
- You have install GitHub CLI, check this Repo for more detail [Spec-Kit/Docs-Plus](https://github.com/panaversity/spec-kit-plus/tree/main/docs-plus)

- Our strategy provides developers with a choice of the three dominant, competing AI CLI platforms:

* `Google Gemini CLI or Qwen:` Known for its radical openness and fast-growing extension ecosystem.
* `OpenAI Codex:` Focused on SDK-first enterprise integration and powerful cloud-based execution.
* `Anthropic Claude Code:` Emphasizes safety, reliability, and curated marketplaces.

![AI Coding Tools](assets/AI%20Coding%20Tools.jpg)

We give command to AI CLI (as a prompt in markdown) ==> that command will go to LLMs ==> and LLMs control CLI, CLI means here your whole system like (Git, GitHub, Cloud, Docker, DockerHub etc.) ==> and give you end result that task has been completed.

---

### **Pillar 4: Model Context Protocol (MCP) for Extensibility**

- Standardized protocol for connecting AI agents to tools, data sources, and enterprise systems, enabling composable agent ecosystems.
- AI Coding agents must interact with external tools and data to perform meaningful work. The **Model Context Protocol (MCP) has emerged as the universal standard—the "USB-C for AI"—for connecting agents to any data source or tool.**
- `MCP wraps APIs and provide function-based communication`
- MCP is third party application who made it own MCP server, by using AI CLI we initiate our requests to MCP server and can create repositories there and commit as well.
- MCP is better than https because of the advancement of tech.
- MCP has quality, it can attach with CLI (AI CLI in this case) and LLMs based app (like ChatGPT UI)

Now we have to do development in small iterations not in wipe coding **(wipe coding = `deleting everything and rewriting`)**, you write small code and execute.

---

### **Pillar 5: Test-Driven Development (TDD)**

- Even though we are writing and running small pieces of code, the process should follow **Test-Driven Development (TDD)**. This means that tests must be written along with the code.
- Before making any changes, another developer should run all existing tests provided with the code.
- If all tests pass, it means the code is working correctly `(“green light”)`.
- When a developer adds new code, they must run both their own tests and the previous developer’s tests to make sure everything still works properly.
- `TDD` approach said, you have to write test first before making actual code and that is called `red light`.
- Speed without quality is technical debt. TDD is the essential discipline that validates the output of our AI agents, ensuring correctness and reliability.

---

### **Pillar 6: Spec-Driven Development (SDD)**

- Specification Driven Development
- Write down all specs of it, like What work do you want to get done? otherwise AI make assuming for it
- We will divide our work into multiple specs, which will create the AI App.

---

### **Pillar 7: Cloud-Native Deployment**

- The ultimate goal is to deploy scalable, resilient, and distributed AI systems. Our chosen stack is composed of battle-tested, cloud-native technologies designed for modern applications.
- According to sir we have found that we can deploy on any cloud
    * `Containerization:` **Docker** for packaging agents and services into portable containers.
    * `Orchestration:` **Kubernetes** for managing and scaling our containerized agent fleets.
    * `Distributed Application Runtime:` **Dapr** simplifies building resilient, stateful, and event-driven distributed systems. Its Actor Model is particularly powerful for implementing stateful agents.
    * `Distributed Compute:` **Ray** for parallel agent execution and scaling compute-intensive AI workloads.

```bash
┌─────────────────────────────────────────────────────────────────┐
│              AI-Driven Development (AIDD) Workflow             │
└─────────────────────────────────────────────────────────────────┘

PHASE 1: SPECIFICATION (Pillars 1, 6)
   │
   ├─→ Write system requirements in spec.md (Markdown)
   ├─→ Define agent behaviors and protocols using SDD+ templates
   ├─→ Define org standards in constitution.md
   └─→ Version control all specs with Git (Pillar 2)
   │
   ▼
PHASE 2: IMPLEMENTATION (Pillars 3, 4, 5)
   │
   ├─→ Use an AI CLI (Gemini, Codex, Claude) to interpret specs
   ├─→ Coding Agent writes tests first (TDD) to match acceptance criteria
   ├─→ Coding Agent generates implementation code to pass tests
   └─→ Coding Agent interacts with envirnoment via MCP plugins
   │
   ▼
PHASE 3: INTEGRATION & VALIDATION (Pillar 2)
   │
   ├─→ CI pipeline on GitHub Actions is triggered
   ├─→ Lints specs, runs all tests, checks for spec alignment
   ├─→ Human developer reviews the pull request (spec + code)
   └─→ "No green, no merge" policy enforced
   │
   ▼
PHASE 4: DEPLOYMENT & ORCHESTRATION (Pillar 7)
   │
   ├─→ Build Docker containers for agents and services
   ├─→ Deploy to a Kubernetes cluster
   ├─→ Manage state and communication with Dapr
   └─→ Scale compute tasks with Ray
```
---

### CI/CD (Continuous Integration/Continuous Deployment)
CI/CD is an automated pipeline that tests, builds, and deploys software — making development faster, safer, and more reliable.

#### **Continuous Integration (CI):**
- Developers regularly add (or “integrate”) their code into a shared project.
- Each time code is added, an automated system `builds the project` and `runs tests` to check that nothing is broken.
    * Think of it as `automatic testing every time someone adds new code.`

#### **Continuous Deployment/Delivery (CD):**
- Once the code passes all tests, it can be automatically released (deployed) to a server or application for users.
    * Think of it as `automatic publishing of working code to production.`