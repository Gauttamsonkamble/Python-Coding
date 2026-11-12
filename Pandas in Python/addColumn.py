
import pandas as pd 

df = pd.DataFrame({
    "Names" :["Rahul","Priya","Amit","sneha"],
    "Marks" : [85,80,75,95],
    "City" : ["Pune","Mumbai","Nanded","Pune"]
})

print(df)

print()

df["Result"] = ["pass","fail","pass","fail"]

print(df)