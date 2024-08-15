from abc import ABC, abstractmethod

class Character(ABC):
    '''
    Abstract class Character
    '''
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Character Constructor'''
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die(self):
        '''Abstract method to be implement will change health stat to False'''
        ...
    
    def __str__(self):
        return str(f"Vector : ('{self.family_name}', '{self.eyes}', '{self.haire}')")
    
    def __repr__(self):
        return self.__str__()
    

class Stark(Character):
    '''Stark Character class.'''
    def __init__(self, first_name, is_alive=True):
        '''
Stark class constructor
Args:
    first_name (str): Stark mumber's first name
    is_alive (bool): Stark's health stat Default value is true
        '''
        super().__init__(first_name, is_alive)
    
    def die(self):
        '''Overrided method that change health stat to false'''
        self.is_alive = False
