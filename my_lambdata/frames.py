# my_lambdata/frames.py

# State abbrev <=> full name

import pandas as pd 


class DataProcessor():
    def __init__(self, my_df):
        """
        my_df is a pandas.Dataframe, should have a column of abbrev
        """
        self.df = my_df

    def add_state_names(self):
        """
        Add a column of state names to a df with state abbrevs
    
        Return  a copy of the df with a new column of "name"
        """
        names_map = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
        # breakpoint() # only available in 3.7 or later, else pdb
        self.df['name'] = self.df['abbrev'].map(names_map)
        

df1 = pd.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
df2 = pd.DataFrame({"abbrev": ["AZ", "DC", "MI", "WI"]})

for df in [df1, df2]:
    processor = DataProcessor(df)
    processor.add_state_names()
    print(processor.df.head())

