## When to use RAG and Fine-tuning?

|  |RAG|Fine-tuning|
|:-------------|:----------:|:-------------:|
|Real-Time data? |   ✅  |   ❌   |
| Change Model behavior?   | ❌ | ✅ |
| Minimize Hallucination?     | ✅ | ❌       |
| Training data Available?   | ❌  | ✅ |
| Is data mostly dynamic?     | ✅ | ❌       |
| Model lacks characteristics, your use-case needed ?| ❌ | ✅ |

![trade-off](../images/trade-off_graph.PNG)

## **Advantages - Fine tuning**

1. **Customization**
     1.  Fine-tuning allows models to be tailored to specific needs or tasks. Instead of relying on a generic model, you can adjust it to better understand the nuances of a particular industry, audience, or domain.  

2. **Consistency**
     1. One of the significant benefits of fine-tuning is maintaining a consistent level of performance across different tasks.  
     2. This reliability is essential when building applications(eg: medical) that require steady, predictable behavior, as it minimizes variability and errors when dealing with specialized content.

3. **Specialization**
     1. Fine-tuning enhances the model’s ability to specialize in a particular area, making it more knowledgeable and accurate in that specific domain.

### **Disadvantage**

1. High computation cost
2. Dependency on training data.
     1. Fine-tuning is highly dependent on the quality and quantity of the training data. If the data used for fine-tuning is incomplete, biased, or not representative of the domain, the model’s performance will suffer. Essentially, the model can only learn from what it is fed, so poor-quality data will result in a less effective model.
3. Over-fitting
     1. Over-fitting occurs when the model becomes too specialized on the fine-tuning data. This means the model might perform exceptionally well on the specific training data but fail to generalize when exposed to new, unseen data. Over-fitting can be problematic because it limits the model’s flexibility and usefulness in real-world applications, especially when the input is varied and unpredictable.
4. Data loss may occur after training
     1. During fine-tuning, there is a risk of what is known as "catastrophic forgetting." This happens when the model loses some of the general knowledge it acquired during pre-training as it adapts to new, domain-specific data. The model may become too focused on the specialized knowledge and forget some of the broader, foundational information it learned earlier.**