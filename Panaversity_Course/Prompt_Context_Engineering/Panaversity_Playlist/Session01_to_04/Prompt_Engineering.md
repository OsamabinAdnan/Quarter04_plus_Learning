# **Prompt and Context Engineering**

## **Class 01: Prompt and Context Engineering Introduction**

- **Prompt engineering:** craft the exact instruction (the prompt) you give an LLM so it returns the output you want.
- **Context engineering:** design and manage the surrounding information (examples, system messages, memory, tool outputs, documents) that the model uses when it runs.

---
![Stats](assets/stats.jpg "Annual Global Web Visits from Aug 2024 to July 2025")

---
* **Key Takeaways**
    - With 46.59B visits, ChatGPT accounts for more than 83% of total traffic among the top 10 chatbots.
    - The second most-used chatbot, DeepSeek at 2.74B visits, has barely 6% of ChatGPT’s traffic.
    - While traffic is concentrated, the list includes a mix of U.S., Chinese, and European players.

* When we are doing prompt engineering, we will try our prompt on 4 places
    - ChatGPT (To make report after search from web, Sir use it)
    - Gemini (context window is short in free tier)
    - Claude (expensive but best, Sir Zia used it for coding, tutorial)
    - Grok (Sir used Grok for authenticate and creditable infor)

### **Which is the best LLM?**
See how leading models stack up across text, image, vision, and beyond. This page gives you a snapshot of each Arena:
[Imarena](https://lmarena.ai/leaderboard)

### **Understand the Power of Prompts: Context Engineering for Agentic AI Developers, Image and Video Generation, UX/UI Design and UI Development**

To understand the power of LLMs and prompt engineering go through these tutorials:

* **[Complete Guide to Context Engineering for AI Agents](https://github.com/panaversity/learn-n8n-agentic-ai/blob/main/00_prompt_engineering/context_engineering_tutorial.md)**
* **[Nano Banana Tutorial](https://github.com/panaversity/learn-low-code-agentic-ai/blob/main/00_prompt_engineering/image_generation/readme.md)**
* **[Google's Veo 3: A Guide With Practical Examples](https://github.com/panaversity/learn-low-code-agentic-ai/blob/main/00_prompt_engineering/video_generation/readme.md)**
* **[UX Design by Prompting](https://github.com/panaversity/learn-low-code-agentic-ai/tree/main/00_prompt_engineering/ux_design)**
* **[UI Development by Prompting](https://github.com/panaversity/learn-low-code-agentic-ai/tree/main/00_prompt_engineering/ui_development)**

* **[Google's Veo 3: Official Website](https://labs.google/flow/about)**, sign in to proceed
* **[Text to UI/UX design](https://uxpilot.ai)**, sign in to proceed
* **[Text to Frontend](https://lovable.dev)**, sign in to proceed

- In Prompt engineering, you need to upgrade your English writting skills because prompt engineering is a iterative process.

### **Use these Prompt Engineering Tools to Learn (Playgrounds)**
* https://platform.openai.com/chat/ (ChatGPT, https://chat.com is another URL)
* https://aistudio.google.com/ (Gemini)
* https://console.anthropic.com/ (Claude)

### **Prompt Coach**
Here’s a reusable “Prompt Coach” prompt you can keep handy. You’ll paste this into ChatGPT (or any LLM), then just drop in your messy idea, and it will rewrite it into a polished, effective prompt for you:

Copy Paste this in your LLM:
```bash
You are my Prompt Coach. I will give you a rough or unclear prompt. 
Your task is to:
1. Clarify it
2. Add missing context
3. Structure it for best results
4. Suggest 2–3 alternative versions (different styles: simple, detailed, structured)

Here’s my rough prompt: [INSERT YOUR PROMPT HERE]
```
### **1. What is Prompt Engineering?**
Prompt engineering is the art and science of crafting instructions that guide AI language models to produce desired outputs. Think of it as learning to communicate effectively with AI systems to achieve specific goals.

**Why is it important?**

* You don't need to be a programmer to use AI effectively
* Good prompts can dramatically improve AI performance
* It's an iterative skill that improves with practice
* It's becoming essential for productivity in many fields

#### **Prompt engineering vs. context engineering**
- **Prompt engineering** = crafting the *instruction* you give the model.
- **Context engineering** = curating the *information* the model can see when following that instruction.

#### **Quick contrast**

| Aspect          | Prompt engineering                                                       | Context engineering                                                                      |
| --------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Goal            | Tell the model *how* to behave and *what* to produce                     | Give the model the *facts/examples* it should rely on                                    |
| Levers          | Wording, structure, roles, constraints, output schema, few-shot examples | Retrieval (RAG), documents, knowledge bases, tools/APIs, memory, state across turns      |
| Typical changes | “Be concise. Return valid JSON with fields X/Y/Z.”                       | “Attach the company glossary, latest policy PDF, and retrieved passages for this query.” |
| Failure mode    | Vague instructions → messy/incorrect format                              | Missing/irrelevant info → hallucinations/outdated answers                                |
| Ownership       | UX/prompt designers, app devs                                            | Data/ML/platform teams (pipelines, indexing, chunking, evals)                            |

#### **How they work together**

* Start with a **good prompt**: clear task, constraints, and an **output contract** (e.g., JSON schema).
* Then **ground it with context**: supply only the *most relevant* passages, tables, and tool results.
* The prompt guides *behavior*; the context supplies *knowledge*. You usually need both.

#### **Concrete examples**

1. **Invoice → JSON extractor**

* *Prompt engineering*: “Extract fields {vendor, date, total}. Return JSON only. If a field is missing, use null.”
* *Context engineering*: Provide a few labeled examples and attach the vendor’s invoice spec retrieved via embeddings.

2. **Policy Q\&A bot**

* *Prompt engineering*: “Answer using the attached passages; if unsure, say ‘Not in policy.’ Cite section IDs.”
* *Context engineering*: RAG over your policy repo (chunking, metadata filters like `department=HR`, freshness boosts), plus a recency cache for updates.

3. **Agentic workflow**

* *Prompt engineering*: Tool-use instructions and function signatures.
* *Context engineering*: Feed tool responses (DB rows, API payloads) back into the context window each step; maintain short-term memory/state.

#### **Practical tips**

* Keep prompts **short, specific, and testable**; define output schemas.
* Prefer **few-shot** examples only when they generalize; otherwise move them into **retrieval**.
* For context: optimize **chunking**, **ranking**, **deduping**, and **token budgets**; log what was retrieved for each answer.
* Add **citations** and “answer only from context” instructions when correctness matters.
* Evaluate both layers separately: prompt A/B tests and retrieval quality (precision/recall, groundedness).

**One-liner:** Prompt engineering is *how you ask*; context engineering is *what you show*. Combine them for reliable, scalable LLM apps.

### **2. Understanding Large Language Models**

#### How LLMs Work (The Basics)

Large Language Models are prediction engines that:
- Take text input (your prompt)
- Predict the next most likely word/token
- Continue this process to generate complete responses
- Base predictions on patterns learned from training data

#### Key Concept: Autocompletion
LLMs don't "understand" in the human sense—they're sophisticated autocomplete systems. Your prompt sets up the context for what should come next.

### **3. Essential Configuration Settings**

Before diving into prompt techniques, understand these key parameters that control AI behavior:

#### Temperature (0-1)
- **Low (0-0.3)**: Focused, consistent, deterministic responses
- **Medium (0.4-0.7)**: Balanced creativity and consistency
- **High (0.8-1.0)**: Creative, diverse, but potentially unpredictable

**When to use:**
- Temperature 0: Math problems, factual questions
- Temperature 0.7: Creative writing, brainstorming
- Temperature 0.9: Poetry, experimental content

#### Output Length/Token Limits
- Controls maximum response length
- Higher limits = more computational cost
- Set appropriately for your task needs

#### Top-K and Top-P (Nucleus Sampling)
- **Top-K**: Limits choices to top K most likely tokens
- **Top-P**: Limits choices based on cumulative probability
- Work together with temperature to control randomness

**Recommended starting points:**
- Conservative: Temperature 0.1, Top-P 0.9, Top-K 20
- Balanced: Temperature 0.2, Top-P 0.95, Top-K 30
- Creative: Temperature 0.9, Top-P 0.99, Top-K 40

## **Class 02: Prompt and Context Engineering Introduction (Cont.)**

`Action` => connect with `MCP Server` => `Multi Models` => `Text + Images + Videos`

### **4. Fundamental Prompting Techniques**

#### 1. Zero-Shot Prompting

The simplest approach—just ask directly without examples.

**Example:**
```
Classify this movie review as positive, negative, or neutral:
"The film was visually stunning but the plot felt rushed."
```

**When to use:**
- Simple, well-defined tasks
- When the model has clear knowledge of the domain
- Quick one-off requests

#### 2. One-Shot Prompting

Provide a single example to guide the response format.

**Example:**
```
Translate English to French:

English: "Hello, how are you?"
French: "Bonjour, comment allez-vous?"

English: "Where is the library?"
French:
```

#### 3. Few-Shot Prompting

Provide multiple examples to establish a clear pattern.

**Example:**
```
Convert customer feedback to structured data:

Feedback: "Great service, but food was cold"
JSON: {"service": "positive", "food": "negative", "overall": "mixed"}

Feedback: "Amazing experience, will definitely return"
JSON: {"service": "positive", "food": "positive", "overall": "positive"}

Feedback: "Terrible food and rude staff"
JSON:
```

**Best practices:**
- Use 3-5 examples for most tasks
- Include diverse examples
- Mix up the classes in classification tasks
- Ensure examples are high-quality and consistent

#### 4. System Prompting

Set overall context and behavior guidelines.

**Example:**
```
You are a helpful travel guide. Provide practical, accurate information about destinations. Always include:
- Key attractions
- Local customs to be aware of
- Budget considerations
- Best time to visit

User: Tell me about visiting Tokyo.
```

#### 5. Role Prompting

Assign a specific character or expertise to the AI.

**Example:**
```
Act as an experienced software architect. I need help designing a scalable web application for 1 million users. What architecture patterns should I consider?
```

**Effective roles:**
- Subject matter expert (doctor, lawyer, teacher)
- Creative roles (writer, designer, poet)
- Analytical roles (data analyst, consultant)
- Communication styles (friendly tutor, formal advisor)

#### 6. Contextual Prompting

Provide specific background information relevant to the task.

**Example:**
```
Context: You're writing for a tech blog aimed at beginners who have never coded before.

Write a 200-word explanation of what an API is, using simple language and practical examples.
```

### **5. Advanced Prompting Strategies**

#### 1. Chain of Thought (CoT) Prompting

Encourage step-by-step reasoning for complex problems.

**Example:**
```
Solve this step by step:
If I was 6 when my sister was half my age, how old is my sister when I'm 40?

Let me think through this step by step:
```

**When to use:**
- Math problems
- Logical reasoning
- Complex analysis
- Multi-step processes

**Best practices:**
- Use "Let's think step by step" or similar phrases
- Set temperature to 0 for consistent reasoning
- Extract final answers separately from reasoning

#### 2. Self-Consistency

Generate multiple reasoning paths and select the most common answer.

**Process:**
1. Ask the same question multiple times with different phrasings
2. Compare the answers
3. Choose the most frequently occurring result

**Example:**
```
Question: If a store offers a 20% discount on a $50 item, what is the final price?

Generate 3 different reasoning paths for this question and select the most consistent answer.

Path 1: To find the final price, calculate the discount: 20% of $50 is 0.20 × 50 = $10. Subtract this from the original price: $50 - $10 = $40. The final price is $40.

Path 2: A 20% discount means paying 80% of the original price. So, 80% of $50 is 0.80 × 50 = $40. Therefore, the final price is $40.

Path 3: Compute the discount amount: 20% = 0.20, so 0.20 × $50 = $10 off. The original price is $50, so after the discount, it’s $50 - $10 = $40. The final price is $40.

Most common answer: $40
```

**Explanation of Concept:**
Self-Consistency involves generating multiple answers to the same question using varied reasoning approaches to ensure reliability. By comparing the results, you select the most frequent or consistent outcome, reducing the chance of errors from a single flawed reasoning path. This method leverages the model's ability to approach the problem from different angles, increasing confidence in the final answer when all paths converge, as seen here with the consistent result of $40.

#### 3. Step-Back Prompting

Ask a more general question first, then use that context for the specific question.

**Example 1:**
```
First, what are the key principles of good user interface design?

[Get response]

Now, using those principles, redesign this mobile app's login screen: [description]
```

**Example 2:**
Question: How should I optimize the loading speed of my e-commerce website?
```
Step 1: First, what are the key factors that generally affect website loading speed?

Response: Key factors include:
- Server response time (hosting quality, server location)
- Image and asset optimization (file size, compression)
- Code efficiency (minifying CSS/JavaScript, reducing HTTP requests)
- Caching strategies (browser caching, CDNs)
- Third-party scripts (ads, analytics)

Step 2: Using these factors, provide specific recommendations to optimize the loading speed of an e-commerce website with heavy product images and multiple third-party plugins.

Response:
1. **Server Optimization**: Choose a reliable hosting provider with servers close to your audience. Enable server-side caching (e.g., Redis or Varnish).
2. **Image Optimization**: Compress product images using formats like WebP. Implement lazy loading to defer off-screen images.
3. **Code Efficiency**: Minify CSS and JavaScript files. Combine small files to reduce HTTP requests.
4. **Caching**: Use a Content Delivery Network (CDN) like Cloudflare to cache static content globally. Set browser cache headers for repeat visitors.
5. **Third-Party Plugins**: Audit and remove unnecessary plugins. Asynchronously load scripts for analytics or ads to avoid blocking page rendering.

```

**Explanation of Concept:**
Step-Back Prompting involves first asking a broader, foundational question to establish key principles or context before tackling the specific task. This approach ensures the model grounds its response in general knowledge (e.g., factors affecting website speed) before applying it to the specific problem (e-commerce site optimization). By breaking the task into two steps, the model produces more informed and structured recommendations, reducing the risk of overlooking critical factors.


#### 4. ReAct (Reasoning + Acting)

Combine reasoning with tool use or actions.

**Example 1:**
```
I need to find out how many children the members of Metallica have in total.

Thought: I need to find information about each band member and their children.
Action: Search for "Metallica band members"
Observation: [results]
Thought: Now I need to search for each member individually...
```

**Example 2:**
```
Question: What is the current population of Tokyo, and how does it compare to New York City?

Thought: I need to find the current population of Tokyo and New York City to compare them. I should start by searching for the latest population data for Tokyo.

Action: web_search
<parameter name="query">current population of Tokyo 2025</parameter

Observation: [Assume tool response: According to recent estimates, Tokyo's population in 2025 is approximately 37.4 million in the metropolitan area.]

Thought: Now I have Tokyo's population. Next, I need the population for New York City.

Action: web_search
<parameter name="query">current population of New York City 2025</parameter

Observation: [Assume tool response: New York City's metropolitan area population in 2025 is estimated at about 23.6 million.]

Thought: With both figures, I can compare them. Tokyo has a larger population than New York City by about 13.8 million people.

Final Answer: Tokyo's population is approximately 37.4 million, compared to New York City's 23.6 million, making Tokyo significantly larger.

```

**Explanation of Concept:**
ReAct (Reasoning + Acting) is a prompting strategy that interleaves reasoning steps (Thoughts) with actions (tool calls or external queries) to solve complex problems iteratively. Each cycle includes a Thought (planning the next step), an Action (executing a tool or search), and an Observation (processing the result). This loop continues until the question is resolved, allowing the model to dynamically gather information and refine its approach. It's particularly useful for tasks requiring real-time data or multi-step verification, as demonstrated by sequentially fetching and comparing population data.

#### 5. Tree of Thoughts (ToT)

Explore multiple reasoning branches simultaneously for complex problems.

**When to use:**
- Creative problem solving
- Strategic planning
- Complex decision-making
- Tasks requiring exploration of alternatives


**Example:**

Question: What is the best marketing strategy for launching a new eco-friendly clothing brand targeting young adults?

Task: Explore multiple strategic approaches, evaluate them, and select the best one.

**Branch 1: Social Media Campaign**
Thought: Young adults are active on platforms like Instagram and TikTok. A campaign using influencers could build brand awareness.
Exploration:
- Pros: High engagement, visually appealing for clothing, cost-effective with micro-influencers.
- Cons: Risk of inauthentic partnerships, oversaturation in influencer marketing.
Evaluation: Strong for visibility but needs unique content to stand out. Score: 8/10.

**Branch 2: Sustainable Pop-Up Events**
Thought: Hosting pop-up shops at eco-conscious festivals or college campuses could create direct engagement.
Exploration:
- Pros: Hands-on experience with products, builds community, aligns with eco-friendly values.
- Cons: High logistical costs, limited geographic reach.
Evaluation: Great for brand authenticity but resource-intensive. Score: 7/10.

**Branch 3: Collaborative Partnerships**
Thought: Partnering with eco-friendly brands (e.g., sustainable accessories) could cross-promote to aligned audiences.
Exploration:
- Pros: Expands reach via partner networks, reinforces eco-mission.
- Cons: Complex coordination, potential brand dilution.
Evaluation: Effective for niche targeting but requires careful partner selection. Score: 7.5/10.

**Synthesis**: Combine a social media campaign (Branch 1) with selective pop-up events (Branch 2) for maximum impact. Use partnerships (Branch 3) to amplify reach at events.

Final Strategy: Launch with a TikTok influencer campaign showcasing eco-friendly clothing, paired with pop-up shops at green festivals to engage young adults directly. Collaborate with a sustainable accessory brand to co-promote at events.


**Explanation of Concept:**
Tree of Thoughts (ToT) involves generating multiple reasoning branches to explore different solutions to a problem, evaluating each, and synthesizing the best ideas into a final answer. Each branch represents a distinct approach, which is explored, assessed for pros and cons, and scored. This method is ideal for complex, open-ended tasks like strategic planning, as it encourages creative exploration and systematic comparison, as shown in the marketing strategy example above.

### **6. Best Practices for Effective Prompts**

#### 1. Be Specific and Clear

**Bad:**
```
Write about dogs.
```

**Good:**
```
Write a 300-word informative article about the health benefits of owning a dog, focusing on mental health, physical activity, and social connections. Use a friendly, accessible tone for general readers.
```

#### 2. Use Action Verbs

Be explicit about what you want the AI to do:
- Analyze, Compare, Create, Describe, Evaluate
- Extract, Generate, List, Rank, Summarize
- Translate, Write, Explain, Classify

#### 3. Provide Examples When Possible

Examples are the most powerful way to communicate your expectations.

#### 4. Structure Your Prompts

Use clear formatting:
```
Task: [What you want done]
Context: [Background information]
Format: [How you want the output structured]
Example: [Sample of desired output]
```

#### 5. Use Instructions Over Constraints

**Better:**
```
Write a professional email summarizing the key points from our meeting.
```

**Avoid:**
```
Write an email but don't make it too long or too informal or too detailed.
```

#### 6. Control Output Format

Specify exactly how you want the response structured:
```
Return your answer as a JSON object with the following structure:
{
  "main_idea": "string",
  "supporting_points": ["string", "string"],
  "confidence_level": "high/medium/low"
}
```

#### 7. Use Variables for Reusability

```
Role: You are a {expertise} expert
Task: Analyze the {document_type} and provide recommendations for {target_audience}
Context: This is for a {industry} company with {company_size} employees
```

#### 8. Iterate and Document

- Keep track of what works and what doesn't
- Document your successful prompts
- Test variations to improve performance

## **Class 03: Prompt and Context Engineering**

### **7. [Common Pitfalls and How to Avoid Them](https://github.com/panaversity/learn-low-code-agentic-ai/tree/main/00_prompt_engineering#common-pitfalls-and-how-to-avoid-them)**

#### a. Ambiguous Instructions

**Problem:** Vague requests lead to unpredictable outputs
**Solution:** Be specific about what you want

#### b. Contradictory Instructions

**Problem:** Conflicting requirements confuse the model
**Solution:** Review prompts for internal consistency

#### c. Too Many Constraints

**Problem:** Over-constraining limits model creativity
**Solution:** Focus on positive instructions rather than long lists of don'ts

#### d. Ignoring Token Limits

**Problem:** Responses get cut off mid-sentence
**Solution:** Set appropriate limits and structure accordingly

#### e. Not Testing Variations

**Problem:** Assuming first attempt is optimal
**Solution:** Test different phrasings, examples, and approaches

---

### **8. [Hands-On Examples](https://github.com/panaversity/learn-low-code-agentic-ai/blob/main/00_prompt_engineering/readme.md#hands-on-examples)

#### **Example 1: Content Creation**

**Task:** Create a social media post

**Basic prompt:**
```
Write a social media post about coffee.
```

**Improved prompt:**
```
Write an engaging Instagram post for a local coffee shop's new seasonal drink. 

Context: Fall season launch of Pumpkin Spice Maple Latte
Audience: Coffee enthusiasts aged 25-40
Tone: Warm, inviting, not overly promotional
Format: 
- Main text (150 characters max)
- 3-5 relevant hashtags
- Call to action

Include sensory details about taste and aroma.
```

#### **Example 2: Data Analysis**

**Task:** Analyze customer feedback

**Basic prompt:**
```
What do customers think about our product?
```

**Improved prompt:**
```
Analyze the following customer reviews and provide insights:

Reviews: [paste reviews here]

Please provide:
1. Overall sentiment breakdown (positive/negative/neutral percentages)
2. Top 3 most mentioned positive aspects
3. Top 3 most mentioned concerns or issues
4. Specific recommendations for improvement
5. Confidence level in your analysis

Format as a structured report with clear headings.
```

#### **Example 3: Code Generation**

**Task:** Create a function

**Basic prompt:**
```
Write a function to sort a list.
```

**Improved prompt:**
```
Write a Python function that:

Requirements:
- Sorts a list of dictionaries by a specified key
- Handles missing keys gracefully (items without key go to end)
- Supports both ascending and descending order
- Includes proper error handling
- Has clear documentation

Example usage:
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
result = sort_by_key(data, "age", descending=False)

Please include:
- Function definition with type hints
- Docstring with parameters and return value
- Example usage
- Brief explanation of the approach
```

### 9. **Testing and Iteration**

#### a. **Create a Testing Framework**

A testing framework is a documented, organized system for recording and analyzing how different prompts perform when interacting with an AI model. It involves creating a standardized way to:

- **Record** prompt variations, their goals, and settings (e.g., model used, temperature).
- **Test** these prompts to assess the quality of the AI's outputs.
- **Evaluate** results based on specific criteria (e.g., accuracy, relevance, style).
- **Iterate** by refining prompts based on insights from the tests.

The framework ensures that prompt engineering is not a haphazard process but a methodical one, allowing users to identify what works, what doesn’t, and how to improve prompts over time.

Document your prompts systematically:

| Prompt Version | Goal | Model | Temperature | Output Quality | Notes |
|----------------|------|-------|-------------|----------------|--------|
| v1.0 | Generate blog post | GPT-4 | 0.7 | Good | Too formal |
| v1.1 | Generate blog post | GPT-4 | 0.7 | Better | Added tone guidance |

#### b. **A/B Test Different Approaches**

A/B testing in prompt engineering involves creating and trying out multiple versions of a prompt (e.g., different wordings, structures, examples, or settings like temperature) to see which version yields the most accurate, relevant, or high-quality output from the AI. It’s a systematic way to experiment and optimize prompts by comparing their performance side by side.

Try variations:
- Different example sets
- Various instruction phrasings
- Different temperature settings
- Alternative output formats

#### c. **Evaluate Results**

Consider:
- **Accuracy**: Does it answer correctly?
- **Relevance**: Is it on-topic?
- **Completeness**: Does it cover everything needed?
- **Style**: Does it match the desired tone?
- **Format**: Is it structured as requested?

#### d. **Common Evaluation Metrics**

- **Consistency**: Same prompt, similar outputs
- **Following instructions**: Adherence to specific requirements
- **Creativity** (when desired): Novel and interesting responses
- **Factual accuracy**: Correctness of information

### **Advanced Tips for 2025**

#### 1. Leverage Structured Outputs

Use JSON, XML, or other structured formats for complex data:
```
Return analysis as JSON:
{
  "summary": "brief overview",
  "key_insights": ["insight1", "insight2"],
  "recommendations": [
    {
      "action": "specific action",
      "priority": "high/medium/low",
      "timeline": "timeframe"
    }
  ]
}
```

#### 2. Context Management

For long conversations:
- Summarize previous context
- Use system messages effectively
- Break complex tasks into smaller parts

#### 3. Multi-Modal Prompting

When working with models that support images:
- Be explicit about what to look for in images
- Combine text and visual instructions
- Use images as examples or context

#### 4. Prompt Chaining

Break complex tasks into steps:
```
Step 1: Research the topic
Step 2: Create an outline based on research
Step 3: Write the full content based on outline
```
### 10. **Resources and Next Steps**

#### Tools and Platforms
- **OpenAI Playground**: Test prompts with GPT models
- **Anthropic Console**: Experiment with Claude
- **Google AI Studio**: Try Gemini models
- **Prompt optimization tools**: Available from various providers

#### Learning Resources
- Model documentation and guides
- Community forums and Discord servers
- GitHub repositories with prompt examples
- Academic papers on prompt engineering techniques

#### Practice Projects
1. **Personal Assistant**: Create prompts for scheduling, email drafting
2. **Content Creation**: Develop templates for different types of writing
3. **Data Analysis**: Build prompts for interpreting datasets
4. **Code Review**: Create prompts for code analysis and improvement

#### Building a Prompt Library
- Create templates for common tasks
- Document what works for different models
- Share and learn from other practitioners
- Keep updating as models improve

### 11. **Mixture-of-Experts (MoE) and Prompt Engineering**

Mixture-of-Experts (MoE) is a machine learning architecture designed to improve the efficiency and scalability of large models, particularly in the context of Large Language Models (LLMs). It draws from the concept of dividing complex tasks among specialized "experts" in a system, allowing the model to activate only a subset of its parameters for a given input rather than using the entire model every time. This sparse activation leads to computational savings while maintaining or even enhancing performance.

![Mixture of Experts Architecture](assets/moe.webp)


#### MoE Implementation Status in Frontier Models
Below is an table summarizing the Mixture-of-Experts (MoE) implementation status based on available information up to August 2025. 

| **LLM**                | **Developer**         | **MoE Implementation** | **Details**                                                                 |
|------------------------|-----------------------|------------------------|-----------------------------------------------------------------------------|
| **GPT-5**              | OpenAI               | Yes (Speculated)       | Likely uses MoE with dynamic routing for reasoning levels. Estimated ~2T total parameters. No official confirmation, but performance (e.g., 74.9% SWE-bench) suggests sparse MoE-like design. |
| **Grok 4**             | xAI                  | Yes (Confirmed)        | Utilizes MoE with multi-agent architecture. ~500B total parameters, sparse activation. Strong performance on ARC-AGI (16.2% with Thinking Mode). Expert count not disclosed. |
| **Gemini 2.5 Pro**     | Google               | Yes (Confirmed)        | Confirmed MoE with advanced reasoning capabilities. Details on sparsity and expert count not specified, but designed for efficient scaling. |
| **Claude 4**           | Anthropic            | Unknown                | No confirmed details on Claude 4. Based on Claude 3.5 Sonnet, no MoE implementation is confirmed. Estimated ~400B parameters, likely dense architecture. |
| **DeepSeek-V3**        | DeepSeek             | Yes (Confirmed)        | MoE model with 671B total parameters, 37B active per token, using DeepSeekMoE architecture with Multi-Head Latent Attention (MLA). Highly efficient, trained on 14.8T tokens for ~$5.6M. |[](https://arxiv.org/abs/2412.19437)[](https://www.infoq.com/news/2025/01/deepseek-v3-llm/)

#### Notes:
- **GPT-5**: MoE is speculated due to its dynamic routing and massive scale (~2T parameters), suggesting a sparse architecture. No official OpenAI confirmation.
- **Grok 4**: Confirmed MoE with multi-agent design for specialized task handling, enhancing efficiency through sparse activation.
- **Gemini 2.5 Pro**: Confirmed MoE, optimized for scalability, though specific expert counts are undisclosed.
- **Claude 4**: No explicit data on Claude 4. Assuming similarity to Claude 3.5 Sonnet, it likely uses a dense transformer without MoE, pending new evidence.
- **DeepSeek-V3**: Explicitly uses MoE with 671B total parameters, activating only 37B per token via DeepSeekMoE and MLA, achieving cost-effective training and inference. Outperforms many open-source models on benchmarks like MMLU and SWE-bench.

#### **Key Components of MoE:**
1. **Experts:** These are specialized sub-networks (often feed-forward neural networks) within the model, each trained to handle specific types of data or tasks. For example, one expert might specialize in mathematical reasoning, another in creative writing, and so on. In advanced LLMs, there can be dozens or hundreds of experts (e.g., Mixtral 8x7B has 8 experts per layer).

2. **Gating Network (or Router):** This is a lightweight mechanism (typically a simple neural network) that evaluates the input and decides which experts to route the data to. It assigns weights or probabilities to experts, selecting the top-k (e.g., top 2 out of 8) most relevant ones. The output is a weighted combination of the selected experts' responses. The gating is learned during training and can be dynamic, adapting to the input.

> - `Router` or `Gating Model` decides which expert will give the answer of user query.
> - Router model return probability of experts to you
> - Prompting is important here in order to get potential result from MOE

3. **Sparse Activation:** Unlike dense models (e.g., GPT-3 or Llama) where all parameters are activated for every token, MoE activates only a fraction (e.g., 10-20%) of the parameters per input. This makes MoE models "conditionally compute" – they scale to trillions of parameters but run as efficiently as smaller dense models during inference.

##### **Dense Vector VS Sparse Vector**
1. **Dense Vectors**
  * **Definition:** Every element in the vector has a (usually nonzero) value or if zero quantity is less so it called dense vector.
  * **Usage:** Standard LLMs (like GPT) use dense layers, where all neurons are active for every input.
  * **Effect:**
    - More computation and energy use.
    - All parameters participate in generating the output.
    - Example: Transformer feedforward layers.

2. **Sparse Vectors**
  * **Definition:** Most elements are zero or inactive, only a subset is used or if zero quantity is more so it called sparse vector.
  * **Usage in MoE:** MoE models activate only a few “experts” (sub-networks) per input — making computation sparse.
  * **Effect:**
    - Saves compute while keeping total model capacity large.
    - Only selected experts (e.g., 2 of 64) process each token.
    - Example: **Switch Transformer, Mixtral, DeepSeekMoE.**

![MOE](assets/MOE.png)

## **Class 04: Prompt and Context Engineering**

### 11. **Mixture-of-Experts (MOE) and Prompt Engineering (Cont.)

#### **[How Does MoE Change Prompt Engineering?](https://github.com/panaversity/learn-low-code-agentic-ai/blob/main/00_prompt_engineering/readme.md#how-does-moe-change-prompt-engineering)**

* Prompt engineering – the art of crafting inputs to elicit optimal responses from LLMs – traditionally focuses on clarity, structure, role-playing, chain-of-thought (CoT), and few-shot examples to guide dense models.
* MoE introduces nuances because of its modular, expert-based design, shifting the focus toward "expert elicitation" and robustness to routing dynamics. While core principles remain, MoE can make prompts more effective (or unpredictable) depending on how they activate the underlying experts. Here's how it impacts the practice:
  - Need for Expert-Aware Prompting:
  - Enhanced Chain-of-Thought (CoT) and Multi-Step Reasoning:
  - Handling Sparsity and Variability:
  - Efficiency in Prompt Length and Complexity:
  - Broader Implications and Best Practices:

---

### **6 Steps Prompting Framework**
This framework works across all major AI models (ChatGPT, Gemini, Claude) and is based on fundamental principles of how large language models operate.

#### 1. **Command: Start Strong, Not Soft**
- Use action verb to give command
- Dont used words like `help me` etc.

**The Problem:** Most people ask vague questions or make wishy-washy requests.

**The Solution:** Every great prompt starts with a clear, direct command using action verbs.

**Bad Example:**
```
Give me investing advice
```

**Good Example:**
```
Recommend a diversified investment strategy for a moderate risk investor saving for a home within 5 years
```

**Key Principles:**
- Use strong action verbs: analyze, create, design, recommend, generate, evaluate
- Avoid weak words like "give" or "help"
- Be specific about what you want
- Set a professional, focused tone

#### 2. Context: More is Always Better

**The Rule:** AI can take your prompt in any direction if you let it. Your job is to narrow it down with the right background, constraints, and goals.

**Bad Example:**
```
Recommend a diversified investment strategy for me
```

**Good Example:**
```
Recommend an investment strategy for a 32-year-old with moderate risk tolerance, earning $90,000/year, saving to buy a home in 5 years
```

**The Rule of Three Framework:**
- **Who:** Age, profession, experience level, situation
- **What:** Specific goal, constraints, requirements
- **When:** Timeline, deadlines, urgency

**Context Scaling:**
- Simple requests (restaurant recommendation): Minimal context needed
- Complex projects (business plan): Extensive context required
- Life-changing decisions: Maximum context investment

#### 3. Logic: Define the Output Structure

**The Problem:** Without guidance, AI will respond in whatever format it chooses, which might not be useful for your needs.

**The Solution:** Tell the AI exactly how to think and respond.

**Basic Example:**
```
List the asset categories, explain the percent allocation for each, and briefly justify the rationale behind each choice
```

**Advanced Formatting Options:**
- "Format this as a screenshotable Apple Notes format"
- "Give me a copy-and-pasteable asset I can send to my partner"
- "Respond in PDF format for saving and sharing"
- "Create this as a table with columns for..."
- "Structure this as an interactive checklist"

**Key Questions to Ask Yourself:**
- Do I want this in a table, graph, or list format?
- Will I need to share this with others?
- How will I use this information next?

#### 4. Roleplay: Transform Generic into Expert-Level

**The Power:** The way you prompt doesn't just affect what AI says—it affects who it becomes.

**Basic Example:**
```
You are a certified financial advisor with 15 years of experience specializing in personal finance and mid-term investment planning
```

**Role Variations by Field:**
- **Finance:** "Certified financial advisor with 15 years experience in personal finance"
- **Marketing:** "Senior marketing strategist with expertise in digital campaigns"  
- **Technology:** "Senior software architect with 10 years in enterprise systems"
- **Legal:** "Corporate lawyer with 10 years experience in contract law"

**Style and Tone Modifiers:**
- "Be brutally honest and conservative in your advice"
- "Take a creative and innovative approach"
- "Provide practical, actionable recommendations"
- "Focus on data-driven insights"

#### 5. Formatting: Structure for Success

**The Goal:** Organize information in a way that's immediately useful and actionable.

**Example Structure:**
```
Format the response as a clear list with bullet points under three sections:
1. Asset Allocation (with percentages)
2. Rationale for Each Category  
3. Risk Considerations
```

**Popular Formatting Options:**
- Numbered lists for sequential steps
- Bullet points for equal-weight items
- Tables for comparing options
- Sections with headers for complex topics
- Summary boxes for key takeaways

#### 6. Questions: The Secret Sauce

**The Game-Changer:** After building your complete prompt (command + context + logic + roleplay + formatting), add this powerful ending:

```
Ask me 10 questions that will help you tailor this strategy even more
```

**Why This Works:**
- AI identifies gaps in your prompt that you missed
- Provides nuanced questions you hadn't considered
- Leads to dramatically better, more personalized results

**The Advanced Question Strategy:**

1. **Round 1:** "Ask me 10 questions to tailor this better"
2. **Round 2:** "Based on my answers, ask 10 more questions that fill in gaps"  
3. **Round 3:** "Give me 10 more detailed questions"
4. **Stop when:** AI starts repeating questions (means it has enough info)

**Pro Tips:**
- Use voice memos for answering questions (faster and more natural)
- For major decisions: Go through 20-30 questions
- For simple tasks: 3-5 questions are sufficient
- The more life-changing the decision, the more questions you should answer

#### Complete Example: Putting It All Together

Here's how the full framework looks in practice:

```
**COMMAND:**
Recommend a comprehensive investment strategy 

**CONTEXT:**
for a 32-year-old software engineer with moderate risk tolerance, earning $90,000/year, with $25,000 in savings, looking to buy a home in 5 years while also building long-term wealth

**LOGIC:**
List the asset categories, explain the percent allocation for each, justify the rationale behind each choice, and include specific investment vehicles or funds

**ROLEPLAY:**
You are a certified financial advisor with 15 years of experience specializing in personal finance and mid-term investment planning for tech professionals

**FORMATTING:**
Format the response as:
1. Executive Summary (2-3 sentences)
2. Asset Allocation Table (with percentages and reasoning)
3. Specific Investment Recommendations
4. Timeline and Milestones
5. Risk Management Considerations

**QUESTIONS:**
Ask me 10 questions that will help you tailor this strategy even more specifically to my situation
```

#### Best Practices and Pro Tips

##### Model Selection
- **ChatGPT & Gemini:** Best for this framework (battle-tested)
- **Claude:** Works well with slight modifications
- **Specialized Models:** May require framework adjustments

##### Context Balancing
- **High-Stakes Decisions:** Invest heavily in context and questions
- **Daily Tasks:** Use abbreviated version with 3-5 elements
- **Creative Projects:** Emphasize roleplay and formatting elements

##### Voice Memo Strategy
- Use your phone's voice memo feature for answering AI questions
- Speak naturally and conversationally
- Let AI ask follow-up questions until it stops finding new angles

##### Iteration Approach
1. Start with basic framework
2. Let AI ask questions and answer them
3. Refine the prompt based on gaps identified
4. Generate final output when AI stops asking fresh questions

#### Common Mistakes to Avoid

1. **Skipping the Command:** Starting with questions instead of clear directives
2. **Insufficient Context:** Providing generic information that could apply to anyone
3. **No Output Structure:** Letting AI choose its own response format
4. **Generic Roles:** Using vague expertise instead of specific professional roles
5. **Stopping Too Early:** Not using the questions feature to refine results

#### Advanced Applications

This framework scales from simple daily tasks to complex professional projects:

- **Personal:** Meal planning, workout routines, travel itineraries
- **Professional:** Business plans, marketing strategies, technical documentation  
- **Creative:** Content scripts, design briefs, storytelling frameworks
- **Educational:** Study guides, research plans, learning curricula
