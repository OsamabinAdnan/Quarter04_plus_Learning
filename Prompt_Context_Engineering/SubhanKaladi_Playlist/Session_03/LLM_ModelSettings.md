# **LLM Model Settings (Essential Configuration Settings)**

**[Canva Presentation](https://www.canva.com/design/DAG2iU_MYIc/phqBOJFefuNSLTnqtelwVA/view?utm_content=DAG2iU_MYIc&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h8c2c00c669#1)**

Before diving into prompt techniques, understand these key parameters that control AI behavior:

### **Temperature (0-1)**
* **Low (0-0.3):** Focused, consistent, deterministic responses
* **Medium (0.4-0.7):** Balanced creativity and consistency
* **High (0.8-1.0):** Creative, diverse, but potentially unpredictable

**When to use:**
* **Temperature 0:** Math problems, factual questions
* **Temperature 0.7:** Creative writing, brainstorming
* **Temperature 0.9:** Poetry, experimental content
* **Temperature => 1.0:** Unpredictable response, randomness

**Some models are range from 0.0 to 2.0.**
* `0.1` means Focus response
* `0.5` means Balance response
* `1.0` means Creative response, add randomness
* `1.5` means Unpredictable response

### **Output Length/Token Limits**
* Controls maximum response length
* `Higher limits` = more computational cost
* Set appropriately for your task needs

### **Top K:** `Limits choices to top K most likely tokens`

* **🔹 Purpose:** It controls how many of the model’s most likely next tokens are considered during text generation.
* **🔹 Meaning:** `k `= the number of top tokens (by probability) kept at each prediction step.
* **🔹 Process:**
    1) The model predicts probabilities for all possible next tokens.
    2) It keeps only the top k tokens with the highest probabilities.
    3) It randomly selects the next token **only from these k options.**
* **🔹 Example:**
    - If `k = 1` → always picks the single most likely token (deterministic, less creative).
    - If `k = 50` → picks from the top 50 tokens (more variety, more creativity).
* **🔹 Trade-off:**
    - `Smaller k` → safer, more focused outputs.
    - `Larger k` → more diverse, sometimes less coherent text.

In short: `top_k` **limits how many high-probability words the model can choose from next — balancing focus and creativity.**

### **Top P:** `Limits choices based on cumulative probability`

* **🔹 Purpose:** Controls randomness by using a **probability threshold** instead of a fixed number of tokens.
* **🔹 Meaning:** `p` = the cumulative probability cutoff.
* **🔹 Process:**
    1) The model sorts all tokens by probability (highest to lowest).
    2) It keeps the **smallest set of tokens whose total probability ≥ p.**
    3) It randomly selects the next token from **that set.**

* **🔹 Example:**
    - If `p = 0.9`, the model picks from the top tokens that together make up **90% of total probability.**
    - The number of tokens varies each time — unlike `top_k`, which is fixed.

* **🔹 Trade-off:**
    - Lower `p` (e.g., 0.5) → safer, more predictable text.
    - Higher `p` (e.g., 0.95) → more creative and varied text.

In short: `top_p` **keeps only the most probable tokens that together reach a certain confidence level, balancing coherence and creativity dynamically.**

### **Recommended starting points:**

* **Conservative:** Temperature 0.1, Top-P 0.9, Top-K 20
* **Balanced:** Temperature 0.2, Top-P 0.95, Top-K 30
* **Creative:** Temperature 0.9, Top-P 0.99, Top-K 40