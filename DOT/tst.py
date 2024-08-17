
class Data:
    def __init__(self, args:list=None):
        self.__args = args

    def get_data(self):
        return self.__args


class Methods:
    def __init__(self, args:dict=None):
        self.__args = args
    
    def get_methods(self):
        return self.__args

class StatisticTools:

    @staticmethod
    def mean(data: Data):
        print(data.get_data())
        pass

    @staticmethod
    def median(data: Data):
        pass

    @staticmethod
    def quartile(data: Data):
        pass

    @staticmethod
    def std(data: Data):
        pass
        

StatisticTools.mean(Data([1,2,3]))


# for dt in Methods({1:'lol', 2:'alo'}):
#     print(dt)