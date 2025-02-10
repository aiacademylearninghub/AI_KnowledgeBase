# LangChain vs LlamaIndex

|![image](images/framework1.png)**Features**|![image](images/framework2.png)**LangChain**|![image](images/framework3.png)**LlamaIndex**|
|--|--|--|
|Wikipedia Page|[LangChain - Wikipedia](https://en.wikipedia.org/wiki/LangChain)|No Wikipedia page for LlamaIndex
|Github Page|[LangChain - Github](https://github.com/langchain-ai/langchain)|[LlamaIndex - Github](https://github.com/run-llama/llama_index)
|Accessibility|Open-Source|Open-Source|
|First Version Released|Oct-25 2022|Nov-13 2022|
|Latest Version Released|Jul-19 2024|Jul-23 2024|
|About|LangChain is a framework for developing applications powered by large language models (LLMs). |LlamaIndex is a framework for building context-augmented generative AI applications with LLMs. |
|UseCases| Question-Answering(RAG), Chatbots, Structured Data Extraction, Agents, Multi-Modal Applications, Fine-Tuning.|SQL, Chatbots, Extraction, Query analysis, Q&A with RAG, Tool use, Interacting with APIs, Tabular Question Answering, Graphs, Summarization, Agent Simulations, Autonomous Agents, Code Understanding, Audio/Video Structured Extraction|
|No of LLM Integration|90 [LangChain - LLM Integrations](https://python.langchain.com/v0.2/docs/integrations/llms/)|54 [LlamaIndex - LLM Integrations](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/modules/)|
|No of Vector Store Integration|102 [LangChain - Vector Store Integration](https://python.langchain.com/v0.2/docs/integrations/vectorstores/)|45 [LlamaIndex - Vector Store Integration](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/)|
|Cost and Token Tracking|[Cost Analysis and tracking token](https://python.langchain.com/v0.1/docs/modules/model_io/llms/token_usage_tracking/) usage is available. We can also use [FakeLM](https://js.langchain.com/v0.1/docs/integrations/llms/fake/) to mock the LLM calls and simulate what would happen if LLM responded. By this way we can predict the token usage and cost analysis.|[Cost Analysis and tracking token](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/) usage is available. We can also use [MockLLM](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/usage_pattern/) to predict token usage of LLM calls and also predict the token usage of embedding calls.
|Data Connectors|Use document loaders to load data from a source as Document's. A Document is a piece of text and associated metadata. For example, there are document loaders for loading a simple .txt file, for loading the text contents of any web page, or even for loading a transcript of a YouTube video. There are totally [168](https://python.langchain.com/v0.1/docs/integrations/document_loaders/) document loaders are provided by langchain|A data connector (aka Reader) ingest data from different data sources and data formats into a simple Document representation (text and simple metadata). There are totally [201](https://llamahub.ai/?tab=readers) data connectors are provided by llamaindex|



# **Evaluation**
## **[LangChain:](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/)**

LangChain offers various types of evaluators to help you measure performance and integrity on diverse data. Here are some of the types of evaluators LangChain offers 
1. **String Evaluators:** These evaluators assess the predicted string for a given input, usually comparing it against a reference string. Some of the available string evaluators are Criteria Evaluation, Custom String Evaluator, Embedding Distance, Exact Match, JSON Evaluators, Regex Match, Scoring Evaluator, String Distance.
2. **Trajectory Evaluators:** These are used to evaluate the entire trajectory of agent actions. Some of the available trajectory evaluators are Custom Trajectory Evaluator, Agent Trajectory.
3. **Comparison Evaluators:** These evaluators are designed to compare predictions from two runs on a common input. Some of the available Comparison Evaluators are Pairwise string Comparison, Pairwise embedding distance, custom pairwise evaluator.
4. **LangSmith Evaluation:** LangSmith provides an integrated evaluation and tracing framework that allows us to check for regressions, compare systems, and easily identify and fix any sources of errors and performance issues. 
5. **LangChain benchmarks:** AI application quality is a function both of the LLM we choose and the prompting and data retrieval strategies we employ to provide the model context. LangChain published a number of benchmark tasks within the LangChain Benchmarks package to grade different LLM systems. Example Agent tool use, Retrieval-augmented question-answering, structured extraction.
## **[LlamaIndex:](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/evaluation/)**

LlamaIndex is meant to connect the data to LLM applications. LlamaIndex offers key modules to measure the quality of generated results also offers to measure retrieval quality. 
1. **Response Evaluation:** Does the response match the retrieved context? Does it also match the query? does it match the reference answer or guidelines? LlamaIndex offers LLM-based evaluation modules to measure the quality of the results. The available evaluation modules are in the following forms Correctness, Semantic Similarity, Faithfulness, Context Relevancy, answer Relevancy, Guideline Adherence.
2. **Retrieval Evaluation:** Are the retrieved sources relevant to the query? Given a dataset of questions and ground-truth rankings, we can evaluate retrievers using ranking metrics like mean-reciprocal rank(MRR), hit rate, precision and more. The core retrieval evaluation steps revolve around Dataset generation (Given an unstructured text corpus, synthetically generate (question, context) pairs), Retrieval evaluation (Given a retriever and a set of questions, evaluate retrieved results using ranking metrics).
3. **Integrations:** LlamaIndex also integrated with community evaluation tools like UpTrain, Tonic Validate(Includes Web UI for visualizing results), DeepEval, Ragas, RAGChecker.


## **Agents**

### **LangChain:**
The core idea of agents is to use a language model to choose a sequence of actions to take. In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.






