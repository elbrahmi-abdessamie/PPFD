def all_thing_is_obj(object: any) -> int:
    if isinstance(object, (str, float, set, list, dict, tuple)):
        type_string = str(type(object))
        type_name = type_string.split("'")[1].title()
        print(f"{object+'is in the kitchen' if type_name =='Str' else type_name} : {type_string}")
    else:
        print("Type not found")
    return 42
