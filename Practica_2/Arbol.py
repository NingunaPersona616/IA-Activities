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
        print("Estado inicial:")
        print(initialState, '\n')
        result = self.root.expandNodes(self.nodesList,0, self.path)
        if isSolution(result):
            print("se encontro la solucion, y su camino es:")

            print(initialState, '\n')
            for node in reversed(self.path):
                print(node, "\n")
            print(target)