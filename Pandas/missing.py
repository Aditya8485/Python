import pandas as pd 

data = {
"Name" : ['Ram', 'Shyam', 'Mohan', 'None', 'Gita'],
"Age" : [25, 30, 35, 28, 32],
'Salary' : [None, 60000, 70000, None, 65000],
"Performance" : [85, 90, 88, 92, None]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())

#Now check sum of missing values

print(df.isnull().sum())

#Now grepping data 

print(df.head(3))
print(df.tail(2))