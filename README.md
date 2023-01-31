# (Paper title) Measuring Tax Effort

In this GitHub repository we include all datasets and code used for the analysis made on a paper to define and study the consecuences of a better definition of tax effort. 

The goal is to find relations between variables and see if they confirm an economic rationale. For example, assuming low tax effort tends to more economic activity and a faster capitalisation of economic agents, then wealth (measured as GDP) should grow in a faster pace than other countries with high tax effort and similar GDP per capita levels.

## Language & Packages
We employ Python to devise the logic of every program written. Some external packages are also utilised. These are versions installed:

- `Python`: 3.11.1
- `matplotlib`: 3.6.2
- `openpyxl`: 3.0.10
- `pandas`: 1.5.2
- `scikit-learn`: 1.2.0

Also, it's important to mention that all code has been executed and designed for its usage in a Windows 11 laptop.

The way to install packages in Python is by typing `py -m pip install <package_name>` on the Terminal or Command Prompt.

## Data sources
Data has been extracted from three main sources: International Monetary Fund, World Bank and OurWorldInData.org. Links to download pages are linked below (always select the option which downloads full dataset):
- `filename`: url


**Note:** Some files were modified in order to facilitate or propitiate its utilization. For example, we have copied the content of every `.xls` file and pasted into a `.xlsx` file. That is because package `openpyxl` does not support the `.xls` type. Nonetheless, data was not altered in any way, in any case. Thus, their preprocessing does not affect the outcome sought.
