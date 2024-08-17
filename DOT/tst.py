
class Data:
    def __init__(self, args:list=None):
        self.__index = self.__end = 0
        self.__args = args
        if isinstance(args, list):
            self.__end = len(args)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__args is None:
            raise Exception("No data are provided")
        if self.__index >= self.__end:
            raise StopIteration
        val = self.__args[self.__index]
        self.__index += 1
        return val

class Methods:
    def __init__(self, args:dict=None):
        self.__index = self.__end = 0
        self.__args = args
        self.__keys = list(args.keys())
        if isinstance(args, dict):
            self.__end = len(self.__keys)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__args is None:
            raise Exception("No data are provided")
        if self.__index >= self.__end:
            raise StopIteration
        val = self.__args[self.__keys[self.__index]]
        self.__index += 1
        return val

# for dt in Data([1,2,'3']):
#     print(dt)

for dt in Methods({1:'lol', 2:'alo'}):
    print(dt)