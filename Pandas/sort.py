import pandas as pd


data = {
    "Name": ["Manish", "Rajesh", "Mahesh", "Ganesh"],
    "Age": [25, 30, 20, 10],
    "Salary": [50000, 10000, 20000, 80000],
}
df = pd.DataFrame(data)

#df.sort_values(by="Age", ascending=True, inplace=True)
#print("Dataframe after sorting by Age in ascending order:")
#print(df)

"""
Now we will target 2 coulmns at once
"""
df.sort_values(by=["Age", "Salary"], ascending=True, inplace=True)
print("Double Coulmns targetted")
print(df)
"""
ascending = True => sort in ascending order
ascending = False => sort in descending order"""
