
import pandas as pd 

df = pd.DataFrame(pd.read_excel("students.xlsx"))

print(df)

print()

# print(df.notna())

valid_people = df[df["Name"].notna() & df["Age"].notna()]

print(valid_people)

print(df.notna().sum())

selected = df[df["Name"].notna() | df["Age"].notna()]

print(selected)