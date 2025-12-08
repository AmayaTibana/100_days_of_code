import pandas as pd

df = pd.read_csv("sample_data/wine-ratings-small.csv", index_col=0)
df.index = range(1, len(df)+1)
df.head()
data = df.to_dict()(orient='index')
wines = [data[key] for key in data] # Convert to list of dictionaries
# Example wine dictionary:
# {'name': 'Chateau Ste. Michelle Columbia Valley Riesling 2017',
#  'country': 'US',

#  'province': 'Washington',
#  'region_1': 'Columbia Valley',
#  'region_2': '',
#  'winery': 'Chateau Ste. Michelle',