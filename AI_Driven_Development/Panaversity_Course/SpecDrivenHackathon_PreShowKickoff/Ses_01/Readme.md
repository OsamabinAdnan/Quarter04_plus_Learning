# Session-01 | AI-Driven • Spec-Driven Hackathon — Pre-Show Kickoff

In this era of AI, we have 3 pillars:

1. **AI Driven Development using Spec Driven Development**
    * Tool are:
        - Claude code mainly, could be GEMINI CLI, GPT 5.1 Codex
2. **AI Native Development**
    * Tools are:
        - OpenAI SDK and MCP Servers
3. **AI Ops (Operations) i.e.,**
    * Deployment of Agent into Kubernetes and Cloud Native technologies
    * How to make Event Driven applications using Kafka
    * How to integrate these all.
    * Tools are:
        - Kubernetes
        - Kafka
        - DAPR and Docker
* There is another pillar along with mentioned above one, how to grab business/work

**Rule decided to write `AI Native Development` Book from `Panaversity`**

1. Maximum author contribution was 5%, 95% work had been done by agent
2. Content should have been equal or better than simple writer content quality
3. Tooling locked so we will not go beyond it
4. We checked and learned about how book has written and author's mindset behind it, we broken down it and identify some components, like writter has these skills to write book plus these are the mode and aura which he use to write a book, which we translate in our **reusable intelligence**.
5. We set up skills of our AI companions and partners
6. Identify groups of `sub agents`, in order to work in group, each agent has particular task

**Code Analysis**
- Constitution file present in `.spec/memory/constitution.md`
- When request forward to LLM, constitution file is not send to it, LLM already knows about it
- `Claude.md` or `Gemini.md` (Depend on which LLM you are using) file has been sent to LLM, constitution referred in these files so LLM will check constitution by default. This 

## Requirement

### Step 01:
AI/Spec-Driven Book Creation: Write a book using Docusaurus and deploy it to GitHub Pages. You will use [Spec-Kit Plus](https://github.com/panaversity/spec-kit-plus/) and [Claude Code](https://www.claude.com/product/claude-code) to write the book. 

#### How to make constitution of project?
- Go to project file
- Copy incomplete requirements and course details
- Go to claude and discuss with those requirement, ask him to write prompt about it to write constitution
- After discussion, ask him to generate constitution on the basis of detail, we have to generate book using `Docusaurus`

##### Docusaurus
- Docusaurus is a framework of `Facebook` to generate documents/books
- It allows you to add react components
- We have to make interactive AI book in order to add react components
- We need to ask CLI to read docusaurus document in order to implement it.
- **Make empty/empty shell/skeleton repository for docusaurus**
    - **`then run chap1, chap2 and prefix etc. Write one chapter at a time`**
- Dont do `Vibe Coding`
- You tell about Docusaurus in constitution then in specify, in plan, in tasks then implement
- Then you make first chapter in specify

##### Hackathon (Course Detail)
- Course detail respect to writing book will be mentioned in Hackathon document.
- Save that document in markdown file in our project folder.
- We have to `say/write in constitution` that I want to write a book to teach this course.
- At least write three chapters

Read Chap # 05 of Panaversity AI Native for Claude Code
And Chap # 14 of Panaversity AI Native for Spec-Kit Plus

### Step 02:
Integrated RAG Chatbot Development: Build and embed a Retrieval-Augmented Generation (RAG) chatbot within the published book. This chatbot, utilizing the OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres database, and Qdrant Cloud Free Tier, must be able to answer user questions about the book's content, including answering questions based only on text selected by the user.

**Chat Agent Concept**
- We are building a chat agent that will live on the website.
- When a user clicks the chat icon, a popup opens.
- The agent knows:
    * Which lesson the user is currently viewing.
    * What the user is asking about that lesson.

**How the System Works**
- User sends a question → request goes from client-side to the ChatKit server.
- Behind ChatKit, an agent processes the query.
- The agent knows the user is asking something related to the book/lesson.
- But the agent cannot search the book unless we implement tools for it.

**Why RAG Is Needed**
- To enable the agent to look inside the book, lessons, or chapters.
- We implement Agentic RAG using:
    * **A vector database**
    * Vectors generated from the entire book stored in this database.
- At runtime:
    * User question → agent searches relevant chapters/sections.
    * Finds context → sends it to the LLM.
    * LLM generates an answer based on book context.

**Why Not Put Entire Book in LLM Context**
* Book has many parts (e.g., 34 chapters).
* User may be in Part 1 but ask about something in Part 5.
* Entire book cannot be loaded into prompt context → not possible.
* Therefore RAG + vector DB solves this.

**Final System Flow**
1. RAG retrieves context from vector DB.
2. LLM generates answer using that context.
3. Chatbot displays the final answer.

**Project Requirements**
- These two steps complete the core project.
- Additional tasks are given for advanced learners.
- Extra days were added so beginners also get a fair chance.

**Submission Details**
- Deploy your project (e.g., on Vercel or GitHub Pages).
- Submit:
    * Your repository URL
    * Deployment link
    * A demo video

**Demo Video Requirements**
- Reviewers cannot open every repo and read all code.
- So they begin evaluation with your demo video.
- You must create a 90-second demo video showing:
    * How your chatbot works
    * Key features
    * RAG functionality (if implemented)

**`Points to be noted`**
How to start:
- Read Chap 5 and 14 of book in order to know sub-agents, skills of Claude code and spec-kit plus
- Setup project
    * first setup docusaurus
    * then generate constitution, copy detail from given hackathon file to do so.
    * then start working on your chapters one by one, go with planning
- Deploy on github pages, it will give to action, you push it will deploy
- Then come part 2
    * Discuss with agent that how we can make these things/stuffs, treat it as your companion and learn with him
    * Then you come in collabration phase, things about implement simple agent and how i do it
    * Then start your work on part 2


