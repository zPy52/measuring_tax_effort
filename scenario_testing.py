# Import sqrt from math library.
from math import sqrt

# Use it to hold the golden number.
PHI = (1 + sqrt(5)) / 2 

# Ask the user what scenario he/she would like to see.
scenario = int(input('Type what scenario you would like to analyse (1, 2 or 3): '))

# Ensure the chosen scenario is one of the available.
assert scenario in {1, 2, 3}, 'Given option is not one of the available'

# Define tax effort function (omega).
te = lambda tax_burden, unemployment, gdp_ppp: tax_burden / ((1 - tax_burden) * (1 - unemployment) * (gdp_ppp ** PHI))


### A, B and C ###
if scenario == 1:
    C1 = te(0.1, 0.05, 1_250)
    C2 = te(0.1, 0.05, 10_000)
    C3 = te(0.1, 0.05, 50_000)

    print('Tax Efforts:', f'  - A: {C1}', f'  - B: {C2}', f'  - C: {C3}', sep='\n')

    print('Relations:', f'  - A to B: {C1 / C2}', f'  - A to C: {C1 / C3}', f'  - B to C: {C2 / C3}', sep='\n')


### D, E, F, G ###
if scenario == 2:
    C1 = te(0.5, 0.05, 20_000)
    C2 = te(0.33, 0.05, 20_000)
    C3 = te(0.1, 0.05, 20_000)
    C4 = te(0.01, 0.05, 20_000)

    print('Tax Efforts:', f'  - D: {C1}', f'  - E: {C2}', f'  - F: {C3}', f'  - G: {C4}', sep='\n')

    print('Relations:', f'  - D to E: {C1 / C2}', f'  - D to F: {C1 / C3}', f'  - D to G: {C1 / C4}',
                f'  - E to F: {C2 / C3}', f'  - E to G: {C2 / C4}', f'  - F to G: {C3 / C4}', sep='\n')


### H, I, J, K ###
if scenario == 3:
    C1 = te(0.1, 0.33, 20_000)
    C2 = te(0.1, 0.2, 20_000)
    C3 = te(0.1, 0.1, 20_000)
    C4 = te(0.1, 0.025, 20_000)

    print('Tax Efforts:', f'  - H: {C1}', f'  - I: {C2}', f'  - J: {C3}', f'  - K: {C4}', sep='\n')

    print('Relations:', f'  - H to I: {C1 / C2}', f'  - H to J: {C1 / C3}', f'  - H to K: {C1 / C4}',
                f'  - I to J: {C2 / C3}', f'  - I to K: {C2 / C4}', f'  - J to K: {C3 / C4}', sep='\n')