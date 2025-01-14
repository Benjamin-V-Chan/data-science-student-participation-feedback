import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load dataset
data_path = "data/student_participation_feedback_dataset.csv"
data = pd.read_csv(data_path)

# Handle missing values
data = data.fillna(data.median(numeric_only=True))
data = data.fillna(method="ffill").fillna(method="bfill")

# Normalize numeric features
scaler = MinMaxScaler()
numeric_columns = [
    "interaction_duration (min)", "feedback_rating (1-5)",
    "assignments_completed", "total_interactions", "quiz_score (%)",
    "engagement_score", "age"
]
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

# Encode categorical variables
encoder = LabelEncoder()
categorical_columns = ["final_grade", "learning_style", "participation_label"]
for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])

# Save cleaned dataset
data.to_csv("data/processed/cleaned_data.csv", index=False)

print("Data preprocessing complete. Cleaned dataset saved.")
