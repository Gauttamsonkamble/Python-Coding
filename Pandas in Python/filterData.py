
import pandas as pd 

df = pd.DataFrame({
    "Names" :["Rahul","Priya","Amit","sneha"],
    "Marks" : [85,80,75,95],
    "City" : ["Pune","Mumbai","Nanded","Pune"]
})

# print(df[df["Marks"]>80])

# print(df[df["City"]=="Mumbai"])

# print(df[(df["Marks"]>80) & (df["City"]=="Pune")])

print(df[["City","Marks"]])

