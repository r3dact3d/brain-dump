---
type: journey-note
---

# AI Journey

![ai-journey](../attachments/ai-journey.png)

![expertise](../attachments/expertise.png)

![costly_1](../attachments/costly_1.png)

![costly_2](../attachments/costly_2.png)

![run_local](../attachments/run_local.png)

SOURCE: [Red Hat Developer](https://www.youtube.com/watch?v=tZj8j3fdXy4)

Here's the content formatted in Markdown:

## AI Fundamentals: Key Takeaways

Think about:

- How to use AI to increase productivity 
- How to us AI to reduce costs and ineeficiencies 
- How to use AI to redefine business process or customer experiences
- How to use AI to completely rethink the business

This document compiles the key takeaways from each lesson of the AI Fundamentals course.

### Lesson 1: Introduction

* Part of what makes the incredible growth in AI possible is Moore's law, which states that the number of transistors in an integrated circuit doubles approximately every two years

* AI is a branch of computer science that enables machines to perform tasks that typically require human intelligence.

* Machine learning (ML) is a subcategory of AI that uses algorithms to identify patterns and make predictions within a set of data.

### Lesson 2: Predictive AI

* Predictive AI is a common type of artificial intelligence system used in business applications that predicts or forecasts outcomes based on historical data.

* Predictive AI is an integral part of many everyday activities such as conducting web searches, texting, shopping online, and engaging with video and music streaming services.

* Data science is an interdisciplinary field that leverages mathematical, statistical, and computational techniques to extract knowledge and insights from structured and unstructured data.

* Some of the tasks data scientists perform include data collection, data cleansing, model selection and training, and evaluation and validation of those models.

For a given scenario, try to **predict** the next logical outcome.

- Retail Shopping - Recommendation Engine
- Medical Imaging - Identify a disease pattern
- Manufacturing - identify flawed products on the line
- Mortgage Bank
- Airlines - Predict an engine failure from the flight logs
- Automotive - Autonomous driving

### Lesson 3: Generative AI

* The Turing test is a well-known experiment designed to assess the ability of a machine to exhibit intelligent behavior that is indistinguishable from that of a human. In the Turing test, a human evaluator reviews text from a conversation between two participants: a human and a machine. A machine is said to pass the test if the evaluator cannot reliably tell the human participant from the machine.

* Generative AI is AI technology that relies on deep learning models trained on large data sets to create new content.

* Deep learning is a specialized form of machine learning that teaches computers to process data by using an algorithm inspired by the human brain and neural networks. Deep learning teaches computers to learn through observation, imitating the way humans gain knowledge.

* Some examples of generative AI include AI-generated summaries of customer reviews on Amazon, chatbots such as ChatGPT generating content based on a text prompt, AI-generated highlight reels from sporting events, and Red Hat's KCS Solution Summaries.

  - Call Center - Interactive Chatbot
  - Marketing - Create copy for 100s of online ads 
  - Legal - Summerize 1000s of documents and identify errors 
  - Consulting - Create automated tasks from best practices
  - SW Developers - Review code and write testing
  - Procument - Review 10000s of invoices and find cost savings

* A large language model (LLM) is a type of AI program designed to understand and generate human language.

* Creating an LLM from scratch requires a tremendous amount of money, expertise, and resources. For all but a handful of organizations, creating such a model is out of reach; most organizations are likely to start with a foundation model.

* There are a variety of approaches an organization might use when working with a foundation model. One of the most popular approaches is retrieval-augmented generation (RAG), a method that involves getting better answers from a generative AI application by linking an LLM to an external resource.

* There are several issues associated with LLMs, including massive energy and resource costs, a lack of transparency with regard to how models are trained, biases in model training, hallucinations, data recency, and issues related to copyright and privacy.

## Standalone AI

Standalone AI refers to AI frameworks and platforms that can be used independently to build and deploy AI models. These tools often provide a comprehensive set of features for developing AI applications from scratch.

- [Mistral](https://console.mistral.ai/)
- [Claude](https://claude.ai/new)
- [ChatGPT]
  
  
- TensorFlow

Type: Open-source machine learning framework.\
Popularity: Widely used for deep learning and machine learning tasks.\
Open-source: Yes.

- PyTorch

Type: Open-source deep learning framework.\
Popularity: Popular among researchers and developers for its flexibility and ease of use.\
Open-source: Yes.

- IBM Watson

Type: Enterprise AI platform.\
Popularity: Used for various AI applications including natural language processing and data analytics.\
Open-source: No.

## Integrated AI

Integrated AI refers to AI services that are integrated into larger platforms or ecosystems, often provided by cloud service providers. These services are designed to be easily integrated into existing applications and workflows.

- Google AI Services

Type: Integrated AI services including vision, speech, and language processing.\
Popularity: Widely used for integrating AI capabilities into applications.\
Open-source: No.

- Amazon Web Services (AWS) AI

Type: Integrated AI services including machine learning, natural language processing, and computer vision.\
Popularity: Popular for cloud-based AI solutions.\
Open-source: No.

- Microsoft Azure AI

Type: Integrated AI services including cognitive services, machine learning, and bot services.\
Popularity: Used for a variety of AI applications in the cloud.\
Open-source: No.

## Custom AI

Custom AI refers to AI libraries and platforms that allow for the creation of custom AI models tailored to specific needs. These tools often provide flexibility and control over the AI development process.

- Hugging Face Transformers

Type: Open-source library for state-of-the-art Natural Language Processing (NLP).\
Popularity: Widely used for building custom NLP models.\
Open-source: Yes.

- Apache MXNet

Type: Open-source deep learning framework.\
Popularity: Used for building custom deep learning models.\
Open-source: Yes.

- Seldon

Type: Open-source platform for deploying machine learning models.\
Popularity: Used for deploying and managing custom AI models at scale.\
Open-source: Yes.

## Challenges for Customers

- Choosing GenAI LLM 
- Add Business Data
- Add Secure Guardrails 
- Manage Costs 

## How most customers are organized for AI today

- Data Science Team 
  - Building Models
  - Predictive AI 
  - Expensive Data Scientists
- Ambitious CIO 
  - Early GenAI Adopter
  - Center of Excellence
  - Nobody questions them
- Line of Busniess (Shadow AI)
  - Using a SaaS service
  - Using a consulting Security is a low priority
- Central IT  
  - Trying to create AI policy
  - Trying to keep up with projects
  - Understaffed

## AI Costs

- Data Scientists -> Subject Matter Experts 
- AI Hardware -> Reduced AI Hardware  
- Model Training -> Smaller Models 
- Model Tuning -> Synthetic Data Generation 
- MLOps -> Faster Time-To Production 

## Red Hat AI portfolio 
- RHEL AI
- OpenShift AI 
- Lightspeed portfolio 
- App & Developer services 

## Blinker19 AI

### Private AI

- [[Open WebUI]]
- [[Fabric]]
- [Auto Intelligence](https://github.com/r3dact3d/Auto-Intelligence)
- [[Home Lab]]
- [[RAG]]


## Todo List

- Check out [[Langchain-Gmail Toolkit]] for gmail integration


Note Created: 2025-01-06




[//begin]: # "Autogenerated link references for markdown compatibility"
[Open WebUI]: <../AI/Open WebUI.md> "Open WebUI"
[Fabric]: Fabric.md "Fabric"
[Home Lab]: <Home Lab.md> "Home Lab"
[RAG]: ../AI/RAG.md "RAG"
[//end]: # "Autogenerated link references"
