import pandas as pd

data = pd.read_csv(r"c:\Users\kaziu\OneDrive\Documents\PYTHON LAB TASK\Lab-8\data.csv")

print("First 5 rows:")
print(data.head())

print("\nLast 5 rows:")
print(data.tail())

print("\nInformation:")
print(data.info())