# my_lambdata/my_script.py
import pandas as pd

# Reach into another file and import
from my_mod import enlarge
from my_mod import nullcheck
from my_mod import list_into_df
from my_mod import Car


df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]],
                   columns=['letter', 'number'])
lst = [2,6,78,9,10]


print('new df with list', list_into_df(lst,df1))

print("------------")


x = 5
print("number", x)
print('Enlarged Number', enlarge(x))

print("Null checker \n\n\n")


car1 = Car('Toyota', 'Celica', 15000)
Car.set_lower_amount(0.85)
print('Original price', car1.price)

print('lower amount', car1.lower_amount)

# apply method
car1.apply_depreciation()

print('new price', car1.price)


