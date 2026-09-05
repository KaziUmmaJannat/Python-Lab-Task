
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv', r'c:\Users\kaziu\OneDrive\Documents\PYTHON LAB TASK\Lab-12\diabetes_prediction_dataset.csv')
df = pd.read_csv(r"c:\Users\kaziu\OneDrive\Documents\PYTHON LAB TASK\Lab-12\diabetes_prediction_dataset.csv")
df.columns = [c.lower() for c in df.columns]
df = df.rename(columns={"outcome": "diabetes"})

print("Dataset:")
print(df.head())

X = df.drop("diabetes", axis=1)
y = df["diabetes"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)