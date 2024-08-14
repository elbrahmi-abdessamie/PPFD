from load_csv import load
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import sys

def converter(value):
    '''
    Convert value sufix M & K to there cores values
    '''
    if isinstance(value, str):
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('k') or value.endswith('K'):
            return float(value[:-1]) * 1_000
        return float(value)

def filter_data(data1: pd.DataFrame, data2: pd.DataFrame, year: str)-> pd.Series:
    '''
    Filter DataFames by given year returns series dtype
    within an error while filtring Exception raised
    '''
    df_1 = data1[year]
    df_2 = data2[year]
    df_1 = df_1.map(converter)
    if df_1.size and df_2.size:
        return df_1, df_2
    raise Exception


def projection_life(year:str, *files):
    '''
    Load the files filter it in order to visualize data for a year
    given through scatter plots
    '''
    try:
        income_df = load(files[0])
        life_expectancy_df = load(files[1])
        income_pp_year, life_expectancy_year = filter_data(
            income_df, life_expectancy_df, year)
    except (Exception, OSError, FileNotFoundError):
        raise
    else:
        plt.figure(figsize=(14,8))
        plt.xscale('log')
        plt.scatter(income_pp_year, life_expectancy_year)
        plt.title(year)
        plt.xlabel('Gross dpmestic product')
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.ylabel('Life Expectancy')
        plt.show()

def main():
    try:
        projection_life('1900',
            'income_per_person_gdppercapita_ppp_inflation_adjusted.csv',
            'life_expectancy_years.csv')
    except (Exception, OSError, FileNotFoundError) as err:
        print(err)
    except KeyboardInterrupt:
        sys.exit("You have exited the program")

if __name__ == '__main__':
    main()