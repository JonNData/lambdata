# my_lambdata/frames.py

# State abbrev <=> full name

import pandas


class MyFrame(pandas.DataFrame):
    """
    pandas.DataFrame should have a column of "abbrev"
    """
    def add_state_names(self):
        """
        Add a column of state names to a dataframe that already has the abbrevs
        Return a copy of the DataFrame with a new column called "name"
        """
        #names_map = {"CT": "Conn", "CO": "Colorado", "CA": "Cali"}
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
        } # http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
        #breakpoint() # python 3.7 or later, otherwise use pdb module
        self["name"] = self["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

#df1 = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
#df2 = pandas.DataFrame({"abbrev": ["AZ", "DC", "CO", "MI", "WI"]})


if __name__ == "__main__":
     # invoke all below only if run from command line not if imported from other file

    print("-------")
    my_frame = MyFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    print(type(my_frame))
    my_frame.add_state_names()
    print(my_frame.head())

    print("-------")
    my_frame = MyFrame({"abbrev": ["AZ", "DC", "CO", "MI", "WI"]})
    print(type(my_frame))
    my_frame.add_state_names()
    print(my_frame.head())