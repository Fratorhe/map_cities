# In this case we create the YAML file from a csv (or more than one)
# This allows to download google lists and put them here "easily"
# One needs to add the subsections in the Notes of the csv.
# to remove the URLs from those files you can use the regex https?://\S+
import pandas as pd

from create_yaml_file import YAML_file_parser

place = "Rome"
coordinates = [41.9028, 12.4964]
creator = "Vincent"
year = 2023

# load the dataframes
df1 = pd.read_csv('csv/rome.csv')
# print(df1.Title.values)

unique_sections = df1['Note'].unique()
# print(unique_sections)

data = {}
for section in unique_sections:
    places_section = df1[df1['Note'] == section]
    places_comment_dict = places_section.set_index('Title')['Comment'].to_dict()
    data[section] = places_comment_dict



create_city = YAML_file_parser(coordinates, place, creator, year, data)
create_city.to_YAML()