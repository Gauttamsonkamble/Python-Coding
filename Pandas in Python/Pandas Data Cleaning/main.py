
import numpy as np
import pandas as pd 

df = pd.DataFrame({
    "Name" : ["Asha","Rohan",None,"Meera"],
    "Age" : ["25",np.nan,31,pd.NA],
    "Score":[88.0,92.5,np.nan,79.0],
    "City" :["Pune","Mumbai","Nagpur",None]
})



print(df)
