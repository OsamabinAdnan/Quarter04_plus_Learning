## **Structure of LLMs**

At a high level, an LLM (like GPT-5 or Gemini) is built through a series of structured stages — from collecting data to training and fine-tuning — that give it the ability to **understand, generate, and reason with human language.**

---

### **Stage 1: Pre-Processing Stage**

* Preprocessing stage will always happens once, it is not dynamic, it statics
* Check this video from 3Blue1Brown for brief about LLMs [LLMs explain briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs)

#### **1) Pre-training (Data Collection from multiple sources)**

* The process starts by gathering huge amounts of text data — books, articles, websites, code, etc.
* **The goal:** give the model a broad understanding of language, facts, and patterns i.e., `Structuring the data`.


    ##### **a) Scraping the Code (HTML, CSS, JS)**

    * Data is collecting in the form of raw HTML from the internet, collector has raw algorithm which make possible to collect data from the internet.
    * According to some article, writer said in it, to prepare simple base model we have to roughly scrap 2.7 Billion webpages.

    ##### **b) Filtering of Data (Raw Text)**

    * After scraping, we apply filter on data.
    * Filtering process involve cleaning of data, sending raw text in data set etc.
    * As a result, we get raw text data.

#### **2) Tokenization**

* Converting the raw text into the tokens which we feed as a data to `neural networks`.
* We assign some random digits/number to that raw data, this process is called `mapping of tokens` (tokens means words, sub-words, characters)

#### **3) Mathematical Expression (numeric value)**

* Raw text is cleaned, filtered, and `tokenized` (broken into small chunks called tokens).
* All junks like HTML tags, duplicates, or harmful content have been removed.
* Now convert every token into a numeric format (mathematical expression sequence) that computer can understand.
* Bits/Bytes (Computer Language) or Binary Language.
* Tokenized value of `'hello'` depends on model, like in OpenAI model value of hello is different than Gemini model, according to sir the value is hello is `189065`
* Now we will save all data in big dataset

### **Stage 2: Post-Training Stage**

* `Neural Network` means predicting the next token based on data
* Before 2017, to analyze the user query and answer it, the mathematical formula applied to whole dataset in order to get first word of reply then this formula will run again to get next word, this took lot of time to answer a simple query.
* `Attention all you need` article said to replace above (time consuming) network from `transfomer architecture`, it said you should predict next token simultaneously i.e., run billion of queries at a time on dataset and bring the answer from it and show to user.