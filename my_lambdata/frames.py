# my_lambdata/frames.py

# State abbrev <=> full name

import pandas as pd 

def add_state_names(my_df):
    """
    Add a column of state names to a df with state abbrevs
    my_df is a pandas.Dataframe, should have a column of abbrev
    Return  a copy of the df with a new column of "name"
    """

    names_map = {
        "CT": "Conneticut",
        "CO": "Colorado",
        "CA": "California",
        "TX": "Texas",
        'AZ': 'Arizona',
        'DC': 'Washington D.C.',
        'MI': 'Michigan',
        'WI': 'Wisconsin'
    }
    # breakpoint() # only available in 3.7 or later, else pdb
    new_df = my_df.copy()
    new_df['name'] = my_df['abbrev'].map(names_map)
    return new_df

df = pd.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
mutant = add_state_names(df)
print(mutant.head())

df2 = pd.DataFrame({"abbrev": ["AZ", "DC", "MI", "WI"]})
mutant2 = add_state_names(df2)
print(mutant2.head())