
import pandas as pd 

df = pd.DataFrame({
    "Names" :["Rahul","Priya","Amit","sneha"],
    "Marks" : [85,80,75,95],
    "City" : ["Pune","Mumbai","Nanded","Pune"]
},index=["A","B","C","D"])

print(df[["Names","City"]])

# print(df.head(2))

# print(df.tail(2))

# print(df.count())

# print(df.describe())

# print(df.info())


