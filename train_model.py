import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, classification_report

data = pd.read_excel("student_data_changed.xlsx")

print("==========================================")
print(" SMART STUDENT PERFORMANCE PREDICTION")
print("==========================================")

print("\nDataset loaded successfully!")
print("Total students:", len(data))

X = data[
    [
        "Attendance",
        "Study Hours",
        "Internal Marks",
        "Assignment",
        "Previous Score"
    ]
]


y = data["Performance"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining students:", len(X_train))
print("Testing students :", len(X_test))

model = Pipeline([("scaler", StandardScaler()),("logistic_regression", LogisticRegression(max_iter=2000 ))])

model.fit(X_train,y_train)

print("\nLogistic Regression training completed!")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)


print("\n==========================================")
print("MODEL PERFORMANCE")
print("==========================================")

print(
    "Algorithm:",
    "Logistic Regression"
)

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)

model_package = {

    "model": model,

    "model_name": "Logistic Regression",

    "accuracy": accuracy,

    "features": [
        "Attendance",
        "Study Hours",
        "Internal Marks",
        "Assignment",
        "Previous Score"
    ]
}


with open(
    "student_performance_model.pkl",
    "wb"
) as file:

    pickle.dump(
        model_package,
        file
    )

print("\n==========================================")
print("MODEL SAVED SUCCESSFULLY")
print("==========================================")

print(
    "Algorithm:",
    "Logistic Regression"
)

print("Accuracy:",round(accuracy * 100, 2),"%")
print("File created:")
print("student_performance_model.pkl")
print("==========================================")