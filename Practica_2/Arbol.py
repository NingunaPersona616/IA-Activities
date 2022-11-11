from Nodo import *

initialState = np.array([[1,2,5],[3,4,8],[6,7,0]])

class Tree:
    def __init__(self):
        self.root = Node()
        self.root.setSolucion(initialState)
        self.nodesList=[]
        self.nodesList.append(self.root.Data)
        self.path=[]

    def deepSearch(self):
        result = self.root.expandNodes(self.nodesList,0, self.path)
        if isSolution(result):
            print("se encontro la solucion")

            print(target, '\n')
            for node in self.path:
                print(node, "\n")
            print(initialState)