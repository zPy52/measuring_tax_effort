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
- `International_Monetary_Fund/`
    - `IMF_GDP_Per_Capita.xlsx`: https://www.imf.org/external/datamapper/NGDPDPC@WEO/OEMDC/ADVEC/WEOWORLD
    - `IMF_GDP_Per_Capita_PPP.xlsx`: https://www.imf.org/external/datamapper/PPPPC@WEO/OEMDC/ADVEC/WEOWORLD
    - `IMF_GDP_Real_Growth.xlsx`: https://www.imf.org/external/datamapper/NGDP_RPCH@WEO/OEMDC/ADVEC/WEOWORLD
- `Our_World_In_Data/`
    - `OWID_Annual_Working_Hours_Per_Worker.csv`: https://ourworldindata.org/grapher/annual-working-hours-per-worker
    - `OWID_Human_Development_Index.csv`: https://ourworldindata.org/grapher/human-development-index?time=2017
    - `OWID_Total_Tax_Revenues_GDP.csv`: https://ourworldindata.org/grapher/total-tax-revenues-gdp
    - (Pendent) `OWID_Real_GDP_Per_Capita.csv`: https://ourworldindata.org/grapher/real-gdp-per-capita-pennwt?country=SGP~CHE~IRL~LUX~USA~KHM~BGD~BRA~IND~ZAF
- `World_Bank/`
    - `WB_Informal_Economy_Database.xlsx`: https://www.worldbank.org/en/research/brief/informal-economy-database -> (https://thedocs.worldbank.org/en/doc/37511318c092e6fd4ca3c60f0af0bea3-0350012021/related/informal-economy-database.xlsx)
    - `WB_Unemployment.xlsx`: https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS


**Note:** Some files were modified in order to facilitate or propitiate its utilization. For example, we have copied the content of every `.xls` file and pasted into a `.xlsx` file. That is because package `openpyxl` does not support the `.xls` type. Nonetheless, data was not altered in any way, in any case. Thus, their preprocessing does not affect the outcome sought.
