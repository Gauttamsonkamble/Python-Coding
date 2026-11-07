
import pandas as pd 

df = pd.DataFrame({
    "Names : " :["Rahul","Priya","Amit","sneha"],
    "Marks : " : [85,80,75,95],
    "City : " : ["Punr","Mumbai","Nanded","Pune"]
})

# print(df)

print(df.head(3))

print(df.tail(2))