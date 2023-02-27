from csv import DictReader
from dataclasses import dataclass
from typing import List
from copy import deepcopy

import pandas as pd

@dataclass
class Country:
    name: str
    starting_year: int
    history: List[float]

print('--- Real GDP Evolution And Average Historical Tax Effort ---')

with open('datasets/Our_World_In_Data/OWID_Real_GDP_Per_Capita.csv', 'r') as file:
    data = DictReader(file)

    countries_to_analyse = ('Singapore', 'Ireland', 'Luxembourg', 'Switzerland', 'South Korea', 
                                'Bangladesh', 'South Africa', 'Brazil', 'India', 'Cambodia')

    countries_data = {country: [] for country in countries_to_analyse}

    starting_years = {}

    for row in data:
        country_name = row['Entity']
        if country_name in countries_to_analyse:
            starting_years.setdefault(country_name, int(row['Year']))
            countries_data[country_name].append(float(row['GDP per capita (output, multiple price benchmarks)']))
    
countries = [Country(country_name, starting_years[country_name], countries_data[country_name]) 
                for country_name in countries_to_analyse]

#  Tables with data. First element corresponds to low-effort countries; 
# the second element to high-effort countries.
dfs = [{'Country': [], 'Starting Year': [], 'Starting GDP': [], 'GDP Multiplication Divided By Time Passed': []}]
dfs.append(deepcopy(dfs[0]))

for i, country in enumerate(countries):
    # Real GDP growth divided by number of years, in base 100. 
    """print(f'  - {country.name} ({country.starting_year}) - (Starting GDP ${country.history[0]:,.2f}):',
                f'{100 * (country.history[-1] / country.history[0]) / len(country.history)}')"""
    
    df_index = 0
    if i >= 5:
        df_index = 1
    
    # Add data to a pandas DataFrame.
    dfs[df_index]['Country'].append(country.name)
    dfs[df_index]['Starting Year'].append(country.starting_year)
    dfs[df_index]['Starting GDP'].append(f'${country.history[0]:,.2f}')
    dfs[df_index]['GDP Multiplication Divided By Time Passed'].append(
        100 * (country.history[-1] / country.history[0]) / len(country.history)
    )

dfs[0] = pd.DataFrame(dfs[0])
dfs[1] = pd.DataFrame(dfs[1])

print('Low-effort countries:', dfs[0], '', 'High-effort countries:', dfs[1], sep='\n')