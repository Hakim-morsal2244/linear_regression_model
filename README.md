# 🎓 Student Performance Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Libraries](https://img.shields.io/badge/Packages-Pandas%2CNumPy%2CScikit--learn%2CMatplotlib%2CSeaborn-yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135.2-green)
![Flutter](https://img.shields.io/badge/Flutter-App-blueviolet)

---

## 📝 Mission
Our mission is to **predict student exam scores** using factors like study hours, attendance, parental involvement, and motivation. This helps educators, parents, and students optimize learning outcomes with actionable insights.

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
├── API/ # FastAPI backend for predictions
│ ├── prediction.py # FastAPI app to serve model
│ └── best_model_LinearRegression.pkl # Model copied for API
│
├── FlutterApp/ # Flutter mobile app to call API
│ ├── services/prediction_service.dart
│ └── main.dart
│
├── summative/ # Summative or additional project files
│ └── .gitkeep
│
├── README.md # This file


---

## 📊 Dataset
- **Source:** Kaggle / Student Performance Dataset  
- **Entries:** 6607  
- **Features:** Hours_Studied, Attendance, Parental_Involvement, Motivation_Level, Previous_Scores, Sleep_Hours, Tutoring_Sessions, Physical_Activity, and more  
- **Target:** Exam_Score  

---

## 📈 Analysis & Models
- Exploratory Data Analysis (EDA) using Pandas, Matplotlib, Seaborn  
- Feature engineering: encoding categorical variables, scaling, and cleaning missing values  
- Models implemented:
  - **Linear Regression** (best-performing)
  - Decision Tree Regressor
  - Random Forest Regressor
- Linear Regression optimized using gradient descent  
- Best model saved as `best_model_LinearRegression.pkl`  
- Model evaluation metrics printed for comparison (MAE, MSE, RMSE)

---

## 🚀 API Integration
- Built using **FastAPI** for real-time predictions
- **Endpoint:** POST `/predict`  
- Accepts student data JSON with the following fields:
  ```json
  {
    "Hours_Studied": float,
    "Attendance": float,
    "Parental_Involvement": str
  }
Returns predicted Exam_Score
Swagger UI available at: http://127.0.0.1:8000/docs#/default/predict_predict_post
CORS enabled for integration with mobile/web apps
📱 Flutter App
Mobile app calls FastAPI backend to get predictions
Service: services/prediction_service.dart handles API requests
Inputs: feature1, feature2, feature3 (must match dataset columns)
Displays predicted exam score instantly
Can be extended for UI enhancements
💻 How to Run
1️⃣ Linear Regression Prediction
python linear_regression/predict.py
2️⃣ Start FastAPI
cd API
python -m uvicorn prediction:app --reload
3️⃣ Use Flutter App
cd FlutterApp
flutter pub get
flutter run
🌟 Notes
🎯 Focused on actionable insights for student improvement
🛠️ Built using Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, FastAPI, and Flutter
📌 Ready for deployment and future enhancements
🔗 API & Flutter app fully integrated for end-to-end prediction
🧩 Future Enhancements
Auto-retraining of model with new data
Integration with cloud-hosted API (e.g., Render, Heroku)
Add more features like learning disabilities, family income, and peer influence for better predictions
Improve Flutter UI with charts and historical score comparisons


⚠️ Note from the Author

I am Morsal Hakim, a student living in Afghanistan. Due to the ongoing situation, including unstable internet access, I was unable to create the video demo for this project. I sincerely apologize for this and hope you can kindly excuse it this time. I will ensure to complete all parts fully in the future.
