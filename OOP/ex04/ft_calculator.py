
class calculator:
    '''Class calculator'''


    @staticmethod
    def dotproduct(V1: list[float], V2: list[float])-> None:
        dotproduct = 0
        for idx in range(len(V1)):
            dotproduct += V1[idx] * V2[idx]
        print(f'Dot product is: {dotproduct}')
        return dotproduct
    
    @staticmethod
    def add_vec(V1: list[float], V2: list[float])-> None:
        new_vec = []
        for idx in range(len(V1)):
            new_vec.append(V1[idx] + V2[idx])
        print('Add Vector is : ', [float(val) for val in new_vec])
        return new_vec
    
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float])-> None:
        new_vec = []
        for idx in range(len(V1)):
            new_vec.append(V1[idx] - V2[idx])
        print(f"Sous Vector is : {[float(val) for val in new_vec]}")
        
        return new_vec