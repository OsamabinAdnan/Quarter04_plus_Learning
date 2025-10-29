# **How AI Like ChatGPT is Built: A Step-by-Step Guide**

Link of [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) YouTube video

## **Introduction: The Magic Behind the Text Box**

You type a question into an AI chat window, press enter, and watch as a remarkably human-like response appears. But what are you talking to, exactly? What is happening behind that simple text box that allows a machine to write poetry, debug code, or explain quantum physics?

This article will demystify that magic. We will embark on a journey through the entire pipeline of how a large language model (LLM) is built, framing it as a three-stage process of learning from a textbook. We'll start with a raw "internet simulator" that has read all the background material, move to an expert imitator that has studied all the worked examples, and end with a genuine problem-solver that has learned how to think by doing the practice problems for itself.


--------------------------------------------------------------------------------


### **1. Stage 1: The Foundation — `Pre-training` a "Base Model"**

The first stage is like building a vast library and having an AI read every single book. This is the Exposition phase of our textbook analogy, where the model builds its core knowledge by absorbing the patterns, facts, and nuances of human language on a global scale. It is a massive, computationally expensive process that forms the foundation for everything to come.

#### **1.1. Step 1: Download and Process the Internet**

The journey begins by gathering an immense amount of text from publicly available sources. A major starting point is Common Crawl, an archive of billions of web pages. The goal of this data collection is threefold:

* **Huge Quantity:** The model needs to see trillions of words to learn the near-infinite statistical patterns of language. More data means more patterns. To ground this, the massive FineWeb dataset, containing 15 trillion tokens, is only about 44 terabytes—a size that could fit on a single modern hard drive.
* **High Quality:** Raw internet data is messy. It's aggressively filtered to remove spam, malware, and low-quality content, ensuring the model learns from well-written and informative text.
* **Large Diversity:** To be broadly knowledgeable, the model needs text from a wide variety of topics, including science, history, art, and everyday conversation.

This raw data is heavily processed to extract just the main text (removing ads and navigation bars), filter by language, and remove personally identifiable information (PII).

---
![Fineweb Recipe](assets/fineweb-recipe.png)

---
#### **1.2. Step 2: From Text to "Tokens"**

An AI doesn't see words or characters the way we do. Instead, it breaks text into small, manageable chunks called `tokens`. You can think of tokens as  **atoms of text.** This process of converting text into a sequence of token IDs is called **`tokenization`**.

There's a trade-off here: a small vocabulary of tokens (like only 0s and 1s) would create extremely long sequences, while a larger vocabulary makes sequences shorter and more efficient. Models like GPT-4 use a vocabulary of around 100,000 unique tokens, which can represent common words, parts of words, or characters.

- In tokenization, convert text into sequences of symbols `(token)`
- Start with stream of bytes (256 tokens)
- All tokens represent `text chunks`, they are all like atoms of these sequences and numbers are just unique IDs
- Run the `Byte Pair Encoding algorithm` (iteratively merge the most common token pair to mint new token)

Example: ~5000 text characters
* ~= 40,000 bits (with vocabulary size of 2 tokens: bits 0/1)
* ~= 5000 bytes (with vocabulary size of 256 tokens: bytes)
* ~= 1300 GPT-4 tokens (vocabulary size 100,277)
---
![App to count Token](assets/tokenization.png)

---
#### **1.3. Step 3: The Training Game — Predicting the Next Token (Neural Network Training)**

> In this step, we want to model the statistical relationships of how these tokens follow each other in the sequence, we take windows of token from data fairly randomly, window length can range anywhere between 0 to some maximum size of our chosen, for e.g., token window of 8000 tokens.

- Processing of long window sequences would be very computationally expenses.
- We pick small set of token, as you see in below picture, these four `tokens are context and they feed into neural network as input`.

---
![Next Token Prediction](assets/next%20token%20prediction.png)

---
- With a massive dataset of token sequences, the training can begin. The fundamental task during pre-training is incredibly simple:` predicting the next token in a sequence`.

    * **Input of Neural Network:** Sequences of tokens of variable length anywhere between 0 to maximum size (like 8000 tokens)
    * **Output of Neural Network:** Next token in the sequence, what's come next?

- As per above picture, our vocabulary has 100,277 possible tokens, the neural network output exactly that many numbers and all those numbers correspond to that many tokens (i.e., 100277 tokens) as coming next in the sequences, so it's making guesses about what comes next

- In the beginning, neural network is randomly initialized, so as the probabilities in the very beginning of the training are also going to be kind of random

    * probability of 19438 (" Direction"): `4%`
    * probability of 11799 " Case": `2%`
    * probability of 3962 " Post": `3%`

- Imagine the entire 15-trillion-token training set as a single, giant piece of text.. The model is shown a "window" of tokens (the context) and its only job is to guess the single token that comes next. The training process iteratively `"nudges" (a light touch or push.)` the model's billions of internal parameters—think of them as tiny adjustment knobs—so that its predictions get slightly better each time, aligning with the statistical patterns of language found on the internet.

- `We have mathematical process to make update in neural network like a way of tuning it`, so that correct answer has higher probability, so if I make update in neural network now, the next time i feed above particular sequence of four tokens in neural network, it will be slightly adjusted and change the probability depend. 
- This is the way of `nudging` of slightly updating the neural network to basically given the higher probability to the correct token that comes next in the sequence.

    * probability of 19438 (" Direction"): `2%`
    * probability of 11799 " Case": `1%`
    * probability of 3962 " Post": `4%`

- This process happens at the same time for all tokens in the entire dataset. In practice we sample little windows, little batches of windows and then every single one of these tokens.
- We want to adjust our neural network so that the probability of that token become slightly higher and this all happens in parallel in large batches of tokens. This is the process of training neural network, its a sequence of updating it so that it predictions match up the statistics of what actually happens in your training set. Its probabilities become consistent with our statistical pattern of how these tokens follow each other in a data.

    ##### **Neural Network Internals**
    ---
    ![Neural Network Internals](assets/neural%20network%20internal.png)

    ---

    - `Input sequence` mixed with `giant mathematical expression` together with `parameters or weights` of neural network
    - Modern neural network has billion of parameters and in the beginning they are randomly set
    - Because parameters are randomly set, you can expect this neural network will make random predictions and it does
    - Iteratively updating the network (training a neural network), the setting of parameter get adjusted such that the output of neural network becomes consistent with the pattern seen in our training set.
    - Training of neural network means `discovering a setting of parameters` that seems to be consistent with the statistics of the training set.
    - Neural Network Architecture Reasearch is a subject to design effective mathematical expression having convenient characteristics.
    - [Neural Network 3d Visualization](https://bbycroft.net/llm)

#### **1.4. Inference**

Inference is the process where an LLM generates text by predicting one token at a time, using what it learned during training. Inference is like generating new data from the model, we want to basically see what kinds of patterns it has initialized in the parameters of its network. 

- Inference is the stage where the trained model is used to generate or predict new text.
- It’s what happens after the model has already been trained.

**Think of it like this:**

- `Training =` teaching the model by showing it tons of examples and adjusting its internal settings (“weights”).
- `Inference =` asking the trained model to use what it learned to predict the next word (token).

##### **🔄 How it works (step-by-step, based on your image):**

1) **You give the model some starting text (context)**

    Example:
    > “The weather today is”

2) **Model converts that text into tokens**
    (numbers like 91, 860, 287, etc.)

3) **Neural network predicts the next token**
    It calculates the probability for every possible next token — e.g.:

    * “sunny” → 40%
    * “rainy” → 20%
    * “cold” → 10%
    The token with the highest probability (or sampled randomly) is chosen.

4) **That new token is added to the input, and the process repeats**
Now the model predicts the next one again, using the updated sequence.

5) **Repeat this loop until it completes a full sentence, paragraph, or response.**

---
![Inference](assets/step04_inference.png)

---
- Now that the model is trained, it enters the inference phase — the stage where it actually generates text.
Here’s where one key idea matters: **LLMs are stochastic systems** — meaning their behavior involves randomness.
- That means their predictions involve controlled randomness — similar to flipping a weighted coin.
- At each step, the model doesn’t always pick the single most likely next token. Instead, it samples from a probability distribution of possible tokens, allowing for natural variation and creativity.

    * **Randomness with structure:** Because of this probabilistic sampling, the model can generate slightly different outputs each time, even from the same prompt.
    * **Reusing learned fragments:** Sometimes, you’ll see small snippets or phrases that resemble parts of the training data. This happens because the model has statistically learned those patterns very well.
    * **Generating new combinations:** More often, though, the model produces sequences that were never seen **verbatim** (in exactly the same words as were used originally) in its training set. It’s not copying—it’s **remixing** ideas, forming new combinations that *feel* familiar because they share the same statistical structure as the data it learned from.
    * **Divergent token streams:** Since each token influences the next, small random differences compound over time. Within just a few steps, you can end up with a completely new sequence—a **unique stream of tokens inspired by training data, not identical to it.**

- So, inference is where the model takes what it learned, applies a touch of randomness, and begins creating text that’s statistically grounded yet never fully predictable.

##### **GPT(Generative Pre-trained Transformer)-2 training and inference**
---
![GPT-2](assets/gpt-2.png)

---
- Processing 1 million token per update
- Each update taking 7 seconds roughly
- Taking 32000 steps of optimizations
- 32000 steps with 1 million tokens each is about 33 billion tokens that are going to process
- 420/32000 showing 420 steps are done out of 32000
- Every 20 steps, he has configured this optimization to do inference.
- This is `Gold Rush`. Gold Rush is getting GPUs and getting enough them, so they can all collabrate to perform this optimization to predict next token on a dataset (like the fine web dataset in this case).
- This is the computation workflow that is extremely expensive, the more GPUs you have, the more tokens you can try to predict and improve on. You can process this dataset faster, you can iterate faster to get a bigger network and train it.

##### **Base Model**

Once the model has been trained (and inference is working), what we get is called a **Base Model** — sometimes also referred to as a pretrained model or foundation model.

###### **🔹 What is the Base Model?**

- The Base Model is the raw neural network right after its pretraining phase — the phase where it learned to predict the next token from massive amounts of internet text.
- Base Model is an `internal text token simulator`

- At this point, the model has:

    * Learned grammar, facts, concepts, and styles of human language.
    * Developed a strong sense of statistical relationships between words and ideas.
    * Acquired general language understanding and generation ability.

But…

- Even though it can generate text, the base model is not aligned with human expectations or task goals.
It hasn’t been taught how to respond helpfully, safely, or coherently in conversations.

- The base model knows a lot, it doesn’t know what you want from it. It’s like a brilliant but untrained intern — full of raw knowledge, but no understanding of how to communicate or behave appropriately.

###### **LLAMA 3.1 Base Model Inference**
---
![Base Model and LLAMA 3](assets/base%20model%20and%20LLAMA%203.png)

---
- Check `LLAMA-3.1-405B-Base` model on hyperbolic website (link mentioned at the end of this docs)
- LLAMA-3.1-405B-Base means its the base model not assistant trained on 405 billion parameters.
- LLAMA-3.1-405B-Base is just token autocomplete (from the internet) and stochastic system
- It is still very useful b/c in the task of predicting the next token in the sequences the model has learned lot about the world and store all that knownledge in its parameters of the network.
- BaseModel regurgitate, `Regurgitation` refers to when a language model reproduces text from its training data verbatim — that is, it spits back exact or near-exact passages it has seen before, instead of generating new, original combinations. In simple terms:

    > In Regurgitation, the model `memorizes` parts of the data rather than `learning` general patterns — and later repeats that text word-for-word during generation.

    * **🔹 Why Regurgitation Happens (especially in Base Models)**
    Regurgitation is most noticeable in Base Models (the raw pretrained models) because:

    1) **Their training objective is purely next-token prediction.:** They’re rewarded for guessing the next token correctly — not for being original or avoiding repetition.

    2) **They train on massive text datasets:** When some text snippets or code appear many times online, the model can memorize them instead of learning generalizable patterns.

    3) **No alignment or filtering yet:** Base Models haven’t gone through alignment stages like supervised fine-tuning (SFT) or RLHF, which encourage human-like, useful, and non-repetitive responses. So they can easily output copied segments from the web.

- If a Base Model’s knowledge cutoff is in 2023 and you ask it about an event from 2024, it will likely **hallucinate** — meaning it will generate a plausible-sounding but potentially incorrect answer.
- This happens because the model doesn’t actually *know* about events beyond its training data; instead, it relies on **probabilistic token prediction** to guess what might come next, since its primary objective is simply to generate the next most likely token.

**We have done in Stage 01: Pre-training**
* In this stage, the model is trained on vast amounts of text from the internet.
    > The data is first broken down into tokens — small chunks of text — and the model learns to **predict the next token** in a sequence using a neural network.

* After months of computation and millions of dollars in training, the result is a **Base Model** — essentially an *internet text simulator or a glorified autocomplete system.*

* It has absorbed an enormous amount of knowledge, compressed within its parameters — like a **“lossy zip file of the internet.”**

However, this model is **not yet a helpful assistant**. It can mimic how people write and continue text, but it doesn’t truly understand instructions or intent.
This raw, knowledge-rich model becomes the foundation for the next stage, where it will learn how to respond usefully by studying human-guided examples.


--------------------------------------------------------------------------------

### **2. Stage 2: Post Training Stage - Supervised Fine-Tuning (SFT)**

The **Supervised Fine-Tuning (SFT)** stage transforms the raw `Base Model` into an AI system that can follow instructions and hold natural, human-like conversations.
This stage can be thought of as the `“Worked Examples”` section of the model’s textbook — *where it learns how to act like an expert assistant* by studying examples written by humans.

SFT is **much faster and cheaper** than pre-training, often taking hours or days instead of months, yet it plays a `critical role` in shaping the model’s behavior.

#### **2.1 Programming by Example**

In this phase, the massive internet text dataset used during pre-training is **replaced** with a smaller, **highly curated dataset** composed entirely of `multi-turn conversations` between humans and assistants.

Each data point looks like a chat dialogue:

```sql
User: How can I learn Python?
Assistant: You can start with online tutorials, interactive courses, and small projects.

```

This dataset is created by **human labelers** — skilled annotators or domain experts (e.g., programmers, writers, educators).
They follow detailed **guidelines** instructing them to produce responses that are *helpful, truthful, and harmless.*

When you interact with a model like ChatGPT, you’re essentially engaging with a **statistical simulation of these human experts**.

#### **2.2. Conversations**

- The Base Model, originally trained on general internet text, is now **retrained** on this new **dataset of conversations.**

- Although the **training algorithm remains the same** (next-token prediction), the **data type changes** — from web documents to structured dialogues.

- This single change fundamentally alters the model’s behavior:

    * Instead of completing web pages, the model now learns to complete **conversations** in the style of a **helpful assistant.**

- Modern SFT pipelines also include **synthetic data** — AI-generated conversations created by other powerful models, which are then reviewed and edited by humans to ensure quality and safety.

##### **Tokenization of Conversations**

- During Supervised Fine-Tuning (SFT), the goal is to teach the Base Model how to behave like a helpful assistant by showing it examples of human-style conversations — prompts and ideal responses.

- Before these conversations can be used for training, they must be tokenized — that is, converted into numerical form so the model can process them.

    1) **Structuring Conversational Data:** Supervised Fine-Tuning (SFT) datasets are usually organized into structured conversation formats such as:
        * Each dialogue is represented as a sequence of `messages` with clear roles:
            - system → sets behavior or context
            - user → provides input or question
            - assistant → provides the ideal, human-written response
        * This structure ensures the model learns when and how to respond appropriately.

    2) **Tokenization Rules:** Once the conversation structure is defined, it’s `encoded into tokens` — small numerical units representing words, punctuation, and formatting.
        * The model learns the relationships between these token sequences:
            - How `user tokens` lead to `assistant tokens`
            - How to maintain context across turns
            - When to stop or switch roles
        * Special tokens such as `<|im_start|>`, `user`, and `assistant` are used to delineate conversation boundaries, marking who is speaking at each point.

        ```bash
        <|im_start|>user
        Hello!
        <|im_start|>assistant
        Hi there! How can I help you today?
        ```
        * During training, the model learns:
            - How user tokens lead to assistant tokens
            - How to predict the next response token-by-token
            - When to end or transition between conversation turns
        * These tokens are later `decoded` back into human-readable text during inference.

    3) **Why This Matters in SFT:**
        * This tokenization and structuring step ensures:
            - The model understands `conversation flow` (who’s speaking, when to reply).
            - The model learns `instruction-following behavior` rather than just text prediction.
            - Training remains `consistent`, because all conversation data follows the same encoding format.

- **The Magic of talking to AI:**

* When you chat with ChatGPT, the responses you get aren’t coming from a magical or conscious intelligence.
Instead, they’re generated based on **patterns learned from human-written examples** in its training data.

* These examples were created by human labelers who followed detailed **instruction guidelines** provided by the company.
So, in a way, when you talk to ChatGPT, you’re really interacting with a **statistical imitation of those human labelers.**

* The model has learned to predict *what a well-trained human labeler would say* in a similar situation —
so each reply you get is like a **simulation of how an expert human would respond**, not the thoughts of an actual AI mind.

* Pretrained Knowledge + Postering Dataset = Result
---
![Conversation](assets/Step02-Conversations.png)

---

##### **Hallucinations, tool use, knowledge/working memory**

These are the Emergent cognitive effects of the training pipeline that we have for models

* Hallucination refers to when LLMs generate outputs that are factually incorrect, misleading, or entirely fabricated despite appearing coherent and plausible.
* These outputs seem confident and trustworthy but have no real grounding in the training data or reality.
* Causes include limitations or errors in training data, overfitting, vague or ambiguous inputs, and the lack of real-world understanding or fact-verification ability.
* It is like "seeing" or creating something imaginary, similar to how humans sometimes see patterns that do not exist.
* Hallucinations can take forms such as contradicting the input, contradicting themselves, or contradicting known facts.
* This problem undermines user trust and the reliability of LLMs, sometimes leading to significant consequences.
* This phenomenon is a metaphorical use of the term "hallucination" to describe AI generating nonsensical or inaccurate responses that don't match training or facts.​

---
![Hallucinations](assets/Hallucination_1.png)

---

**Mitigation # 01**
* Use model interrogation to discover model's knowledge, and programmatically augment its training dataset with knowledge-based refusals in cases where the model doesn't know, for example:
---
![Mitigation # 01](assets/Hallucination_2.png)

---
**Mitigation # 02**

* The model is equipped with the ability to **initiate web searches** when it lacks sufficient knowledge to answer a question confidently.
* This is achieved by defining **special control tokens** — `<SEARCH_START>` and `<SEARCH_END>` — which act as a protocol indicating when the model wants to perform a search.
* When the model determines that it doesn’t know an answer, it can emit:
    - `<SEARCH_START>` followed by a query, e.g., *“Who is Orson Kovacs?”*, and then
    - `<SEARCH_END>` to signal the end of the query.
* During inference, when the system detects <SEARCH_END>, it **pauses token generation** and executes an external search (e.g., via Bing or Google) using the emitted query.
* The retrieved text from the search results is then inserted back into the model’s context, represented by placeholder tokens such as `[...]`.
* This inserted text becomes part of the **context window**, which functions as the model’s **working memory** — data here is directly accessible to the neural network for reasoning.
* When token generation resumes, the model can **reference and incorporate** this newly retrieved information in its response.
* Because the base (pretrained) model already possesses an inherent understanding of how search queries work, it can naturally generate effective and contextually relevant search prompts.

---
![Mitigation # 02](assets/Hallucination_3.png)

---

**Vague Collection VS Working Memory**

* **Knowledge in the parameters == Vague recollection (e.g. of something you read 1 month ago)**
    - The information stored in the *model’s parameters* (i.e., weights) represents what the model **learned during pretraining.**
    - This knowledge is **implicit, fuzzy, and generalized** — similar to how a human might vaguely remember something they read a long time ago.
    - Because it’s encoded statistically across billions of parameters, it cannot recall exact details or sources, which often leads to **hallucinations** when the model “fills in the gaps.”
    - Example: The model might recall that “Orson Kovacs is a scientist,” but not accurately remember which field he belongs to or the exact facts.
* **Knowledge in the tokens of the context window == Working memory**
    - The *context window* (the tokens currently being processed in a conversation or prompt) acts as the model’s **short-term or working memory**.
    - Information here is **explicit, precise, and immediately accessible** — the model can directly refer back to it while generating new tokens.
    - It’s similar to how a human keeps information temporarily in mind while reasoning or speaking.
    - Example: If the retrieved search text includes “Orson Kovacs is an astrophysicist from MIT,” the model can now use that exact phrase reliably in its next response.

* `Parameters` = **Long-term, fuzzy recollection** (broad understanding, not detail-accurate)
* `Context tokens` = **Short-term, precise working memory** (temporary but exact information)

##### **Knowledge of Self**

* The LLM has no knowledge of self "out of the box"
* If you do nothing, it will probably think it is ChatGPT, developed by OpenAI.
* You can program a "sense of self" in ~2 ways:
    - Hardcoded conversations around these topics in the Conversations data (see below picture)
    - "System message" that reminds the model at the beginning of every conversation about its identity.

---
![Hardcoded Conversations](assets/know%20yourself%20hardcoded.png "Hardcoded Conversations")

---

##### **Model Need Tokens to `Think`**
* Suppose we are building out conversation to enter into our training set of conversation, so we are training model on below problem

---
![Model Need Tokens to Think](assets/model%20need%20tokens%20to%20think.png, "Model Need Tokens to Think")

---
**Prompt Construction Matters:**
* When creating training examples, how an answer is structured significantly affects model performance.
* Even if two answers are correct, one may train the model better if it reflects *step-by-step reasoning* rather than giving the answer immediately.

**Finite Computation per Token:**
* Each token generation involves a **fixed, limited amount of computation** (due to a finite number of transformer layers).
* Therefore, a model cannot perform complex reasoning or multi-step calculations in a *single token*.

**Distributed Reasoning:**
* Good training data should encourage models to **spread reasoning across tokens**.
* Example:
    - Bad answer → instantly outputs “The answer is $3.”
    - Good answer → reasons step by step (“Oranges cost $4 → total $13 – $4 = $9 → each apple costs $3”).
* This teaches the model to reason incrementally and use prior context (“working memory”) effectively.

**Demonstration:**
* When forced to output an answer in a *single token*, the model can solve only very simple problems.
* As numbers or complexity increase, it fails — showing it can’t perform all computation in one forward pass.

**Practical Solution — Tool Use:**
* Instead of relying on “mental arithmetic” (internal computation), let the model **use external tools**, e.g., a **code interpreter (Python)**.
* Using tools allows verification of intermediate steps and produces more reliable results.
* Example: the model can write and run Python code to compute results instead of reasoning internally.

**Counting Example:**
* Models struggle with counting (e.g., number of dots) because it requires too much computation per token.
* By delegating the task to a code tool (`.count()` function in Python), results become accurate — showing that **offloading structured tasks to tools** is better.
* So, the python interpreter is doing the counting, it's not the mental arithmetic doing it.

**Core Insight:**
* **Models need tokens to think** — distribute reasoning over multiple tokens.
* **Prefer tool use** for precise or computation-heavy tasks (math, counting, logic).
* **Avoid forcing models to “think” too much in one token**, as that exceeds their per-token computational capacity.

---
![Model Need Token to Think](assets/model%20need%20tokens%20to%20think2.png "Model Need Tokens to Think")

---

##### **Tokenization revisited: Models struggle with spelling**
* **LLMs are not very good with spelling-related tasks.**
* The reason ties back to **tokenization** — models process tokens, not characters.
* Tokens are small chunks of text (not necessarily single letters).
* Because of this, LLMs don’t “see” words as a sequence of letters like humans do.

* **Example: Character Indexing Task**
- Example task: Print every third character of the string “ubiquitous,” starting from the first.
- Expected output (human logic): `uqs`
- Model output: **Incorrect** — because it doesn’t truly process at the character level.
- “ubiquitous” = 3 tokens for the model, not individual letters.
- Humans can easily visualize and index letters; models cannot.

* **Why Tokens Exist**
- Tokens are used for **efficiency** — fewer elements for models to handle.
- However, this causes **limitations in spelling and fine-grained text manipulation.**
- Some researchers want character-level or byte-level models,
    * But these would create very long sequences,
    * And current architectures don’t handle those efficiently yet.

* **Using Tools to Compensate**
- Since spelling is not a strong suit, we can tell the model to **use external tools** like code interpreters.
- Example: “Use code” with Python to manipulate strings correctly.
- When run in Python:
    * It correctly outputs `"uqs"` for every third character in “ubiquitous.”
- This works because Python processes at the **character level**, not token level.

* **Famous Example: “How many R’s in Strawberry?”**
- This question went viral because models used to get it wrong.
- Many state-of-the-art LLMs claimed there were 2 Rs, but there are actually 3.
- Shows two weaknesses combined:
    1) Poor **character-level perception** (due to tokenization).
    2) Weak **counting ability.**
- Newer models (e.g., OpenAI’s) now get it right — possibly due to **fine-tuning** or **even hardcoded corrections.**

* **Takeaway**
- LLMs struggle with:
    * Spelling-related or **character-specific tasks**
    * **Counting** characters or letters
- Always be cautious with such tasks in real applications.
- Use **external tools or code execution** for reliable results.
- The goal here isn’t to show all flaws — just to **raise awareness** of common pitfalls when using LLMs in practice.

##### **Jagged Intelligence — Inconsistent Model Behavior**
- LLMs show **“jagged edges”** — sharp inconsistencies or unpredictable failures.
- They can solve **complex, PhD-level problems**, yet fail at **simple ones**.
- Example: Model claims **9.11 > 9.9**, sometimes flips its answer, not consistent.
- These mistakes are **not reliably reproducible** — results vary per run.
- Researchers found that when analyzing internal activations:
    * Certain neurons **light up similarly to patterns from Bible verse references** (e.g., “John 9:11”).
    * The model might misinterpret “9.11” as a **verse marker**, not a number.
- Shows that **contextual associations** can override logical reasoning.

**Conclusion:**
- Treat LLMs as **stochastic, fallible tools**, not infallible systems.
- Use them thoughtfully — **verify outputs**, don’t blindly copy results.

Now that the model can imitate a helpful human, the next stage teaches it how to discover solutions and "think" for itself by solving practice problems.

--------------------------------------------------------------------------------

### **3. Stage 3: Teaching the AI to "Think" — Reinforcement Learning (RL)**

* **Reinforcement learning (RL)** is the third major stage of LLM training, following:
    1) **Pre-training** (building general knowledge)
    2) **Supervised Fine-Tuning (SFT)** (imitating expert responses)
* Though part of “post-training,” RL is distinct and handled by a separate team inside companies like OpenAI.

* **Analogy: Training Like Going to School**
- Think of training stages as steps in education:
    1) Pre-training → Reading textbooks, gaining background knowledge (exposition).
    2) SFT → Studying worked examples by experts (learning from ideal solutions).
    3) Reinforcement Learning → Solving practice problems without seeing the full solution.

* **What RL Does**
- In RL, the model:
    * Gets a **problem statement** and the **final answer** (like an answer key).
    * Must **experiment** to find the best solution path.
    * Learns by **trial and feedback**, not imitation.
- This mirrors how humans **practice and refine** skills after learning theory.

* **Key Idea**
- RL helps models **practice decision-making, self-correct, and improve alignment.**
- It builds on the foundation of pre-training (knowledge) and SFT (expert imitation) to develop **independent reasoning** and **behavioral refinement.**

---
![Reinforcement Learning](assets/RL-1.png, "Reinforcement Learning")

---

#### **3.1. RL in Action: Guess and Check for Verifiable Problems**

This final stage elevates the model from an expert imitator to a genuine problem-solver. This is where it does the Practice Problems at the end of the chapter. It's not just imitating a solution anymore; it's discovering for itself how to arrive at the correct answer.

* **Setup Problem**
Problem: “Emily buys 3 apples and 2 oranges for $13; oranges cost $2 each — find apple cost.”
Multiple valid solution paths exist, all leading to $3 per apple — some short and efficient, others long and redundant.

* **Key Challenge**
- Humans can’t easily label which reasoning path is *best*.
- Different solution styles (equations, reasoning steps, direct answers) can all work — but:
    * Too-short paths demand high computation per token → more errors.
    * Too-long paths waste tokens and slow inference.
- What’s easy for humans may be hard for LLMs, and vice versa — so we can’t hand-design the “ideal” reasoning sequence.

* **Why Reinforcement Learning (RL) Is Needed**
- The model must **discover for itself** which token sequences work best.
- RL enables the model to:
    1) Generate **many possible solutions** (sometimes thousands per prompt).
    2) **Evaluate** which ones reach the correct final answer.
    3) **Reinforce** the successful token paths that lead to correct results (“green”) and **discourage** failed ones (“red”).
- This is essentially large-scale **“guess and check.”**
- RL works best for **verifiable tasks** like math, coding, and logic—where correctness can be automatically confirmed.

* **How the Process Works**
1) Model receives a problem.
2) Generates multiple candidate solutions.
3) Automated system checks which reached the correct answer.
4) Model is updated to favor the reasoning paths that succeeded.
5) Repeated across tens of thousands of prompts → model self-improves.
- This process refines the model’s internal logic, improving both **accuracy** and **robustness.**

* **Role of Supervised Fine-Tuning (SFT)**
- **SFT:** Teaches by example — the model imitates expert demonstrations.
- **RL:** Lets the model practice independently, discovering what reasoning patterns work best.
- Together:
    > SFT = imitation | RL = self-discovery

![Guess and Check](assets/RL-2.png "Guess and Check")

#### **3.2. The Emergent Skill of “Thinking”**
A fascinating byproduct of RL is the model’s emergence of **step-by-step reasoning** or **“Chains of Thought.”**
No human explicitly programs this; the model *learns* that breaking problems down, backtracking, and re-evaluating steps **improves its success rate.**
It essentially learns to “think out loud” — mirroring human internal reasoning.

* **Analogy to Human Learning**

| Stage | Human Equivalent | Model Process |
|--------|------------------|----------------|
| **Pre-training** | Reading textbooks | Learning general knowledge |
| **Supervised Fine-Tuning** | Studying worked examples | Imitating expert solutions |
| **Reinforcement Learning** | Doing practice problems | Discovering best reasoning paths |

* **Summary Insight**
- LLM training mirrors human learning: **read → imitate → practice.**
- Reinforcement Learning is where models **truly internalize** problem-solving — not by copying, but by discovering what reasoning works best for themselves.
- The result: a model that learns to think, improving in accuracy, efficiency, and reasoning depth over time.

https://youtu.be/7xTGNNLPyMI?t=8867











Now that we understand how the model is built, we can better understand its unique behavior and how to interact with it effectively.


--------------------------------------------------------------------------------


4. Understanding Your AI Companion: Key "Psychological" Quirks

AI models don't think like humans. Their capabilities are not a solid block but more like Swiss cheese—incredibly powerful in most areas, but with seemingly random holes. Understanding their unique cognitive quirks can help you get better results and make sense of their occasional strange behavior.

4.1. The Truth About Hallucinations

Hallucinations—when an AI confidently states incorrect information—happen because the model is built to imitate the confident style of its training data. But how do you teach it to say "I don't know"?

The key insight is to connect the model's internal state to its verbal output. You can imagine that somewhere inside the network, a neuron lights up when the model is uncertain. However, by default, that neuron isn't wired to the words "I don't know." The model will simply make its best guess in a confident tone, just like its training examples.

To fix this, we explicitly create training examples where the correct answer is to admit uncertainty. This teaches the model to connect its internal state of "not knowing" to the token sequence for "I'm sorry, I don't have that information." This wiring is a crucial step in making the model more truthful.

4.2. Working Memory vs. Long-Term Memory

An LLM has two distinct types of knowledge. Understanding this is key to getting high-quality outputs.

Memory Type	Analogy	Description
Parameters	Vague, Long-Term Recollection	Knowledge learned during pre-training and stored in the model's weights. Like something you read a month ago; the details might be fuzzy.
Context Window	Active, Working Memory	The text currently in your conversation prompt. Information here is directly accessible, in-focus, and not a vague recollection.

Practical Takeaway: For the highest quality results on a specific topic, paste the relevant information directly into the prompt. This places it in the model's "working memory," allowing for far more accurate and detailed responses.

4.3. Why AIs Can Struggle with "Simple" Tasks

A core reason for many strange failures is simple: models need tokens to think.

Complex calculations cannot be done in a single computational leap. The reasoning must be spread out over many tokens. For example, if you ask a model "Emily buys 3 apples and 2 oranges..." and demand the answer in a single token, it might succeed. But if you make it "Emily buys 23 apples and 17 oranges..." with more complex numbers, it will likely fail. It needs the "space" of multiple tokens to write out the intermediate steps and arrive at the correct answer.

Because the model sees the world as these tokens, not as individual letters, it also struggles with tasks that are trivial for humans, like counting the characters in a word or accurately reversing a string. It doesn't have direct access to letters—only to the token representations it was trained on.


--------------------------------------------------------------------------------


5. Conclusion: From Internet Simulator to Thinking Partner

The journey to create an AI like ChatGPT is a methodical, three-stage process, much like learning from a textbook. It begins with pre-training, where a base model reads the "Exposition" of the internet to gain knowledge. It is then transformed through supervised fine-tuning, where it studies "Worked Examples" from human experts to become a helpful conversationalist. Finally, reinforcement learning allows it to do the "Practice Problems," discovering for itself how to reason and solve complex challenges.

These models are not magical beings. They are complex systems whose knowledge, personality, and unique cognitive abilities are shaped, step-by-step, by the data they train on. Understanding this process reveals not just how they work, but how we can work with them as increasingly powerful partners in thought.


**Links of this video**
* [ChatGPT](https://chatgpt.com/)
* [FineWeb (pretraining dataset)](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1)
* [Tiktokenizer](https://tiktokenizer.vercel.app/)
* [Transformer Neural Net 3D visualizer](https://bbycroft.net/llm)
* [llm.c Let's Reproduce GPT-2](https://github.com/karpathy/llm.c/discussions/677)
* [Llama 3 paper from Meta](https://arxiv.org/abs/2407.21783)
* [Hyperbolic, for inference of base model](https://app.hyperbolic.xyz/)
* [InstructGPT paper on SFT](https://arxiv.org/abs/2203.02155)
* [HuggingFace inference playground](https://huggingface.co/spaces/huggingface/inference-playground)
* [DeepSeek-R1 paper](https://arxiv.org/abs/2501.12948)
* [TogetherAI Playground for open model inference](https://api.together.xyz/playground)
* [AlphaGo paper (PDF)](https://discovery.ucl.ac.uk/id/eprint/10045895/1/agz_unformatted_nature.pdf)
* [AlphaGo Move 37 video](https://www.youtube.com/watch?v=HT-UZkiOLv8)
* [LM Arena for model rankings](https://lmarena.ai/)
* [AI News Newsletter](https://buttondown.com/ainews)
* [LMStudio for local inference](https://lmstudio.ai/)
* [The visualization UI I was using in the video](https://excalidraw.com/)
* [The specific file of Excalidraw we built up](https://drive.google.com/file/d/1EZh5hNDzxMMy05uLhVryk061QYQGTxiN/view)