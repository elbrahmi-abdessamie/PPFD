import numpy as np

def type_checker(lst: list) -> bool:
    np_arr = np.array(lst)
    return np.issubdtype(np_arr.dtype, np.number) and not np_arr.dtype == np.complex128

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise Exception('bad input lists lenght do not match')
    elif not type_checker(height) or not type_checker(weight):
        raise TypeError('bad input type')
    else:
        np_weight = np.array(weight)
        np_height = np.square(height)
        return list(np.divide(np_weight, np_height))

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [bool(x > limit) for x in bmi]

def main():
    try:
        res = (give_bmi([2.71, 1.15], [165.3, 38.4]))
        print(apply_limit(res, 26))
    except (Exception, TypeError) as err:
        print(err)

if __name__ == '__main__':
    main()
