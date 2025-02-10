
### How Agents work?

  1. Large Language Model (LLM) agents are essentially systems designed to carry out specific tasks by interacting with the user, the environment, or other models. These agents are **built on top of pre-trained language models** like GPT-4 or similar.
  
  2.  What makes LLM agents unique is that they are **designed to perform actions beyond generating text**, they can integrate with external tools, APIs, or databases to complete complex workflows.

  3. *For example*, if a user asks an LLM to book a flight, it would not understand how to complete that task, this is where agents come in. They can guide the model to invoke a flight-booking API or handle other external tasks required to complete the request.

  4. These agents often use **predefined behaviors, workflows, or rules to handle tasks**. While the underlying LLM provides language capabilities, the agent layer introduces logic and decision-making abilities to guide the language model towards achieving a particular goal.

  5. The agent essentially knows when and how to invoke certain actions, either by using a pre-built tool or by relying on language output alone.
   
:::tip
1. Learn more about [LLM Agent](https://medium.com/@aydinKerem/what-is-an-llm-agent-and-how-does-it-work-1d4d9e4381ca)
:::

### How It Differs from RAG and Fine-Tuning

1. Fine-tuning customizes an LLM by training particular datasets, which allows the model to align with specific tasks or industries.
2. RAG, on the other hand, enhances a model's ability to retrieve and generate answers by pulling information from external sources, like a document database, to improve accuracy.
3. In contrast, LLM agents are more action-oriented. Agents focus on executing tasks by interacting with external tools or APIs.
4. Think of RAG and fine-tuning as improving the brain of the system, while agents are the hands that can carry out real-world tasks.

### Use Case

1. Imagine an e-commerce chatbot that helps customers with purchases. Without an agent, the chatbot can only give general information about products and services.
2. However, with an LLM agent integrated, the chatbot could check product availability, initiate a purchase, process payment, and schedule a delivery by interacting with external APIs for inventory, payment gateways, and logistics.
3. It's not just about having the language skills to chat with the customer but also executing a series of tasks to fulfill the customer’s request end-to-end.
