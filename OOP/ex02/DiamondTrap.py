from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    "Long live the King but not you"
    def __init__(self, first_name):
        super().__init__(first_name)
    
    def set_eyes(self, color:str):
        self.eyes = color
    
    def set_hairs(self, color:str):
        self.hairs = color
    
    def get_eyes(self):
        return self.eyes
    
    def get_hairs(self):
        return self.hairs