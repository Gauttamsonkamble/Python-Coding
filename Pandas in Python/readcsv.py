
import pandas as pd 

df = pd.read_csv("Excel file\Resources_and_Towers.csv")

print(df)

df.to_csv("RandT.csv",index=False)

df1 = pd.DataFrame({
    "Names" :["Rahul","Priya","Amit","sneha"],
    "Marks" : [85,80,75,95],
    "City" : ["Pune","Mumbai","Nanded","Pune"]
})

df1.to_csv("StudentData.csv",index=False)