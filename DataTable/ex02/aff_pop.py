from load_csv import load
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def converter(value):
    '''
    Convert value sufix M & K to there cores values
    '''
    if isinstance(value, str):
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('K'):
            return float(value[:-1]) * 1_000
    return pd.to_numeric(value, errors='coerce')
    

def filter_data(data: pd.DataFrame, key1:str, key2:str):
    '''
    Filter dataframe to get two countries frames, replace any nan value with prev valid value
    then return the frames as numpy array
    '''
    filterd = data.loc[lambda data: (data['country'] == key1) | (data['country'] == key2)]
    filterd = filterd.map(converter)
    filterd.ffill(axis=1, inplace=True)
    return pd.array(filterd.to_numpy()[:,1:], dtype=float)
    

def aff_pop(country: str, ver_country:str):
    '''
    Load and filter datatable then plot it
    '''
    try:
        df = load('population_total.csv')
        data = filter_data(df, country, ver_country)
    except (Exception, OSError, FileNotFoundError):
        raise
    else:
        x_axis_range = np.arange(1800, 2101)
        plt.title('Population Projection')
        plt.xticks(np.arange(1800, 2100, 40)) 
        plt.plot(x_axis_range,data[0], color='#4169E1', label=country)
        plt.plot(x_axis_range,data[1], color='#FF4500', label=ver_country)
        plt.xlabel('Year')
        plt.ylabel('population')
        plt.yticks(np.arange(0, 80_000_000, 20_000_000))
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M' if x != 0 else f''))
        plt.legend()
        plt.show()

def main():
    try:
        aff_pop('France', 'Monaco')
    except (Exception, OSError, FileNotFoundError) as err:
        print(err)

if __name__ == '__main__':
    main()