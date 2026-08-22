import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv', r'c:\Users\kaziu\OneDrive\Documents\PYTHON LAB TASK\Lab-9\iris.csv')
data = pd.read_csv(r"c:\Users\kaziu\OneDrive\Documents\PYTHON LAB TASK\Lab-9\iris.csv")


# Line Plot
plt.plot(data.index, data["sepal_length"])
plt.title("Line Plot")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()


# Scatter Plot
plt.scatter(
    data["sepal_length"],
    data["petal_length"]
)

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()


# Bar Chart
species_count = data["species"].value_counts()

plt.bar(
    species_count.index,
    species_count.values
)

plt.title("Species Count")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()


# Histogram
plt.hist(data["sepal_length"])

plt.title("Sepal Length Distribution")
plt.xlabel("Length")
plt.ylabel("Frequency")

plt.show()


# Pie Chart
plt.pie(
    species_count.values,
    labels=species_count.index,
    autopct="%1.1f%%"
)

plt.title("Species Percentage")
plt.show()


# Subplot
fig, ax = plt.subplots(1,2)

ax[0].hist(data["sepal_length"])
ax[0].set_title("Histogram")

ax[1].pie(
    species_count.values,
    labels=species_count.index
)
ax[1].set_title("Pie Chart")

plt.show()