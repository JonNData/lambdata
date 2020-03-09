# my_lambdata/my_script.py
import pandas as pd

# Reach into another file and import
from my_lambdata.my_mod import enlarge


print("Hello World")

df = pd.DataFrame({"state" : ['CT','CA','WY', 'TX']})
print(df.head())

print("------------")


x = 5
print("number", x)
print('Enlarged Number', enlarge(x))