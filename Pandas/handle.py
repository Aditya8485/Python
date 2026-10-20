import pandas as pd

data = {
"Name" : ['None', 'Shyam', 'Mohan', 'None', 'Gita', 'Aditya', 'Ramesh', 'Suresh', 'Anita', 'Sunita'],
"Age" : [25, 30, 35, 28, 32, 29, 31, 33, 34, 36],
'Salary' : [None, 60000, 70000, None, 65000, 78000, 80000, 90000, 100000, 110000],
"Performance" : [85, 90, 88, 92, None, 22, 34, 77, 88, 12]
}


df = pd.DataFrame(data)
print(df)

#print(df.pop('Salary'))  # Remove the 'Salary' column and return it

#Now we are going to fill the missing values 
df['Performance'].fillna(df['Performance'].mean(), inplace=True)
print(df)