# **✅ Session 07: Implement [Agentic Design Patterns](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code/tree/main/06_agentic_design_patterns) with OpenAI AgentKit Agent Builder | AI-100 (05/11/2025)**

**The 4 Core Agentic Patterns We'll Learn**
1. **Reflection Pattern** - Agent reviews its own work
2. **Tool Use Pattern** - Agent decides which tools to use
3. **Planning Pattern** - Agent breaks down complex tasks
4. **Multi-Agent Pattern** - Agents collaborate via handoffs

## 1. Agentic Design Pattern #1 - Reflection

**What is Reflection?**
Reflection is when an agent generates a response, then reviews it, and improves it if needed. It's like having a quality control step built into your agent.

**The Process:**
* Agent drafts a response
* Agent reviews the response: "Is this accurate? Complete? Polite?"
* If good → Send to user
* If needs work → Agent improves it

Example Use Case: **Essay Generator**

**Output Parsed**
When we click on Edge between reflection schema and if/else block, it will show source output schema in which we have output parsed, output parsed appeared or occurred when we set/attached output schema with our agent

---
![Output Parsed](../assets/Ses07_Edge_OutputParsed.png)

---

![Reflection Pattern](../assets/Ses07_ReflectionPattern.png)

---

## 2.  Agentic Design Pattern #2 - Tool Use
**What is Tool Use?**
**Tool Use** is when an agent intelligently decides which tools to use based on the user's needs. Instead of hardcoding which tool to use, the agent makes smart choices.

**The Process:**

1. User asks a question
2. Agent analyzes: "What do I need to answer this?"
3. Agent chooses appropriate tools
4. Agent uses tools to gather information
5. Agent synthesizes the results

Example Use Case: **Personal Assistant**

## 3. Agentic Design Pattern #3 - Planning

**What is Planning?**
Planning is when one agent creates a strategic plan by breaking down a complex task into actionable steps, and another agent executes that plan systematically. This pattern separates strategic thinking from execution.

**The Process:**

1. Planner agent receives complex request
2. Planner agent analyzes the task and creates a structured plan with clear steps
3. Executor agent receives the plan
4. Executor agent follows each step systematically
5. Final output reflects completion of all planned steps

Example Use Case: **Research Report Generator**

