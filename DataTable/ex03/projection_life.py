from load_csv import load
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import sys

def filter_data(data1: pd.DataFrame, data2: pd.DataFrame, year: int)-> pd.Series:
    pass

def projection_life(year:str):
    try:
        income_df = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        life_expectancy_df = load('life_expectancy_years.csv')
    except (Exception, OSError, FileNotFoundError):
        raise
    else:
        income_year_pp = income_df[year]
        life_expectancy_year = life_expectancy_df[year]
        print(type(income_year_pp))
        plt.figure(figsize=(8,6))
        plt.scatter(income_year_pp, life_expectancy_year)
        plt.title(year)
        plt.xlabel('Gross dpmestic product')
        plt.xscale('log')
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.ylabel('Life Expectancy')
        plt.tight_layout()

        plt.show()

def main():
    try:
        projection_life('1900')
    except (Exception, OSError, FileNotFoundError) as err:
        print(err)
    except KeyboardInterrupt:
        sys.exit("You have exited the program")

if __name__ == '__main__':
    main()