
import pandas as pd

df = pd.DataFrame(pd.read_excel("students.xlsx"))

# print(df)

# print()

# result = df.dropna()

# print(result)

# result = df.dropna(axis=1)

# print(result)

# result = df.dropna(how="any")

# print(result)

# result = df.dropna(thresh=3)

# print(result)

# result = df.dropna(subset=["Name","Age"])

# print(result)

# df = df.dropna()

# print(df)

df.dropna(inplace=True)

print(df)