# 🎓 Student Performance Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Libraries](https://img.shields.io/badge/Packages-Pandas%2CNumPy%2CScikit--learn%2CMatplotlib%2CSeaborn-yellow)

---

## 📝 Mission
Our mission is to **predict student exam scores** using factors like study hours, attendance, parental involvement, and motivation. This helps educators and parents improve learning outcomes.

---

## 📂 Repository Structure

linear_regression_model/
│
├── linear_regression/ # Notebook, scripts, and trained models
│ ├── multivariate.ipynb # Jupyter Notebook with full analysis
│ ├── predict.py # Script to make predictions
│ └── best_model_LinearRegression.pkl # Saved best Linear Regression model
│
├── data/ # Dataset used for training
│ └── Student_PerformanceFactors.csv
│
├── API/ # Placeholder for future API
│ └── .gitkeep
├── FlutterApp/ # Placeholder for Flutter app
│ └── .gitkeep
├── summative/ # Placeholder for additional summative files
│ └── .gitkeep
├── README.md # This file


---

## 📊 Dataset
- **Source:** Kaggle / Student Performance Dataset  
- **Entries:** 6607  
- **Features:** Hours_Studied, Attendance, Parental_Involvement, Motivation_Level, Previous_Scores, etc.  
- **Target:** Exam_Score  

---

## 📈 Analysis
- Visualizations: correlation heatmaps, histograms, scatter plots  
- Models implemented: Linear Regression, Decision Tree, Random Forest  
- Linear Regression optimized using gradient descent  
- Best model saved as `best_model_LinearRegression.pkl`

---

## 🚀 How to Use
1. Open `multivariate.ipynb` to explore data, feature engineering, and model training.  
2. Use `predict.py` to make predictions with new student data:
```bash
python linear_regression/predict.py

🌟 Notes

🎯 Focused on actionable insights for student improvement

🛠️ Built using Python, Pandas, NumPy, Scikit-learn, Matplotlib, and Seaborn

📌 Ready for future API or Flutter app integration
