
import pandas as pd 

df = pd.DataFrame(pd.read_excel("students.xlsx"))

print(df)

cleaned = df.fillna({
    "Name":"Unknown",
    "Age":df["Age"].median(),
    "Score":0,
    "City":"Not Specified"
})

print()

# print(cleaned)

# df_filled = df.fillna("Not Available")

# print()

# print(df_filled)

# f_filled = df.copy()

# f_filled["Score"] =f_filled["Score"].ffill()

# print(f_filled)

b_fiilled = df.copy()

b_fiilled["Age"] = b_fiilled["Age"].bfill()

print(b_fiilled)

new_excel = b_fiilled.to_excel("Students2.xlsx")