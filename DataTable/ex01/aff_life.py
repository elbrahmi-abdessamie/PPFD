from load_csv import load
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_country_frame(data: pd.DataFrame, country: str)->np.ndarray:
    '''
    Filter dataframe by country name given then return that frame as numpy array
    '''
    country_frame = data.loc[data['country'] == country].to_numpy()[:,1:]
    if country_frame.size:
        return pd.array(country_frame, dtype=float)[0]
    else:
        raise Exception(f'You gave wrong Country name | {country} |')

def aff_life(country: str):
    '''
    Display the country information and present it as graph
    '''
    try:
        df = load('life_expectancy_years.csv')
        c_frame = get_country_frame(df, country)
    except (Exception, OSError, FileNotFoundError):
        raise
    else:
        x_axis_range = np.arange(1800, 2101)
        plt.title(country + ' Life expectancy Projections')
        plt.xticks(np.arange(1800, 2100, 40)) 
        plt.plot(x_axis_range,c_frame)
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.yticks(np.arange(30, 100, 10)) 
        plt.show()


def main():
    try:
        aff_life('France')

    except (Exception, OSError, FileNotFoundError) as err:
        print(err)

if __name__ == '__main__':
    main()