# Step 8: Prediction Script using Saved Best Model

import pandas as pd
import joblib

# 1️⃣ Load the saved best model
model_path = "best_model_LinearRegression.pkl"  # <-- update if your best model is different
best_model = joblib.load(model_path)
print("✅ Best model loaded successfully!")

# 2️⃣ Load new data for prediction
# You can replace this with a new CSV or a single row as a dictionary
# Example: predicting for one student
sample_data = {
    "Hours_Studied": [10],
    "Attendance": [90],
    "Parental_Involvement": [1],        # make sure this matches your LabelEncoder values
    "Access_to_Resources": [1],
    "Extracurricular_Activities": [0],
    "Sleep_Hours": [7],
    "Previous_Scores": [85],
    "Motivation_Level": [2],
    "Internet_Access": [1],
    "Tutoring_Sessions": [2],
    "Family_Income": [1],
    "Teacher_Quality": [2],
    "School_Type": [1],
    "Peer_Influence": [0],
    "Physical_Activity": [3],
    "Learning_Disabilities": [0],
    "Parental_Education_Level": [2],
    "Distance_from_Home": [1],
    "Gender": [1]
}

# Convert to DataFrame
X_new = pd.DataFrame(sample_data)

# 3️⃣ Make prediction
predicted_score = best_model.predict(X_new)
print(f"\nPredicted Exam Score for the sample student: {predicted_score[0]:.2f}")