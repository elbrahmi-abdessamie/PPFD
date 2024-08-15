
class Calculator:
    '''Calculator class the perfoms simple calc prerations'''
    def __init__(self, vec:list):
        self.vector = vec
    
    def __add__(self, object)-> None:
        self.vector = [num + object for num in self.vector]
        print(self.vector)
        return [num for num in self.vector]

    def __mul__(self, object)-> None:
        self.vector = [num * object for num in self.vector]
        print(self.vector)
        return [num for num in self.vector]
    
    def __sub__(self, object)-> None:
        self.vector = [num - object for num in self.vector]
        print(self.vector)
        return [num for num in self.vector]
    
    def __truediv__(self, object) -> None:
        try:
            self.vector = [num / object for num in self.vector]
            print(self.vector)
            return [num for num in self.vector]
        except ZeroDivisionError as err:
            print(ZeroDivisionError.__name__ + ' : float divition by zero not allowed')


