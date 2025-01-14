import pandas as pd
import matplotlib.pyplot as plt

# Load preprocessed dataset
data_path = "data/processed/cleaned_data.csv"
data = pd.read_csv(data_path)

# Distribution of grades
data["final_grade"].value_counts().plot(kind="bar", title="Distribution of Grades")
plt.savefig("outputs/grade_distribution.png")
plt.close()

# Engagement score vs. feedback rating
data.plot.scatter(x="engagement_score", y="feedback_rating (1-5)", title="Engagement vs Feedback")
plt.savefig("outputs/engagement_vs_feedback.png")
plt.close()

# Participation label counts
data["participation_label"].value_counts().plot(kind="bar", title="Participation Label Counts")
plt.savefig("outputs/participation_label_counts.png")
plt.close()

print("Visualizations saved to outputs.")