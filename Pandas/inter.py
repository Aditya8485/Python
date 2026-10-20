import pandas as pd


data = {
    "name": ["Alice", "Bob", "Charlie", "sam", "eve", "Manish", "jitesh", "ritesh", "suresh", "sachin"],
    "age": [25, None, 35, 40 , 45, None, None, 50, 55, 60],

}

df = pd.DataFrame(data)
print('Before interpolate')
print(df)

df["age"] = df["age"].interpolate(axis=0, method="linear", inplace=True)
print("After interpolate")
print(df)   

""""
uses

seires data
time data
avoid dropping rows
estimated values fill out
"""