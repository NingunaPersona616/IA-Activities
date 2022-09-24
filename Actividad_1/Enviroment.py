from random import randint


class Enviroment:
    def __init__(self):
        self.trash=randint(0,3)
        
    def isClean(self):
        if(self.trash > 0):
            return False
        return True