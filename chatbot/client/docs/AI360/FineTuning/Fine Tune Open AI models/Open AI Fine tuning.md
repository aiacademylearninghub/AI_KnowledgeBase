# Fine Tuning OpenAI Models

:::info
[Fine Tuning OpenAI Models](https://platform.openai.com/docs/guides/fine-tuning/when-to-use-fine-tuning)
:::

1. LLaMA Index also gives packages to fine-tune based on different techniques with different example notebooks. This package is used to fine-tune different LLMs using LLaMA Index Fine Tune Base Class for fine tuning.

## **Step-by-Step Process**

1. Validate Dataset
  
     1. Ensure the dataset is in the correct format required for fine-tuning.
   
     2. Check for data quality and consistency.
   
2. Calculate Tokens and Price

      1. Count the number of tokens in your dataset.

      2.  Estimate the cost based on the token count and current pricing.
   
3. Upload File

      1. Upload the validated dataset to OpenAI's platform.
  
4. Create Fine Tune Job

      1. Initiate a fine-tune job using the uploaded dataset.

      2. Use the fine-tune base class from LLaMA index for easier integration.

5. Get Fine Tune Job

      1.  Retrieve details of the ongoing fine-tune job.

      2. Monitor the job's progress and status.

6. Get the Checkpoints of the Job

     1. Access checkpoints created during the fine-tuning process.

     2. Use these checkpoints to resume or analyze the training process.

7. Check Status of Job

     1. Ensure the fine-tune job completes successfully.

     2. Verify the job status through OpenAI’s API or dashboard.

8. Trying Out the Fine-tuned Model

     1. Test the fine-tuned model with various prompts.

     2. Evaluate the performance and accuracy of the model.

### **Comparison: OpenAI vs. Azure OpenAI Service**

|Feature/Aspect|OpenAI|Azure OpenAI Service|
|---------------|----------|-----------|
|Service Provider|OpenAI|Microsoft Azure|
|Regions Available|Global|Varies by region, not all regions support fine-tuning|
|Pricing|Fixed pricing(add photo)|Pricing depends on region and varies accordingly(add photo)|
|Fine-Tuning Cost|Based on tokens|Based on training hour and region-specific rates|
|Deployment Cost|Higher Cost per token for hosting/inference|Different deployment hosting cost and per token based on region and usage|
|Dataset Upload|Via OpenAI API|Via Azure portal or API|
|Fine-Tune Job Creation|OpenAI API or platform|Azure API or portal|
|Monitoring Progress|OpenAI API or platform|Azure API or portal|
|Concurrent Users|Works Good|Unknown|
|Latency|Little higher latency if requests to our model are rare.|Unknown|