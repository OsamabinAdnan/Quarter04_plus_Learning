# **Fundamental Prompting Techniques**

## **1. Zero-Shot Prompting**
- The simplest approach—just ask directly without examples.
- You ask the model to do a task without any example.

**Examples:**

**`Example # 01`**
```bash
Classify this movie review as positive, negative, or neutral:
"The film was visually stunning but the plot felt rushed."
```

**`Example # 02`**
```bash
What does “HTTP” stand for in web addresses?
```

**`Example # 03`**
```bash
Name the capital city of Japan.
```

**`Example # 04`**
```bash
What is the meaning of the word "photosynthesis"?
```

**When to use:**

* Simple, well-defined tasks
* When the model has clear knowledge of the domain
* Quick one-off requests

## **2. One-Shot Prompting**

- Provide a single example to guide the response format.
- You give one example to show the model what kind of output you want.

**Examples:**

**`Example # 01`**
```bash
Translate English to French:

English: "Hello, how are you?"
French: "Bonjour, comment allez-vous?"

English: "Where is the library?"
French:
```

**`Example # 02`**
```bash
Example:
Review: "I loved the product, it works perfectly."
Sentiment: Positive

Review: "The delivery was late and the item was broken."
Sentiment:
```

**`Example # 03`**
```bash
Example:
News: "A new AI startup raised $10 million to develop healthcare solutions."
Summary: "A new AI company secured funding to improve healthcare."

News: "A major announcement reveals that YouTuber Subhan Kaladi, along with co-founder Shahid Ali, has launched their first startup BotBazzar under Codentic."
Summary:
```

## **3. Few-Shot Prompting**

* Provide multiple examples to establish a clear pattern.
* You give a few examples (2–5) so the model learns the pattern better.

**Examples:**

**`Example # 01`**
```bash
Convert customer feedback to structured data:

Feedback: "Great service, but food was cold"
JSON: {"service": "positive", "food": "negative", "overall": "mixed"}

Feedback: "Amazing experience, will definitely return"
JSON: {"service": "positive", "food": "positive", "overall": "positive"}

Feedback: "Terrible food and rude staff"
JSON:
```

**`Example # 02`**
```bash
Tone Conversion (Formal to Casual):
Rewrite the text in a more casual tone.

Formal: "I would like to inform you that our meeting has been postponed."
Casual: "Hey, just letting you know the meeting’s been pushed back."

Formal: "Please submit your report by the end of the week."
Casual: "Make sure to send your report by this weekend."

Formal: "We appreciate your cooperation in this matter."
Casual:
```

**`Example # 03`**
```bash
Identify the emotion in the following sentences.

Sentence: "I can’t believe I finally did it!"
Emotion: Excited

Sentence: "I miss my friends so much."
Emotion: Sad

Sentence: "You always ruin everything!"
Emotion:
```

**Best Practices**
* Use 3-5 examples for most tasks
* Include diverse examples
* Mix up the classes in classification tasks
* Ensure examples are high-quality and consistent

## **4. System Prompting**

* System prompting sets the **overall behavior, tone, and role** of the AI before any user input — it defines *how* the model should think and respond throughout the conversation.
* Set overall context and behavior guidelines.
* `System prompt = role + rules + personality`
* Used to control consistency and behavior of the model.

**Examples:**

**`Example # 01`**
```bash
You are a helpful travel guide. Provide practical, accurate information about destinations. Always include:
- Key attractions
- Local customs to be aware of
- Budget considerations
- Best time to visit

User: Tell me about visiting Tokyo.
```

**`Example # 02`**
```bash
"Always answer in a professional tone."
```

**`Example # 03`**
```bash
"Don’t give illegal or harmful advice."
```
* Sets a clear role and rules for the AI’s behavior.

## **5. Role Prompting**

* Role prompting means **telling the model to act as a specific role or persona** so its responses match that perspective or expertise.
* Assign a specific character or expertise to the AI.
* Role prompting → defines who the model is


**Examples:**

**`Example # 01`**
```bash
Act as an experienced software architect.
I need help designing a scalable web application for 1 million users.
What architecture patterns should I consider?
```

**`Example # 02`**
```bash
Act as an English teacher.
Explain the difference between “since” and “for” in simple words with two examples.
```

**`Example # 03`**
```bash
Act as a professional Python developer.
Write a simple function to calculate factorial of a number and explain it line by line.
```

**Effective roles:**

* Subject matter expert (doctor, lawyer, teacher)
* Creative roles (writer, designer, poet)
* Analytical roles (data analyst, consultant)
* Communication styles (friendly tutor, formal advisor)

## **6. Contextual Prompting**
* Contextual prompting means giving the model **extra background information or context** so it can produce more accurate and relevant answers.
* You’re basically feeding it the facts it should rely on before asking your question.
* Provide specific background information relevant to the task.
* Contextual prompting → defines what information the model should use

**Examples:**

**`Example # 01`**
```bash
Context: You're writing for a tech blog aimed at beginners who have never coded before.

Write a 200-word explanation of what an API is, using simple language and practical examples.
```

**`Example # 02`**
```bash
Here are the student’s last 3 lessons:
Variables
Loops
Functions

User: "Explain what decorators are."
```

**Inshort**
* You `add context` (data, background, examples) before the question.
* Helps the model `stay accurate and grounded.`
* Common in `RAG systems (Retrieval-Augmented Generation)` — context is retrieved from documents or databases.
