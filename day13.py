import numpy as np
import pandas as pd

#  Python list which we know already where you give a list of things in the brackets vs NumPy array
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

print(python_list)
print(numpy_array)

# Numpy is different because it runs math on all the arrays at once
print(numpy_array * 2)
print(numpy_array + 10)
print(numpy_array ** 2)


print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 11))
print(np.random.randint(1, 100, 5))


data = {
    "name": ["Vasu", "Alex", "Piyu", "Raj", "Kalpana"],
    "age": [26, 24, 25, 28, 30],
    "score": [92, 85, 78, 95, 88],
    "city": ["Orlando", "New York", "London", "Mumbai", "Chicago"]
}

df = pd.DataFrame(data)

print(df)
print("---")
print(df.describe()) 
# df.describe() calculated count, mean, std, min, max 
# automatically across all your data — that would have taken 20+ lines 
# of Python to do manually
print("---")
print(df["name"])
print("---")
print(df[df["score"] > 88])
# df[df["score"] > 88] filtered your entire table to only 
# show people with scores above 88 — Vasu and Raj — in one line. 
# That's the equivalent of a SQL WHERE clause


titanic = pd.read_csv("students.csv")

print(titanic.head())
print("---")
print(titanic.shape)
print("---")
print(titanic.columns.tolist())
print("---")
print(titanic.isnull().sum())

# This is how you get a count of a specific list of field using Panda
print(titanic["Survived"].value_counts())
print("---")

# How to get an average of somethig
print(f"Average age: {titanic['Age'].mean():.1f}")
print("---")

# How to check something against something else such as this example we are getting the survival rate by gender
print(titanic.groupby("Sex")["Survived"].mean())
print("---")

# Now this is how you filter by something
survivors = titanic[titanic["Survived"] == 1]
print(f"Total survivors: {len(survivors)}")
print(f"Survival rate: {len(survivors)/len(titanic) * 100:.1f}%")