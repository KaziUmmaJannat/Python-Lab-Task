import pandas as pd

import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv', r'c:\Users\kaziu\OneDrive\Documents\PYTHON LAB TASK\Lab-8\titanic.csv')
titanic = pd.read_csv(r"c:\Users\kaziu\OneDrive\Documents\PYTHON LAB TASK\Lab-8\titanic.csv")

print(titanic.head())

# Remove duplicate rows
titanic = titanic.drop_duplicates()

# Fill missing Age values
titanic["Age"] = titanic["Age"].fillna(
    titanic["Age"].mean()
)

# Convert wrong format example
titanic["Fare"] = pd.to_numeric(
    titanic["Fare"],
    errors="coerce"
)

# Remove remaining missing values
titanic = titanic.dropna()

print(titanic.info())