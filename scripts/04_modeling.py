import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load preprocessed dataset
data_path = "data/processed/cleaned_data.csv"
data = pd.read_csv(data_path)

# Features and target
X = data.drop(columns="participation_label")
y = data["participation_label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
report = classification_report(y_test, predictions, output_dict=True)
pd.DataFrame(report).to_csv("outputs/classification_report.csv")

print("Modeling complete. Report saved.")
