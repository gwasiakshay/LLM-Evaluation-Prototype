from evaluate import load

# Load ROUGE metric
rouge = load("rouge")

# Sample predictions and references
predictions = ["The company reported strong earnings this quarter."]
references = ["This quarter, the company had strong earnings."]

# Evaluate
results = rouge.compute(predictions=predictions, references=references)
print("ROUGE Evaluation Results:")
print(results)