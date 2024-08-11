import math


def NULL_not_found(object: any)->int:
    return_val = 0
    type_name = type(object)
    if type_name is float and math.isnan(object):
        print(f"Cheese: {object} : {type_name}")
    elif type_name is str and len(object) == 0:
        print(f"Empty: {type_name}")
    elif type_name is int and not object:
        print(f"Empty: {object} {type_name}")
    elif type_name is bool and not object:
        print(f"Fake: {object} {type_name}")
    elif object is None:
        print(f"Nothing: {object} {type_name}")
    else:
        return_val = 1
        print("Type not found")
    return return_val
