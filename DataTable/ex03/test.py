from projection_life import projection_life as projection
import pandas as pd
import sys

def main():
    if len(sys.argv) > 2:
        sys.exit(f"One argument allowed but {len(sys.argv)} are given")
    elif len(sys.argv) < 2:
        sys.exit("No input year given")
    else:
        try:
            projection(sys.argv[1],
            'income_per_person_gdppercapita_ppp_inflation_adjusted.csv',
            'life_expectancy_years.csv')
        except (Exception, OSError, KeyboardInterrupt, FileNotFoundError) as err:
            pass

if __name__ == '__main__':
    main()