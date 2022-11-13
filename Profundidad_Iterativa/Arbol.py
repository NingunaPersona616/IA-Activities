from Nodo import *

initialState = np.array([[1,2,5],[3,4,8],[6,7,0]])

class Tree:
    def __init__(self):
        self.root = Node()
        self.root.setSolucion(initialState)
        self.nodesList=[]
        self.nodesList.append(self.root.Data)
        self.path=[]

    def iterativeDeepSearch(self, max_depth):
        for i in range(1,max_depth+1):
            #print("nivel:", i)
            result = self.root.expandNodes(self.nodesList, 0, self.path, i)
            if isSolution(result):
                print("se encontro la solucion en el nivel:", i)

                print(initialState, '\n')
                for node in reversed(self.path):
                    print(node, "\n")
                print(target)
                return
            self.nodesList=[]   #Reinicia la lista de nodos abiertos

        print("No encontro solucion")