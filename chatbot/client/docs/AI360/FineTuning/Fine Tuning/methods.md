# Methods of fine tuning

## **What is Supervised finetuning and how it works?**

1. Supervised fine-tuning is a process where a pre-trained language model is further trained on a specific dataset with labeled examples. In this approach, the model is exposed to pairs of input data and their corresponding correct outputs, which helps it learn how to predict or generate more accurate results for similar tasks in the future.  

2. The key idea is to guide the model by explicitly providing the correct answers during training, allowing it to learn from structured and curated information.

3. Pre-trained Model -> Labeled Dataset-> Training Process -> Iterative Learning -> Evaluation and Testing.

## **How it differs from the Unsupervised finetuning?**

1. Unsupervised fine-tuning is a technique where a pre-trained language model is refined using unlabeled data. Unlike supervised fine-tuning, which relies on labeled examples with correct answers, unsupervised fine-tuning allows the model to learn patterns, structures, and relationships within the data without explicit guidance.  

2. This approach is particularly useful when labeled data is scarce or unavailable, as it can still help improve a model's understanding of specific domains or tasks. These kind of finetuning is used in the big tech companies while pre- training

## **What is self-supervised learning?**

1. Self-supervised fine-tuning is a method that allows a model to improve its performance by learning from unlabeled data without the need for explicit human supervision. In this approach, the model generates tasks and labels directly from the data itself.  

2. This is achieved through various techniques that enable the model to create structured learning objectives from raw text. Self-supervised fine-tuning bridges the gap between supervised and unsupervised learning, offering the best of both worlds by using unlabeled data while still learning in a guided manner.

3. self-supervised fine-tuning allows models to teach themselves by generating tasks from the data they are exposed to. This process helps the model enhance its understanding of language, making it more adept at handling specialized domains or complex language tasks. It’s a powerful approach, especially when labeled data is scarce, but large amounts of raw data are available for learning.

:::tip 
1. Learn more about [Self-Supervisied Learning](https://www.ibm.com/topics/self-supervised-learning)
:::

**Steps in self supervised learning:**

 1. Pre-trained Model as the Base
      1. Self-supervised fine-tuning, like other types of fine-tuning, starts with a pre-trained model.

 2. Creating Learning Tasks from Data
       1. In self-supervised learning, the model generates its own learning tasks based on the structure of the data.  
       2. For example, the model might mask certain words in a sentence and try to predict those missing words, or it may rearrange sentences and learn to predict the correct sequence. These self-created tasks allow the model to learn context, relationships, and structure within the data, effectively guiding its learning process without external labels.

 3. Contrastive Learning
      1.  The model is given pairs of similar and dissimilar examples and learns to differentiate between them. For instance, the model might be tasked with distinguishing whether two sentences are related or unrelated based on their content. This technique encourages the model to develop a deeper understanding of context and semantics by recognizing patterns and differences.

 4. Evaluation and Testing.
