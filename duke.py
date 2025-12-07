from csv import DictReader

# Open the CSV file and read it into a list of dictionaries and ignore unicode errors

with open('sample_data/wine-ratings-small.csv', encoding='utf-8', errors='ignore') as f:
    reader = DictReader(f)
    wines = list(reader)


# The wines variable is now a list of dictionaries, one for each row in the CSV file. This is the sample output of a single entry:
# {'': '1',
#  'name': 'Laurenz V Charming Gruner Veltliner 2014',
#  'grape': '',
#  'region': 'Kamptal, Austria',
#  'variety': 'White Wine',
#  'rating': '90.0',
#  'notes': ''}

quit()