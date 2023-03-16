# In this case we create the YAML file from a csv (or more than one)
# This allows to download google lists and put them here "easily"
# One needs to add the subsections in the Notes of the csv.
# to remove the URLs from those files you can use the regex https?://\S+
import pandas as pd

from create_yaml_file import YAML_file_parser

place = "Istambul"
coordinates = [41.0082, 28.9784]
creator = "Elena, Nazli, Ipek and Fran"
year = 2023

# load the dataframes
df1 = pd.read_csv('csv/Turkey food.csv')
df2 = pd.read_csv('csv/Turkey.csv')


# concatenate the two dataframes
df_combined = pd.concat([df1, df2])

## display the combined dataframe
# print(df_combined)

# get the unique sections
unique_sections = df_combined['Note'].unique()
# print(unique_sections)

data = {}
for section in unique_sections:
    places_section = df_combined[df_combined['Note'] == section]
    places_comment_dict = places_section.set_index('Title')['Comment'].to_dict()
    data[section] = places_comment_dict



create_city = YAML_file_parser(coordinates, place, creator, year, data)
create_city.to_YAML()