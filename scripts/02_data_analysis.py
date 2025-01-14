import pandas as pd

# Load preprocessed dataset
data_path = "data/processed/cleaned_data.csv"
data = pd.read_csv(data_path)

# Summary statistics
summary = data.describe(include="all")
summary.to_csv("outputs/summary_statistics.csv")

# Analyze relationships
correlation_matrix = data.corr()
correlation_matrix.to_csv("outputs/correlation_matrix.csv")

print("Data analysis complete. Results saved.")
