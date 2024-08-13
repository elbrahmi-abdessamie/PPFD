import pandas as pd
import numpy as np


def path_validitor(path: str, function: None):
    '''
    Checks if path contains csv extention
    '''
    extention_is_valid = function(path)
    if not extention_is_valid:
        raise Exception("Invalide file format missing csv extension")
    elif len(path) < 4:
        raise Exception("Invalide file")

def load(path: str) -> pd.DataFrame | None:
    '''
    Validate path extention then check file 
    '''
    try:
        path_validitor(path, lambda string: string[-3:] == 'csv')
        fd = open(path, 'r')
        fd.close()
    except (Exception, OSError, FileNotFoundError):
        raise
    else:
        return (pd.read_csv(path))

def main():
    try:
        df = load('life_expectancy_years.csv')
        blanck = [''] * len(df)
        df.index = blanck
        print(f"Loading dataset of dimensions {df.shape}", df.head(), sep='\n')
    except (Exception, OSError, FileNotFoundError) as err:
        print(err)

if __name__ == '__main__':
    main()