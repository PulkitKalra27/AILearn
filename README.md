# Learning AI with Python

## Generative AI

### What is Generative AI?

Generative AI refers to AI systems that can **generate new content** such as text, images, audio, video, or code based on patterns learned from existing data.

A useful way to understand Generative AI is from two perspectives:

### 1. Foundation Model — User Perspective

From a user's perspective, the focus is on **building applications using existing foundation models**.

Topics include:

* Building basic LLM applications
* Using LLM APIs
* LangChain
* Hugging Face
* Ollama
* Prompt Engineering
* RAG (Retrieval-Augmented Generation)
* Fine-tuning
* Agents
* LLMOps
* Miscellaneous GenAI concepts

### 2. Foundation Model — Builder Perspective

From a builder perspective, the focus is on **how foundation models are created, trained, evaluated, and deployed**.

Topics include:

* Transformer architecture
* Types of Transformers
* Pre-training
* Optimization
* Fine-tuning
* Evaluation
* Deployment

---

# Transformer Architecture

Transformers are the foundation of many modern Generative AI models.

## Types of Transformers

The major Transformer architectures are:

1. **Encoder**
2. **Decoder**
3. **Encoder-Decoder**

---

## Word Embeddings

### Static Embeddings

A **static embedding** represents a word as a fixed numerical vector.

The same word generally has the same representation regardless of the sentence in which it appears.

For example:

```text
bank → [0.21, -0.43, 0.67, ...]
```

The representation does not change based on context.

---

## Contextual Embeddings

A **contextual embedding** represents a word based on the surrounding context.

The same word can have different representations depending on the sentence.

For example:

```text
I deposited money in the bank.

I sat near the river bank.
```

The word **"bank"** has different meanings in these two sentences.

Contextual embeddings allow the model to capture these differences.

> **Simplified idea:** Static embedding + surrounding context → Contextual representation

---

# Encoder

The encoder takes the input sentence and creates **contextual representations** of the tokens.

For example:

```text
Input Sentence
      ↓
Tokenization
      ↓
Token Embeddings + Positional Information
      ↓
Self-Attention
      ↓
Feed Forward Network
      ↓
Contextual Representations
```

A well-known encoder-based model is **BERT**.

> Note: BERT's hidden size is commonly **768** for BERT-base. It is not the number of parameters.

---

# Decoder

A decoder-based Transformer generates output **token by token**.

For example:

```text
Input: The weather today is

Prediction:
The → weather → today → is → sunny
```

The decoder predicts the next token based on the tokens that came before it.

**GPT** is an example of a decoder-only Transformer architecture.

> GPT models can have different hidden sizes and parameter counts depending on the specific model version.

---

# Tokenization and Positional Embeddings

Before a Transformer processes text, the text goes through several stages.

### Step 1: Tokenization

The input text is divided into tokens.

```text
"I love Python"

        ↓

["I", "love", "Python"]
```

### Step 2: Token IDs

Each token is converted into an integer ID.

```text
["I", "love", "Python"]

        ↓

[101, 2057, 18750]
```

*The actual IDs depend on the tokenizer.*

### Step 3: Token Embeddings

Each token ID is mapped to a numerical vector.

```text
Token ID
   ↓
Embedding Layer
   ↓
Vector Representation
```

### Step 4: Positional Information

Transformers need information about the **position/order of tokens**.

For example:

```text
I love Python
```

The model needs to distinguish:

```text
I     → position 1
love  → position 2
Python → position 3
```

Token embeddings and positional information are then used by the Transformer layers.

---

# Multi-Head Attention

**Multi-Head Attention** allows the model to focus on different aspects or relationships between tokens simultaneously.

Different attention heads can learn different types of relationships, such as:

* Semantic relationships
* Syntactic relationships
* Positional relationships
* Long-range dependencies

This allows the model to build a richer contextual understanding of each token.

---

# Feed Forward Network (FFN)

The **Feed Forward Network** applies transformations to each token representation independently.

It uses nonlinear transformations to help the model learn:

* Complex patterns
* Higher-order features
* Nonlinear relationships

A simplified Transformer block can be represented as:

```text
Input
  ↓
Self-Attention
  ↓
Feed Forward Network
  ↓
Output
```

---

# LangChain

## What is LangChain?

**LangChain** is an open-source framework that helps developers build applications powered by Large Language Models (LLMs).

It provides:

* Modular components
* Integrations with different AI models and tools
* Components for building LLM applications
* Tools for creating complex AI workflows

## Why LangChain?

LangChain is useful because it provides integrations with many components of the Generative AI ecosystem.

It can be used with:

* LLM APIs
* Hugging Face
* Ollama
* Prompt Engineering
* RAG
* Fine-tuning workflows
* Agents
* External tools and data sources

Using LangChain provides a more holistic way to learn and build Generative AI applications.

---

# Semantic Search

**Semantic Search** searches based on the **meaning of the query**, rather than only matching exact keywords.

The general process is:

```text
Documents
    ↓
Create Embeddings
    ↓
Store Embeddings as Vectors
    ↓
User Query
    ↓
Create Query Embedding
    ↓
Compare Query Vector with Document Vectors
    ↓
Retrieve Most Similar Documents
```

For example, suppose we have:

```text
Document 1:
"How can I reset my password?"

Document 2:
"Today's weather is sunny."

Query:
"I forgot my password. How can I recover it?"
```

Even though the words are not exactly the same, semantic search can identify **Document 1** because the meaning is similar.

### What is a Vector?

A vector is a numerical representation of information.

For example:

```text
"Python is a programming language"

        ↓

[0.12, -0.45, 0.78, 0.31, ...]
```

The vector captures semantic characteristics of the text.

---

# Additional GenAI Frameworks

Other frameworks worth learning include:

* **LlamaIndex**
* **Haystack**

---

# Resources

### Transformer / Generative AI Resources

* [YouTube — Generative AI / Transformers](https://www.youtube.com/watch?v=nlz9j-r0U9U&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=3)
* [YouTube — Generative AI](https://www.youtube.com/watch?v=ZhAz268Hdpw)

---

# 08/09/2026

# Context-Aware Text Generation

**Context-aware text generation** is a method where the model uses surrounding information to produce more relevant and accurate responses.

For example:

```text
User:
Who is Narendra Modi?

User:
What is his age?
```

The second question requires the context from the first question to understand who **"his"** refers to.

---

# LangChain Components

LangChain provides several important components for building LLM applications.

## 1. Models

The **Model** component provides an interface through which applications can interact with AI models.

For example, an application can interact with models from different providers such as:

* OpenAI
* Google Gemini
* Anthropic Claude
* Hugging Face
* Ollama

The goal is to provide a common interface so that switching between models requires relatively small changes.

### Two Important Model Types

LangChain primarily works with:

1. **Language Models**
2. **Embedding Models**

### Language Models

Language models work with text and generate text.

```text
Text → Language Model → Text
```

### Embedding Models

Embedding models convert text into numerical vectors.

```text
Text → Embedding Model → Vector
```

These vectors are useful for applications such as:

* Semantic Search
* RAG
* Similarity Search
* Recommendation Systems

---

# 2. Prompts

A **prompt** is the input or instruction given to an LLM.

LangChain provides prompt-related components for creating dynamic and reusable prompts.

---

## PromptTemplate

A `PromptTemplate` allows us to create reusable prompts using placeholders.

For example:

```text
Tell me about {topic} in {language}.
```

The values can be supplied dynamically.

```python
prompt.format(
    topic="Artificial Intelligence",
    language="Hindi"
)
```

---

# Types of Prompting

## Dynamic / Reusable Prompts

Prompts can contain placeholders that are filled dynamically.

Example:

```text
Translate the following text into {language}:

{text}
```

---

## Role-Based Prompting

We can assign different roles to messages.

Common roles include:

* System
* User
* Assistant

For example:

```text
System:
You are a helpful Python tutor.

User:
Explain decorators in Python.
```

---

# Few-Shot Prompting

**Few-shot prompting** means giving the LLM a few examples before asking it to perform a task.

For example, we want to classify customer support tickets.

### Examples

```python
examples = [
    {
        "input": "I was charged twice for my subscription this month.",
        "output": "Billing Issue"
    },
    {
        "input": "The app crashes every time I try to log in.",
        "output": "Technical Problem"
    },
    {
        "input": "Can you explain how to upgrade my plan?",
        "output": "General Inquiry"
    },
    {
        "input": "I need a refund for a payment I didn't authorize.",
        "output": "Billing Issue"
    }
]
```

### Example Template

```python
example_template = """
Ticket: {input}
Category: {output}
"""
```

### Few-Shot Prompt Template

```python
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate(
        input_variables=["input", "output"],
        template=example_template
    ),
    prefix=(
        "Classify the following customer support tickets into one of "
        "the categories: 'Billing Issue', 'Technical Problem', "
        "or 'General Inquiry'.\n\n"
    ),
    suffix="\nTicket: {user_input}\nCategory:",
    input_variables=["user_input"],
)
```

The resulting prompt can look like:

```text
Classify the following customer support tickets into one of the
categories: 'Billing Issue', 'Technical Problem', or 'General Inquiry'.

Ticket: I was charged twice for my subscription this month.
Category: Billing Issue

Ticket: The app crashes every time I try to log in.
Category: Technical Problem

Ticket: Can you explain how to upgrade my plan?
Category: General Inquiry

Ticket: I need a refund for a payment I didn't authorize.
Category: Billing Issue

Ticket: I am unable to connect to the internet using your service.
Category:
```

The LLM generates the category for the final ticket.

---

# 3. Chains

**Chains** allow us to create pipelines where the output of one step becomes the input of another step.

For example:

```text
English Text
     ↓
Chain 1: Summarize
     ↓
Summary
     ↓
Chain 2: Translate
     ↓
Hindi Translation
```

Instead of manually taking the output of one operation and passing it to another, the chain manages the workflow.

Chains can also be used for more complex workflows such as:

* Sequential chains
* Parallel chains
* Conditional chains

---

# 4. Indexes

Indexes allow an LLM application to connect with **external knowledge sources**.

Examples:

* PDF documents
* Websites
* Databases
* Text files
* Other documents

A typical indexing and retrieval pipeline contains:

```text
Documents
    ↓
Document Loader
    ↓
Text Splitter
    ↓
Embedding Model
    ↓
Vector Store
    ↓
Retriever
    ↓
LLM
```

This concept is fundamental to **RAG (Retrieval-Augmented Generation)**.

---

# 5. Memory

LLM API calls are generally **stateless**.

This means that the model does not automatically remember previous interactions between separate API calls unless the application provides the conversation history or some other form of memory.

For example:

```text
User:
Who is Narendra Modi?

LLM:
Narendra Modi is ...

User:
What is his age?
```

If the second request does not include the relevant previous context, the model may not know who **"his"** refers to.

## Types of Memory

### Conversation Buffer Memory

Stores the complete conversation history and sends it back to the LLM.

```text
Message 1
Message 2
Message 3
Message 4
...
```

### Conversation Buffer Window Memory

Stores only the most recent **N** messages.

```text
Old messages → Removed / Not included

Recent messages:
Message N-2
Message N-1
Message N
```

### Summary-Based Memory

Instead of storing the complete conversation, the conversation is summarized.

```text
Long Conversation
       ↓
    Summary
       ↓
      LLM
```

### Custom Memory

Stores only important information or selected facts.

For example:

```text
User prefers Python.
User is learning Generative AI.
User prefers concise explanations.
```

---

# 6. Agents

An **Agent** is an LLM-powered system that can reason about a task and use tools to accomplish it.

A simplified agent architecture is:

```text
User Request
      ↓
     LLM
      ↓
Reasoning / Decision
      ↓
Select Tool
      ↓
Execute Tool
      ↓
Observe Result
      ↓
     LLM
      ↓
Final Answer
```

For example:

> "Book the cheapest ticket from Delhi to Bangalore on this date."

An agent could potentially:

1. Understand the request
2. Search available flights
3. Compare prices
4. Select an appropriate option
5. Perform the required action

Agents combine **LLM reasoning with tool usage**.

---

# Model Component in Detail

## What is a Language Model?

A **Language Model** is an AI system designed to process, understand, and generate natural language.

There are two commonly encountered categories in LangChain:

1. LLMs
2. Chat Models

---

## LLMs

Traditional LLM interfaces generally work with:

```text
String → String
```

Example:

```text
Input:
Explain Python decorators.

Output:
Python decorators are...
```

---

## Chat Models

Chat models are designed for conversational interactions and work with a sequence of messages.

Conceptually:

```text
Messages → Chat Model → Message
```

For example:

```text
System:
You are a helpful Python tutor.

User:
Explain decorators.

Assistant:
A decorator is...
```

Chat models are particularly useful for:

* Conversations
* Role-based prompting
* Multi-turn interactions
* Tool calling
* Agentic applications

---

# Temperature

**Temperature** controls the randomness/variability of model outputs.

The exact supported range depends on the model/provider; commonly it is around **0 to 2**.

### Low Temperature

A lower temperature generally makes the output:

* More deterministic
* More focused
* Less random

For example:

```text
temperature = 0
```

Repeated requests with the same input are more likely to produce the same or very similar responses, although exact determinism is not guaranteed by every provider.

### Higher Temperature

A higher temperature generally makes the model:

* More diverse
* More creative
* More variable

For example:

```text
temperature ≈ 2
```

The model is more likely to produce different outputs for the same input.

### Simplified View

```text
Low Temperature
      ↓
More predictable
More focused
Less variation

High Temperature
      ↓
More diverse
More creative
More variation
```

> **Important:** Temperature does not directly mean "intelligence." It mainly affects the probability distribution used when selecting the next token, and the actual behavior depends on the model and provider.

---

# Overall Generative AI Learning Roadmap

A high-level roadmap based on these topics:

```text
                    Generative AI
                         │
          ┌──────────────┴──────────────┐
          │                             │
   Builder Perspective            User Perspective
          │                             │
          ↓                             ↓
 Transformer Architecture        LLM Applications
          │                             │
          ↓                     ┌───────┼────────┐
 Encoder / Decoder               │       │        │
          │                   APIs  LangChain  Ollama
          ↓
 Pre-training                         │
          │                           ↓
          ↓                      Prompt Engineering
 Optimization                         │
          │                           ↓
          ↓                           RAG
 Fine-tuning                          │
          │                           ↓
          ↓                       Fine-tuning
 Evaluation                            │
          │                           ↓
          ↓                         Agents
 Deployment                            │
                                      ↓
                                    LLMOps
```

## Key Concepts to Remember

| Concept      | Main Purpose                                            |
| ------------ | ------------------------------------------------------- |
| Transformer  | Architecture behind many modern AI models               |
| Tokenization | Converts text into tokens                               |
| Embeddings   | Represents text as numerical vectors                    |
| Attention    | Captures relationships between tokens                   |
| Encoder      | Creates contextual representations                      |
| Decoder      | Generates tokens sequentially                           |
| Prompt       | Instructions/input given to an LLM                      |
| Chain        | Connects multiple LLM/application steps                 |
| RAG          | Connects LLMs to external knowledge                     |
| Vector Store | Stores and searches embeddings                          |
| Memory       | Maintains relevant conversational context               |
| Agent        | Uses an LLM + tools to accomplish tasks                 |
| Temperature  | Controls output variability                             |
| LangChain    | Framework for building LLM applications                 |
| LlamaIndex   | Framework focused heavily on data/knowledge integration |
| Haystack     | Framework for building search and RAG applications      |

---

# 09/09/2026

# Prompts

A **prompt** is the input instruction, question, or information given to an LLM to guide its output.

In simple terms:

```text
User Input / Instruction
          ↓
        Prompt
          ↓
         LLM
          ↓
       Output
```

The messages that we send to an LLM can be considered prompts.

For example:

```text
Explain what Python decorators are.
```

This is a prompt because it provides an instruction to the model about what we want it to generate.

---

# Types of Prompts

Prompts can broadly be thought of as:

1. **Text-based prompts**
2. **Multimodal prompts**

## Text-Based Prompts

Text-based prompts contain text as the input to the model.

Example:

```text
Explain Generative AI in simple terms.
```

---

## Multimodal Prompts

Multimodal prompts can contain different types of information, such as:

* Text
* Images
* Audio
* Video

For example:

```text
Image + Text Prompt
        ↓
       LLM
        ↓
    Description
```

A multimodal model can use multiple forms of input to understand the user's request.

---

# Importance of Prompt Changes

A small change in a prompt can sometimes produce a significantly different output from the model.

For example:

### Prompt 1

```text
Explain Python.
```

### Prompt 2

```text
Explain Python to a beginner using a simple real-world example.
```

The second prompt provides additional instructions about:

* Audience
* Explanation level
* Style
* Example requirement

Therefore, the model can produce a substantially different response.

This is one of the reasons **Prompt Engineering** is an important part of Generative AI application development.

---

# Static vs Dynamic Prompts

Prompts can also be understood as **static** or **dynamic** depending on how the application creates and sends them to the LLM.

---

## Static Prompt

A **static prompt** is predefined by the developer and remains fixed or is selected from a predefined set of prompts.

For example, a customer-support application may provide only specific operations:

```text
1. Check Order Status
2. Cancel Order
3. Request Refund
4. Contact Support
```

The developer controls what kinds of requests the application supports.

The user does not have complete freedom to construct any arbitrary prompt.

### Simplified Flow

```text
Developer
    ↓
Predefined Prompts
    ↓
User Selects / Provides Input
    ↓
LLM
    ↓
Response
```

In a static-prompt system, the **developer has more control over the available instructions and supported interactions**.

---

# Dynamic Prompt

A **dynamic prompt** is generated or modified at runtime based on user input, application data, or other variables.

A general-purpose chatbot such as ChatGPT is an example of a system where users can provide many different types of instructions.

For example:

```text
User Input
    ↓
Dynamic Prompt
    ↓
LLM
    ↓
Response
```

The user can decide what they want to ask, while the application can also add additional instructions or context.

### Static vs Dynamic

```text
STATIC

Developer
    ↓
Predefined Prompt
    ↓
LLM
    ↓
Output


DYNAMIC

User / Application Data
          ↓
    Prompt Template
          ↓
     Dynamic Prompt
          ↓
          LLM
          ↓
        Output
```

---

# Prompt Templates

A **Prompt Template** is a structured way to create prompts dynamically by inserting variables into a predefined template.

Instead of hardcoding the complete prompt every time, we define **placeholders** that can be filled at runtime.

### Without a Prompt Template

We may write:

```python
prompt = "Explain Python in English."
```

If we want to change the topic or language, we would need to construct another string.

---

### With a Prompt Template

We can define:

```text
Explain {topic} in {language}.
```

Here:

```text
{topic}
{language}
```

are placeholders.

At runtime, they can be replaced with different values.

For example:

```text
topic = Python
language = English
```

produces:

```text
Explain Python in English.
```

Another request could use:

```text
topic = Artificial Intelligence
language = Hindi
```

and produce:

```text
Explain Artificial Intelligence in Hindi.
```

---

# Why Prompt Templates?

Prompt templates make prompts:

* Reusable
* Flexible
* Easier to manage
* Easier to maintain
* Suitable for dynamic user input
* Useful for automated workflows

### General Flow

```text
Predefined Template
        ↓
   {variables}
        ↓
Runtime Values
        ↓
  Final Prompt
        ↓
       LLM
        ↓
     Response
```

---

# Prompt Template vs f-string

Python `f-strings` can also be used to dynamically construct prompts.

For example:

```python
topic = "Python"
language = "English"

prompt = f"Explain {topic} in {language}."
```

This works, but frameworks such as LangChain provide dedicated prompt-template components.

### Advantages of Prompt Templates

A prompt template provides functionality beyond simply constructing a Python string.

It can provide:

* Template validation
* Reusability
* Structured prompt construction
* Integration with the LangChain ecosystem
* Easier composition with other LangChain components

For example, LangChain can validate whether the variables expected by the template are correctly supplied.

This makes prompt templates especially useful when building larger LLM workflows.

---

# Messages in LangChain

When working with **Chat Models**, LangChain represents conversations using different message types.

The three important message types are:

1. **System Message**
2. **Human Message**
3. **AI Message**

---

# 1. System Message

A **System Message** provides instructions or behavior that guide the AI model.

For example:

```text
You are a Python expert.
```

The system message establishes the role or behavior of the assistant.

Example:

```python
SystemMessage(
    content="You are a {domain} expert."
)
```

Here `{domain}` can be dynamically provided.

For example:

```text
domain = Python
```

can produce:

```text
You are a Python expert.
```

---

# 2. Human Message

A **Human Message** represents the message or instruction provided by the user.

For example:

```text
Explain Python decorators.
```

Conceptually:

```text
Human Message
      ↓
"Explain Python decorators."
```

---

# 3. AI Message

An **AI Message** represents a response generated by the AI model.

For example:

```text
A Python decorator is a function that...
```

Conceptually:

```text
AI Message
     ↓
Generated Response
```

---

# Conversation Using Messages

A multi-turn conversation can be represented as:

```text
System Message
      ↓
"You are a Python expert."

Human Message
      ↓
"Explain decorators."

AI Message
      ↓
"A decorator is..."

Human Message
      ↓
"Give me an example."

AI Message
      ↓
"Here is an example..."
```

This message-based structure allows the model to work with conversational context.

---

# Chat Prompt Template

A **Chat Prompt Template** is used to create a structured list of messages dynamically.

Instead of creating one large string, we define the different messages and their roles.

For example:

```text
System:
You are a {domain} expert.

Human:
Explain {topic}.
```

At runtime:

```text
domain = Python
topic = decorators
```

the resulting messages become:

```text
System:
You are a Python expert.

Human:
Explain decorators.
```

---

# Chat Prompt Template Flow

```text
Chat Prompt Template
        │
        ├── System Message
        │
        ├── Human Message
        │
        ├── AI Message
        │
        └── Message Placeholder
                 ↓
          Runtime Values
                 ↓
          Final Message List
                 ↓
              Chat Model
                 ↓
             AI Response
```

---

# Model Input

A model can generally be invoked using either:

1. A **single message/input**
2. A **list of messages**

The exact interface depends on the LangChain model abstraction being used.

---

## Single Input

For a simple request, we can provide a single input.

Conceptually:

```text
Single Input
     ↓
   Model
     ↓
 Response
```

For example:

```text
"Explain Python decorators."
```

This is useful when we simply want to send a request and receive a response.

---

# List of Messages

For a conversational interaction, we can provide a list of messages.

For example:

```text
[
    System Message,
    Human Message,
    AI Message,
    Human Message
]
```

The model receives the sequence of messages and can use the conversation history as context.

### Example

```text
System:
You are a Python expert.

Human:
What is Python?

AI:
Python is a programming language...

Human:
What are decorators?
```

The list of messages represents the conversation context.

---

# Static Messages vs Dynamic Messages

When working with chat models, messages can be created directly or generated dynamically.

### Static Messages

Messages can be explicitly defined:

```text
System → You are a Python expert.
Human  → Explain decorators.
AI     → A decorator is...
```

These messages are fixed when we create them.

---

### Dynamic Messages

Messages can be generated using a **Chat Prompt Template**.

For example:

```text
System:
You are a {domain} expert.

Human:
Explain {topic}.
```

The values can be supplied at runtime.

```text
domain = Python
topic = decorators
```

Result:

```text
System:
You are a Python expert.

Human:
Explain decorators.
```

---

# Message Placeholder

A **Message Placeholder** is used inside a Chat Prompt Template to dynamically insert a list of messages at runtime.

This is especially useful when working with **chat history** or other dynamically generated messages.

For example:

```text
Chat Prompt Template

System Message
      ↓
"You are a helpful assistant."

Message Placeholder
      ↓
{chat_history}

Human Message
      ↓
{user_input}
```

At runtime, `{chat_history}` can be replaced with the actual conversation history.

---

# Message Placeholder Flow

```text
Chat Prompt Template
        │
        ├── System Message
        │
        │   "You are a helpful assistant."
        │
        ├── Message Placeholder
        │
        │   {chat_history}
        │
        └── Human Message
            {user_input}

                ↓

        Runtime Values
                ↓
        Actual Message List
                ↓
           Chat Model
                ↓
             Response
```

This becomes particularly useful when building **multi-turn conversational applications**.

---

# Complete Prompting Architecture

The concepts learned so far can be connected together:

```text
User Input
    ↓
Application
    ↓
Prompt Template
    ↓
Insert Runtime Variables
    ↓
Create Messages
    │
    ├── System Message
    ├── Human Message
    ├── AI Message
    └── Message Placeholder
    ↓
Chat Model
    ↓
LLM
    ↓
AI Response
```

---

# Key Concepts Learned

| Concept              | Purpose                                                |
| -------------------- | ------------------------------------------------------ |
| Prompt               | Input/instruction given to an LLM                      |
| Text Prompt          | Prompt containing text-based input                     |
| Multimodal Prompt    | Prompt containing multiple types of input              |
| Static Prompt        | Predefined prompt controlled by the application        |
| Dynamic Prompt       | Prompt generated or modified using runtime input       |
| Prompt Template      | Reusable structure containing dynamic variables        |
| System Message       | Defines instructions/behavior for the AI               |
| Human Message        | Represents user input                                  |
| AI Message           | Represents model-generated output                      |
| Chat Prompt Template | Dynamically creates a structured list of chat messages |
| Message Placeholder  | Dynamically inserts messages such as chat history      |
| Chat Model           | Model interface designed to work with messages         |

---

# Overall Prompt Engineering Flow

```text
                    PROMPT
                       │
             ┌─────────┴─────────┐
             │                   │
          Static              Dynamic
             │                   │
       Fixed Prompt        Prompt Template
                                 │
                                 ↓
                         Runtime Variables
                                 │
                                 ↓
                         Chat Prompt Template
                                 │
                  ┌──────────────┼──────────────┐
                  ↓              ↓              ↓
              System         Human/AI     Message Placeholder
              Message         Messages       / Chat History
                  └──────────────┼──────────────┘
                                 ↓
                             Chat Model
                                 ↓
                                LLM
                                 ↓
                              Output
```

---
