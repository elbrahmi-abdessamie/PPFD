
# def alo(string:str):
#     return 'smash ' + string

# def skip(string: str):
#     return "wrong choice fuck u"

# uppercase = str.upper
# lowercase = str.lower

# transform = [skip, uppercase, lowercase, alo]

# # transform['random']("Hello")

# def transform_max(func, string):
#     print(func(string))


# def pick_amove(choice:str) -> int:
#     index = 1 * (choice == "upper") + 2 * (choice == 'lower') + 3 * (choice == 'random') 
#     return index

# string_to_process = input("Enter ur input here: ")
# choice = input("Enter action ( upper, lower or random): ")
# choice = pick_amove(choice)
# transform_max(transform[choice], string_to_process)

def print_str(string):
    print(string)

def nobody(string):
    string = string.upper()
    def transform(func, string1):
        return func(string1)
    return transform

nobody('hello')(print_str, 'waaaa zebi')

