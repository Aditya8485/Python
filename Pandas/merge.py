import pandas as pd


data1 = pd.DataFrame({
    "Name":["Raj", "hansraj", "Ganesh", "Ramesh", "Suresh", "Ramesh", "Ganesh"],
    "IDS": [1, 20, 3, 41, 5, 64, 7],
    "Age": [25, 55, 65, 43, 32, 30, 32],
    "Salary": [10000, 30000, 40000, 10000, 15000, 30000, 50000],
    "Performance": [5.5, 4.4, 5.5, 7, 8, 4.4, 5.5]
})

data2 = pd.DataFrame({
    "Name":["Raj", "hansraj", "Ganesh", "Ramesh", "Suresh", "Ramesh", "Ganesh"],
    "IDS": [1, 2, 3, 4, 5, 6, 7],
    "Age": [25, 55, 65, 43, 32, 30, 32],
    "Salary": [10000, 30000, 40000, 10000, 15000, 30000, 50000],
    "Performance": [5.5, 4.4, 5.5, 7, 8, 4.4, 5.5],
    "Bonus": [1000, 1000, 1500, 1700, 2000, 1000, 1500]
})

df_merged = pd.merge(data1, data2, on="IDS", how="inner")
print('inner join')
print(df_merged)

df_merged = pd.merge(data1, data2, on="IDS", how="outer")
print('outer join')
print(df_merged)

df_merged = pd.merge(data1, data2, on="IDS", how="left")
print('left join')
print(df_merged)

df_merged = pd.merge(data1, data2, on="IDS", how="right")
print('right join')
print(df_merged)


"""
uses:
combination creation for comparing dataframes
making dataframes for analysis
takin out all possible pairs from datasets
"""