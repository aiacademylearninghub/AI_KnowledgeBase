# Why FineTuning

## **What LLM lacks?**

1. They can generate text, answer questions, and assist with creative and analytical tasks. However, LLMs have limitations, particularly when faced with domain-specific knowledge or highly specialized tasks.

### **Lack of knowledge (Treatment for Corono)**

2. Large Language Models (LLMs), despite their impressive capabilities, often face challenges when it comes to keeping their knowledge up to date. For instance, consider a situation where a user asks an LLM, such as ChatGPT, about common illnesses like coughs and colds. The model might provide a good answer, but it may lack the crucial things like COVID-19 updates. This is primarily because LLMs are trained on datasets that may not include the latest information, leading to potentially outdated or incomplete responses.

3. Once the model is trained, its knowledge base is frozen in time, and it cannot automatically incorporate new information. As a result we may receive the outdated result. Which is not accepted, particularly in the medical industry.

4. But We can solve this issue by fine tuning existing LLM. Fine-tuning is the process of taking a pre-trained LLM and further training it on a smaller, more specific dataset that contains updated or relevant information. By integrating new data, we can enhance the model's understanding and ensure it remains informed about current events and advances in various fields.

5. If we fine-tune the model using recent health guidelines, research findings, and data related to coughs and colds during the COVID-19 era, it can provide users with more accurate and relevant information. Fine-tuning allows the LLM to learn about the latest symptoms, treatment protocols, and public health recommendations, thereby bridging the gap between its static training and the dynamic nature of real-world knowledge.

### **Domain specific Knowledge (Automotive industry)**

1. Imagine a scenario where a customer service chatbot is tasked with assisting automotive technicians and parts suppliers. When a technician queries about the specifications of a particular engine component, the LLM might struggle to deliver the precise details needed. This limitation arises from the general nature of its training data, which typically lacks the in-depth knowledge specific to automotive parts.

2. For instance, if a user asks about the compatibility of a specific aftermarket exhaust system with various car models, the LLM may provide a generic overview of exhaust systems without addressing the in-deapth variations of regulations or performance metrics relevant to that particular product. Such a response can lead to confusion and dissatisfaction.

3. To address this, we can fine tune the pre-trained-llm with the data from detailed product catalogs, technical specifications, installation manuals, and customer feedback. By doing this, now the model will be more aware of domain specific information.

4. Now, we can able to create a chatbot that understands the in-depth details of various automotive components and their applications.

5. Additionally, fine-tuning allows the chatbot to remain current with the latest trends and innovations in the automotive parts industry. As new products and technologies emerge, updating the training dataset ensures that the chatbot continues to provide accurate and relevant information, keeping pace with the rapid changes in the field.

### **In-particular style of doing things(Code generation)**

1. Large Language Models (LLMs) are increasingly being utilized to assist developers in generating code; however, they often struggle to produce code that aligns with the specific standards required for a given project.

2. Consider a scenario in a Python development team that has adopted strict guidelines enforced by tools like mypy for type checking, pydocstyle for docstring conventions, and flake8 for style checks.

When a developer seeks to generate a function that processes user input, the initial output from the LLM may not meet these standards, leading to potential issues down the line. 

**Before Fine-Tuning:**

```python
def validateInput(data):
  if data.isdigit():
      return True 
  return False
```

3. In this initial output, the function name is not following any standards may be renamed as "validate_input"  also  there are no type hints, and the lack of a docstring makes it difficult for other developers to understand its purpose.

4. To address these issue, fine-tuning the LLM presents a viable solution. This process involves retraining the model on a well assembled dataset that emphasizes coding standards aligned with mypy, pydocstyle, and flake8. By providing the model with examples of well-structured code that follows these guidelines.

**After Fine-Tuning:**

```python
def validate_input(data: str) -> bool:
  """Validates if the input is a digit.

    Args: 

        data (str): The input data to validate. 

    Returns: 

        bool: True if the input is a digit, False otherwise. 

    """ 
    return data.isdigit() 
```

5. After fine-tuning, the LLM produces code that not only works properly but also obeys to the necessary standards. 
6. The revised function gives a clear name, type hints for both the parameter and return type, and gives appropriate  docstring that explains the function’s purpose and usage. 
7. The newly generated code, now meets the expectations set by mypy, pydocstyle, and flake8.

8. Fine-tuning allows the model to adapt to various project-specific guidelines, whether that involves different naming conventions, documentation practices, or error handling strategies.

9. The above may also applicable to the scenario like mail generation in the particular format inside the specific company ect...,