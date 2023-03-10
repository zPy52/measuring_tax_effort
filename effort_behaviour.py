# Import needed libraries.
from math import sqrt

import pandas as pd
import matplotlib.pyplot as plt

# Declare golden number.
PHI = (1 + sqrt(5)) / 2

# Tax effort formula.
tax_effort = lambda tax_burden, unemployment, gdp_ppp: b / ((1 - tax_burden) * (1 - unemployment) * (gdp_ppp ** PHI))

#  Use preprocessed data with columns:
# country, gdp_per_capita_ppp, tax_burden, hdi, unemployment
df = pd.read_csv('datasets/data.csv')

df = df.set_index('country', drop=False)

# Choose country (in this case, Spain).
country = 'Spain'
country_data = df.loc[country]

#  Build additional instances for the specified country with different tax burdens. 
# keeping all other information the same.
addons = []
for index, multiplier in enumerate([i / 10 for i in range(1, 21) if i != 10]):
    if index + 1 >= 10:
        index += 1

    sub_df = pd.DataFrame(
        {
            'country': [f'{country} x{(index + 1) / 10}'],
            'gdp_per_capita_ppp': [country_data['gdp_per_capita_ppp']],
            'tax_burden': [country_data['tax_burden'] * multiplier],
            'hdi': [country_data['hdi']],
            'unemployment': [country_data['unemployment']]
        }
    )
    
    addons.append(sub_df)

df = pd.concat((df, *addons), ignore_index=False, axis=0)

# Removing top 5 tax efforts.
df = df.drop(['Cambodia', 'India', 'Brazil', 'South Africa', 'Bangladesh'])

# Get country's tax effort.
countries_data = []
for country_data in df.to_dict('records'):
    b = country_data['tax_burden'] / 100
    u = country_data['unemployment'] / 100
    p = country_data['gdp_per_capita_ppp']

    countries_data.append([country_data['country'], tax_effort(b, u, p), country_data['tax_burden']])


# Format and plot tax burden-tax effort data.
df = pd.DataFrame(countries_data, columns=['country', 'tax_effort', 'tax burden'])

experiment_names = [data[0] for data in countries_data if country in data[0] and country != data[0]]

x = [data[2] for data in countries_data if country not in data[0]]
y = [data[1] for data in countries_data if country not in data[0]]

x2 = [data[2] for data in countries_data if country in data[0] and country != data[0]]
y2 = [data[1] for data in countries_data if country in data[0] and country != data[0]]

x3 = [data[2] for data in countries_data if country == data[0]]
y3 = [data[1] for data in countries_data if country == data[0]]

plt.scatter(x, y, color='lightblue')
plt.scatter(x2, y2, color='darkblue')
plt.scatter(x3, y3, color='darkgrey')

plt.xlabel('Tax Burden')
plt.ylabel('Tax Effort')


# Write country's name attached to its points.
ax = plt.gca()    
for i, txt in enumerate(experiment_names):
    ax.annotate(txt.replace(country, ''), (x2[i], y2[i]))

ax.annotate(country, (x3[0], y3[0]))

# Set a title and plot.
plt.title('Evolution of Tax Effort due to Tax Burden Increases')

plt.show()