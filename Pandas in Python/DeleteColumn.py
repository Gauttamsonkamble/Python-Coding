
import pandas as pd 

df = pd.DataFrame({
    "Names" :["Rahul","Priya","Amit","sneha"],
    "Marks" : [85,80,75,95],
    "City" : ["Pune","Mumbai","Nanded","Pune"]
})

print(df)

df = df.drop(columns=["City"])

print()

print(df)