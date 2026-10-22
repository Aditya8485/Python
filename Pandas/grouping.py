import pandas as pd

data = {
    "Name": ["Manish", "Rajesh", "Mahesh", "Ganesh", "Manish"],
    "Age": [25, 30, 20, 10, 10],
    "Salary": [50000, 10000, 20000, 80000, 10000],
}

df = pd.DataFrame(data)
"""
grouped = df.groupby("Salary")["Age"].sum()
print(grouped)

grouped2 = df.groupby(["Age", "Salary"])["Name"].count()
print(grouped2)"""

grouped2 = df.groupby(["Age", "Salary"])["Salary"].min()
print(grouped2)

grouped2 = df.groupby(["Age", "Salary"])["Salary"].max()
print(grouped2)