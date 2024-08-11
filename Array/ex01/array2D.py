import numpy as np

def check_subarr_len(lst: list) -> bool:
    ref = len(lst[0])
    for x in lst:
        if len(x) != ref:
            return False
    return True

def slice_me(family: list, start: int, end: int) -> list:
    if not check_subarr_len(family):
        raise Exception('Bad input')
    arr = np.array(family)
    print('My shape is : ', arr.shape)
    new_arr = arr[start:end]
    print('My new shape is : ', new_arr.shape)
    return (new_arr.tolist())

def main():
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(e)
    except:
        print('Error accure while slicing array')

if __name__ == "__main__":
    main()