import pandas as pd 

df = pd.read_excel("Excel file\Resources_and_Towers.xlsx")

print(df)

df.to_excel("newxl.xlsx",index=False)

df1 = pd.DataFrame({
    "Names" :["Rahul","Priya","Amit","sneha"],
    "Marks" : [85,80,75,95],
    "City" : ["Pune","Mumbai","Nanded","Pune"]
})

df1.to_excel("studentData.xlsx",index=False)