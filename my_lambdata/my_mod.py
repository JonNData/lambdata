# my_lambdata/my_mod.py
import pandas as pd

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# check for nulls in a viewable manner
def nullcheck(df):
    return pd.DataFrame(df.isnull().sum(), columns=['nulls'])

# Single function to take a list, turn it into a series and add it to a dataframe as a new column
def list_into_df(lst, dtf):
    new_col = pd.Series(lst)
    df_new = pd.concat([dtf, new_col], axis=1)
    return df_new


# Create a class to process cars with attributes
class Car:
  # instantiate with first argument self
  def __init__(self, make ,model, price):
    self.make = make
    self.model = model
    self.price = price

    
  # create another method
  def fullname(self):
    return '{} {}'.format(self.make, self.model)

  # Create a method to decrease price
  def apply_depreciation(self):
    self.price = int(self.price * self.lower_amount)
    # using self with the raise_amount let's each object have their own raise amount

  @classmethod # This will change the value for the whole class...
  def set_lower_amount(cls, amount): # cannot use 'class' as argument
    cls.lower_amount = amount

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))