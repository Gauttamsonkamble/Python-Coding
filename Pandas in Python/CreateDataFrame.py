
import pandas as pd 

data = {
    "Roll No ": [101,102,103,104],
    "Name ":["Rahul","Priya","Amit","Snehal"],
    "Marks":[85,90,75,95]
}

# df = pd.DataFrame(data)
df = pd.DataFrame(data,index=["A","B","c","D"])

print(df)