
import numpy as np
import pandas as pd 

df = pd.DataFrame({
    "Name" : ["Asha","Rohan",None,"Meera"],
    "Age" : ["25",np.nan,31,pd.NA],
    "Score":[88.0,92.5,np.nan,79.0],
    "City" :["Pune","Mumbai","Nagpur",None]
})

# df = pd.read_excel("students.xlsx")

df1 =(pd.DataFrame(df))


print(df)

print()

print(df.isna())

print(df.isna().sum())

missing_age_rows =df[df["Score"].isna()] 

print(missing_age_rows)
