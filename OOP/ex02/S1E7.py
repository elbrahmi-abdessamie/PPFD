from S1E9 import Character

class Baratheon(Character):
    '''Baratheon Character'''
    def __init__(self, first_name, is_alive=True):
        '''Baratheon Constructor'''
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
    
    def die(self):
        '''Overrided method that change health stat to false'''
        self.is_alive = False
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()


class Lannister(Character):
    '''Lannister Character'''
    def __init__(self, first_name, is_alive=True):
        '''Lannister Constructor'''
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
    
    def die(self):
        '''Overrided method that change health stat to false'''
        self.is_alive = False
    
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        '''A Class method for Lannister character creation'''
        return cls(first_name, is_alive)
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()