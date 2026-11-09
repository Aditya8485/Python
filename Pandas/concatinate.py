import pandas as pd

delhi = pd.DataFrame({
    "Name": ['Raju', 'kaju', 'manju'],
    "age": [18, 17, 20]
})

mumbai = pd.DataFrame({
    "Name": ['Suresh', 'Ramesh', 'Mahesh'],
    "age": [11, 14, 19]
})

cnc = pd.concat([delhi, mumbai], axis=0, ignore_index=True)
print(cnc)

cnc = pd.concat([delhi, mumbai], axis=1, ignore_index=True)
print(cnc)


cnc = pd.concat([delhi, mumbai], axis=1, ignore_index=False)
print(cnc)