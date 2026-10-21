import pandas as pd

""""
df["column name].mean()
df["column name].max()
df["column name].min()
df["column name].sum() & so on..
"""

data = {
    "Name": ["Manish", "Rajesh", "Mahesh", "Ganesh"],
    "Age": [25, 30, 20, 10],
    "Salary": [50000, 10000, 20000, 80000],
}
df = pd.DataFrame(data)

Salary = df["Salary"].mean()
print(Salary)

Salary = df["Salary"].min()
print(Salary)

Salary = df["Salary"].max()
print(Salary)

Salary = df["Salary"].sum()
print(Salary)