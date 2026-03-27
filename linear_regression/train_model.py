import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

# 1️⃣ Create simple dataset (no CSV needed for now)
data = {
    "Hours_Studied": [2, 3, 5, 7, 1, 4, 6, 8, 9, 2],
    "Previous_Score": [50, 55, 65, 70, 45, 60, 68, 75, 80, 52],
    "Exam_Score": [55, 58, 68, 75, 48, 63, 70, 78, 85, 56]
}

df = pd.DataFrame(data)

# 2️⃣ Features & target
X = df[["Hours_Studied", "Previous_Score"]]
y = df["Exam_Score"]

# 3️⃣ Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train models
lr = LinearRegression().fit(X_train, y_train)
dt = DecisionTreeRegressor().fit(X_train, y_train)
rf = RandomForestRegressor().fit(X_train, y_train)

# 5️⃣ Evaluate
mse_lr = mean_squared_error(y_test, lr.predict(X_test))
mse_dt = mean_squared_error(y_test, dt.predict(X_test))
mse_rf = mean_squared_error(y_test, rf.predict(X_test))

print("LR:", mse_lr)
print("DT:", mse_dt)
print("RF:", mse_rf)

# 6️⃣ Pick best
models = {"lr": lr, "dt": dt, "rf": rf}
mse = {"lr": mse_lr, "dt": mse_dt, "rf": mse_rf}

best_name = min(mse, key=mse.get)
best_model = models[best_name]

print("Best model:", best_name)

# 7️⃣ Save model to API folder
os.makedirs("../API", exist_ok=True)
joblib.dump(best_model, "../API/best_model.pkl")

print("✅ Model saved successfully!")