### **Quantization vs Parameter Efficient Fine Tuning (peft)**

1. PEFT is about optimizing the training process, ensuring that the model can be adapted to specific tasks with minimal changes, conserving resources while maintaining performance.

2. PEFT is typically used during fine-tuning, where you are adapting a pre-trained model to a specific task.

3. PEFT methods update only certain parts of a model while keeping the rest of the model frozen.

---------------------------------------------------------------------------------------------------------------------
1. Quantization is focused on optimizing the model for inference by making it faster and more memory-efficient, often at the cost of a small drop in model accuracy.

2. Quantization is generally applied after training, as part of the model optimization for deployment.

3. Quantization reduces the numerical precision of the entire model, making it lighter and faster during inference.

----------------------------------------------------------------------------------------------------------------------- 

1. They can be combined to get the benefits of both. For example, QLoRA is a technique that applies both quantization (to reduce memory usage) and LoRA (a PEFT method for efficient fine-tuning). This combination allows for efficient fine-tuning on limited hardware while also optimizing the model for efficient deployment. 

### **What is interference?**

1. Inferencing means load the pretrained model and test your model over the data.

### **Quantization**

1. Quantization reduces the model size by changing the memory format of parameters to low format like float to int. Doing quantization will lead to loss of information.Bitsandbytes package is used

2. Symmetric: Scale factor, zero point = 0

3. Asymmetric: Scale factor, zero point != 0 (can be negative)

4. Quantization focuses on optimizing the model for inference by reducing the precision of its weights and activations, thereby enhancing speed and reducing memory usage.

5. By converting high-precision floating-point numbers into lower-precision representations, quantization effectively reduces memory usage and computational requirements while maintaining an acceptable level of accuracy.

:::tip 
1. [Quantization in LLMs: Why Does It Matter?](https://medium.com/data-from-the-trenches/quantization-in-llms-why-does-it-matter-7c32d2513c9e)

2. [A Visual Guide to Quantization - Maarten Grootendorst](https://www.maartengrootendorst.com/blog/quantization/)
:::

#### **Methods in the Quantization:**

1. Post-Training Quantization (PTQ)
     1. This approach involves quantizing a model after it has been trained.  During this process, weights are typically converted from high-precision formats (like 32-bit floats) to lower precision formats (such as 8-bit integers).  
2. Quantization-Aware Training (QAT):
     1. QAT is a method that integrates quantization into the training process itself. By simulating quantization effects during training, the model learns to accommodate the reduced precision of weights and activations.
3. QLoRA (Quantized Low-Rank Adaptation):  
     1. QLoRA combines quantization with low-rank adaptation techniques. It focuses on fine-tuning large models by quantizing their weights while also introducing low-rank updates for specific tasks. This approach allows for a significant reduction in memory usage and computational costs during fine-tuning, making it highly efficient for adapting large pre-trained models to new tasks.
4. Some more new methods of Quantization involves -> GGUF, GGML, GPTQ - Quantization in LLMs: Why Does It Matter? | by Aimee Coelho | data from the trenches | Medium.