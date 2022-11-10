from Nodo import *

class Tree:
    def __init__(self):
        initialState = [[3,1,2],[6,4,5],[0,7,8]]
        self.root = Node()
        self.root.setSolucion(initialState)

    def deepSearch(self):
        nodesList=[]
        nodesList.append(self.root.Data)
        
        result = self.root.expandNodes(nodesList,0)
        if isSolution(result):
            print("se encontro la solucion")