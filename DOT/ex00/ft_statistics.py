
class Data:
    def __init__(self, args:tuple=None):
        self.__args = args

    def get_data(self):
        return self.__args



class DataValidator:
    @staticmethod
    def validator(data:Data):
        vals = data.get_data()
        if not vals:
            return None
        for val in vals:
            if not isinstance(val, (int, float)):
                return None
        return [arg for arg in vals]

class Methods:
    def __init__(self, args:dict=None):
        self.__args = args
    
    def get_methods(self):
        if not self.__args:
            return None
        return self.__args
            
class StatisticTools:

    @staticmethod
    def mean_find(data: list):
        sum = 0
        for val in data:
            sum += val
        return sum / len(data)

    @staticmethod
    def mean(data: list):
        if not data:
            raise Exception('ERROR')
        print(f'mean: {StatisticTools.mean_find(data)}')

    @staticmethod
    def median(data: list):
        if not data:
            raise Exception('ERROR')
        data.sort()
        median_val = 0
        data_len = len(data)
        if data_len % 2:
            median_val = data[data_len//2]
        else:
            median_val = (data[data_len//2] + data[data_len//2 - 1])//2
        print(f"median: {median_val}")


    @staticmethod
    def quartile(data: list):
        if not data:
            raise Exception('ERROR')
        data.sort()
        loewr_quartile = int((len(data)) * (1/4))
        upper_quartile = int((len(data)) * (3/4))
        print(
        f'quartile : [{float(data[loewr_quartile])}, {float(data[upper_quartile])}]'
        )

    @staticmethod
    def calc_variance(data: list):
        mean = StatisticTools.mean_find(data)
        variance = 0
        for val in data:
            variance += ((val - mean) ** 2)
        variance /= len(data)
        return variance

    @staticmethod
    def std(data: list):
        if not data:
            raise Exception('ERROR')
        standard_deviation = StatisticTools.calc_variance(data)
        print(f'std : { standard_deviation ** 0.5}')
    
    @staticmethod
    def variance(data: list):
        if not data:
            raise Exception('ERROR')
        print(f"var : {StatisticTools.calc_variance(data)}")
        
class MethodsMaper:

    @staticmethod    
    def mapper(methodArgs: Methods):
        methods = {
            'mean': StatisticTools.mean,
            'median': StatisticTools.median,
            'quartile': StatisticTools.quartile,
            'std': StatisticTools.std,
            'var': StatisticTools.variance
            }
        meth_args = methodArgs.get_methods()
        for key, val in meth_args.items():
            if val in methods:
                yield methods[val]


def ft_statistics(*args: any, **kwargs: any)-> None:
    value = DataValidator.validator(Data(args))
    if not kwargs:
        print('ERROR')
        return
    tools = MethodsMaper.mapper(Methods(kwargs))
    for tool in tools:
        try:
            tool(value)
        except Exception as ex:
            print(ex)

def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == '__main__':
    main()
# StatisticTools.mean(([1,2,3]))


# for dt in Methods({1:'lol', 2:'alo'}):
#     print(dt)