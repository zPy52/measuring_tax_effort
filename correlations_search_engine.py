# Import libraries we will use.
from math import sqrt, pi, e
from decimal import Decimal
from typing import Tuple

import pandas as pd

#  The golden number is not included in the math library, so 
# we calculate and hold it in a variable.
PHI = (1 + sqrt(5)) / 2

# Function to test correlations.
def main(exponent: float or int) -> Tuple[float or int]:
    # Tax effort function.
    tax_effort = lambda tax_burden, unemployment, gdp_ppp: tax_burden / ((1 - tax_burden) * (1 - unemployment) * (gdp_ppp ** exponent))

    # Get countries' data with which we will obtain their tax efforts.
    df = pd.read_csv('data_extractor/data.csv')

    # Relevant data of countries.
    countries_data = []

    #  Calculate the tax efforts and get Human Development Index to find if there is
    # a correlation, and which exponent returns the highest.
    for country_data in df.to_dict('records'):
        tax_burden = country_data['tax_burden'] / 100
        unemployment = country_data['unemployment'] / 100
        gdp_ppp = country_data['gdp_per_capita_ppp']

        countries_data.append([tax_effort(tax_burden, unemployment, gdp_ppp), country_data['hdi']])

    # Final DataFrame with relevant data.
    df = pd.DataFrame(countries_data, columns=['tax_effort', 'human development'])

    # Return a tuple with correlations.
    return (
        df.corr(method='pearson').to_dict('records')[0]['human development'],
        df.corr(method='spearman').to_dict('records')[0]['human development'],
        df.corr(method='kendall').to_dict('records')[0]['human development']
    )

# Dictionary to hold exponents and their results.
exponents = {}

#  Create a list of indexes growing 0.01 every time
# until reaching 50.05.
indexes = [Decimal('1')]
cap = Decimal('50.05')

# Include golden number, e and pi.
phi_done = False
e_done = False
pi_done = False

# Add them to the indexes list.
while indexes[-1] < cap:
    addon = indexes[-1] + Decimal('0.01')
    indexes.append(addon)

    if addon < PHI and not phi_done:
        indexes.append(Decimal(str(PHI)))
        phi_done = True

    if addon < e and not e_done:
        indexes.append(Decimal(str(e)))
        e_done = True

    if addon < pi and not pi_done:
        indexes.append(Decimal(str(pi)))
        pi_done = True
        
# Try with each exponent in the list.
for i in indexes:
    dat = main(float(i))
    exponents[i] = (dat[0], dat[1], dat[2])

# Pearson, Spearman and Kendall maximum and minimum values.
pearson_max = sorted(list(exponents.keys()), key=lambda k: exponents[k][0])[-1]
spearman_max = sorted(list(exponents.keys()), key=lambda k: exponents[k][1])[-1]
kendall_max = sorted(list(exponents.keys()), key=lambda k: exponents[k][2])[-1]

pearson_min = sorted(list(exponents.keys()), key=lambda k: exponents[k][0])[0]
spearman_min = sorted(list(exponents.keys()), key=lambda k: exponents[k][1])[0]
kendall_min = sorted(list(exponents.keys()), key=lambda k: exponents[k][2])[0]

# Show every correlation out of the ones before.
print('Pearson max -> exponent =', pearson_max)
print('Spearman max -> exponent =', spearman_max)
print('Kendall max -> exponent =', kendall_max)

print('-----')

print('Pearson min -> exponent =', f'*{pearson_min}* (Chosen exponent)')
print('Spearman min -> exponent =', spearman_min)
print('Kendall min -> exponent =', kendall_min)

print('-----')

print("Pearson's maximum value according to its exponent", main(float(pearson_max)))
print("Pearson's minimum value according to its exponent", main(float(pearson_min)))

'''
    Conclusion: We have chosen the golden number as an exponent because it is the one 
that makes the most sense. The lower the effort experienced by citizens, the higher
their life conditions must be; and therefore, there should appear a linear, negative 
correlation. And that happens with exponent = PHI, with a -0.77 Pearson correlation
and a -0.80 Spearman correlation. 
'''