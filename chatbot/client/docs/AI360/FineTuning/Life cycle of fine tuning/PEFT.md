### **Parameter Efficient Fine Tuning (peft)**

![PEFT](../images/PEFT.PNG)

1. Parameter Efficient Fine-Tuning (PEFT) is a method used to fine-tune large pre-trained models while only adjusting a small subset of their parameters. This approach is designed to reduce the computational resources and memory needed for fine-tuning, making it more practical and efficient, especially when dealing with large models like those used in natural language processing (NLP) and computer vision.
2. This significantly reduces the number of parameters that need to be optimized, speeding up the process and lowering the hardware requirements. PEFT is particularly useful in cases where you want to fine-tune a model for a new task but have limited computational resources.

#### **Methods in PEFT:**

1. LORA
     1. LoRA reduces the number of trainable parameters by learning pairs of rank-decompostion matrices while freezing the original weights.
     2. This vastly reduces the storage requirement for large language models adapted to specific tasks and enables efficient task-switching during deployment all without introducing inference latency.  
     3. LoRA also outperforms several other adaptation methods including adapter, prefix-tuning, and fine-tuning.
      :::tip
           1. [LoRA (Low-Rank Adaptation) (huggingface.co)](https://huggingface.co/docs/text-generation-inference/main/en/conceptual/lora)
   
           2. [microsoft/LoRA: Code for loralib, an implementation of "LoRA: Low-Rank Adaptation of Large Language Models" (github.com)](https://github.com/microsoft/LoRA)
   
           3. [What is Low-Rank Adaptation (LoRA) | explained by the inventor - YouTube](https://www.youtube.com/watch?v=DhRoTONcyZE&t=362s)
     :::

2. [Some more methods of PEFT, Each can be used in the different use cases](https://huggingface.co/docs/peft/package_reference/peft_types)