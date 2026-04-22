# Observability & Cost Control

Official Github Repo: [Observability & Cost Control](https://github.com/panaversity/learn-agentic-ai-from-low-code-to-code/blob/main/09_observability/readme.md)

## Scenario 1: LLM took too long to respond, increased token consumption, and caused the AI to loop or halt unexpectedly

### 1. Research Assistant Bottleneck
- **Latency**: Responses are delayed, averaging 64 seconds per query.
- **Token Consumption**: Excessive token usage, exceeding 24,000 tokens for simple queries.

### 2. Root Cause Analysis
- **Tool and Reasoning Loop**: The agent repeatedly invokes tools and reasoning steps for the same query, leading to redundant processing and inflated token consumption.

### 3. Recommended Checklist
- **User Message Validation**: Ensure the input query is appropriate and clearly defined.
- **System Instruction Review**: The current instruction prompts the agent to iterate through search, analysis, and query refinement cycles even when initial results are satisfactory, causing unnecessary repetition.

### 4. Primary Cause Identification
The root cause originates from system instruction design, which perpetuates unnecessary processing cycles.

### 5. Expected Outcomes Upon Resolution
- Elimination of repetitive tool invocations
- Significant reduction in token consumption
- Decreased latency in response times
- Overall improvement in system reliability and reduction in failure rates

Addressing the system instruction to terminate processing upon achieving adequate results will effectively mitigate the identified bottleneck.

## Scenario 2: Travel Assistant Agent

### 1. Issue / Bottleneck:
- **Latency / Highest response time**
- **Extensive token usage**
- **Complex LLM call due to instructions**
- **Unnecessary length of system instruction**
- **Verbose/Messy Output**
- **Context Repetition**

### 2. What can be reduced??
- **Reduce prompt size**
- **Reducing prompt size will reduce context length**
- **Model intelligence considerations**: Higher capability models will incur higher costs
- **Retrieve data from external sources (RAG)**: While not applicable in this specific case, generally this approach should be considered to reduce token load

### 3. Rule of Thumb:
1. **Time management / latency**
2. **Token usage**  
3. **Repetitive operations**
   
These three areas should be checked and observed first, as addressing them will likely resolve approximately 95% of performance issues.