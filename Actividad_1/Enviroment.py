class Enviroment:
    def __init__(self, trash):
        self.trash = trash
        
    def isClean(self):
        if(self.trash > 0):
            return False
        return True