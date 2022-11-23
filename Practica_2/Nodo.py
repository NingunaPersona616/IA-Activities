import numpy as np

Upper_X=3
Upper_Y=3
maxLevel = 10
target = np.array([[0,1,2],[3,4,5],[6,7,8]]) #Estado objetivo

def copy(data):
    pass

def isSolution(n):
    if n is None:
        return False
    elif (n == target).all():
        return True

class Node:
    def __init__(self):
        self.Nodes = []
        self.Data = np.empty(0)
        self.x_Pos = None
        self.y_Pos = None

        # Flags para saber a donde se puede mover el espacio en blanco
        self.up = True
        self.down = True
        self.left = True
        self.right = True

    def isOpened(self, newData, openNodes):
        for node in openNodes:
            if (newData == node).all():
                return True
        return False

    def setSolucion(self, Solution):    #Considerar para el laberinto no buscar sino pasar como parametros las coordenadas
        self.Data = Solution

        for i in range(Upper_X):    #Busca donde se encuentra el espacio en blanco
            for j in range(Upper_Y):
                if self.Data[i][j] == 0:
                    self.x_Pos = i
                    self.y_Pos = j
                    break
        
        #print("Abriendo Nodo")
        #print(Solution, "\n")

        if self.x_Pos == 0: #si esta en el primer renglon no puede moverse hacia arriba
            self.up = False
        
        if self.x_Pos == Upper_X-1: #si esta en el ultimo renglon no puede moverse hacia abajo
            self.down = False

        if self.y_Pos == 0: #si esta en la primer columna no se puede mover a la izquierda
            self.left = False

        if self.y_Pos == Upper_Y-1:   #si esta en la ultima columna no se puede mover a la derecha
            self.right = False

    
    def expandNodes(self, openNodes, level, path):
        if level == maxLevel:
            return None

        #Si se puede mover hacia arriba
        if self.up == True:
            newData = np.copy(self.Data) #Copia de la data actual

            aux = newData[self.x_Pos-1][self.y_Pos] #guarda el dato que esta arriba de el
            newData[self.x_Pos-1][self.y_Pos] = 0  #mueve el espacio en blanco hacia arriba
            newData[self.x_Pos][self.y_Pos] = aux  #mueve el de arriba hacia abajo


            if isSolution(newData):
                #print("Solucion")
                #print(newData, "\n")
                return newData

            #Suponiendo que in hace comparaciones de matrices uno a uno
            if(self.isOpened(newData, openNodes)) == False:    #Si el nodo por abir no ha sido abierto
                newNode = Node()                
                newNode.setSolucion(newData)    #Guarda el nuevo nodo
                self.Nodes.append(newNode)
                openNodes.append(newData)

                result = self.Nodes[0].expandNodes(openNodes, level+1, path) #Expandimos el nuevo nodo creado y busca la sol en sus hijos

                if isSolution(result):
                    path.append(newNode.Data)
                    return result

                #Quitamos los nodos que no son solucion?
                #openNodes.pop(0)
                #self.Nodes.pop(0)

        #Si se puede mover hacia abajo
        if self.down == True:
            newData = np.copy(self.Data) #Copia de la data actual

            aux = newData[self.x_Pos+1][self.y_Pos] #guarda el dato que esta abajo de el
            newData[self.x_Pos+1][self.y_Pos] = 0  #mueve el espacio en blanco hacia abajo
            newData[self.x_Pos][self.y_Pos] = aux  #mueve el de abajo hacia arriba

            if isSolution(newData):
                #print("Solucion")
                #print(newData, "\n")
                return newData

            if(self.isOpened(newData, openNodes)) == False:     #Si el nodo por abir no ha sido abierto
                newNode = Node()                
                newNode.setSolucion(newData)    #Guarda el nuevo nodo
                self.Nodes.append(newNode)
                openNodes.append(newData)

                result = self.Nodes[0].expandNodes(openNodes, level+1, path) #Expandimos el nuevo nodo creado y busca la sol en sus hijos

                if isSolution(result):
                    path.append(newNode.Data)
                    return result

                #Quitamos los nodos que no son solucion?
                #openNodes.pop(0)
                #self.Nodes.pop(0)

        #Si se puede mover hacia la izquierda
        if self.left == True:
            newData = np.copy(self.Data) #Copia de la data actual

            aux = newData[self.x_Pos][self.y_Pos-1] #guarda el dato que esta a su izquierda
            newData[self.x_Pos][self.y_Pos-1] = 0   #mueve el espacio en blanco hacia la izquierda
            newData[self.x_Pos][self.y_Pos] = aux   #mueve el dato hacia la derecha

            if isSolution(newData):
                #print("Solucion")
                #print(newData, "\n")
                return newData

            if(self.isOpened(newData, openNodes)) == False:    #Si el nodo por abir no ha sido abierto
                newNode = Node()                
                newNode.setSolucion(newData)    #Guarda el nuevo nodo
                self.Nodes.append(newNode)
                openNodes.append(newData)

                result = self.Nodes[0].expandNodes(openNodes, level+1, path) #Expandimos el nuevo nodo creado y busca la sol en sus hijos

                if isSolution(result):
                    path.append(newNode.Data)
                    return result

                #Quitamos los nodos que no son solucion?
                #openNodes.pop(0)
                #self.Nodes.pop(0)
        
        #Si se pude mover a la derecha
        if self.right == True:
            newData = np.copy(self.Data) #Copia de la data actual
            
            aux = newData[self.x_Pos][self.y_Pos+1] #Copia el dato de su derecha
            newData[self.x_Pos][self.y_Pos+1] = 0     #Mueve el espacio en blanco a la derecha
            newData[self.x_Pos][self.y_Pos] = aux  #Mueve el otro dato a la izquiera

            if isSolution(newData):
                #print("Solucion")
                #print(newData, "\n")
                return newData

            #Suponiendo que in hace comparaciones de matrices uno a uno
            if(self.isOpened(newData, openNodes)) == False:    #Si el nodo por abir no ha sido abierto
                newNode = Node()                
                newNode.setSolucion(newData)    #Guarda el nuevo nodo
                self.Nodes.append(newNode)
                openNodes.append(newData)

                result = self.Nodes[0].expandNodes(openNodes, level+1, path) #Expandimos el nuevo nodo creado y busca la sol en sus hijos

                if isSolution(result):
                    path.append(newNode.Data)
                    return result

                #Quitamos los nodos que no son solucion?
                #openNodes.pop(0)
                #self.Nodes.pop(0)
        
        return None #Si ningun nodo es solucion regresa []

        #FALTA BORRAR LOS NODOS CUANDO VENGA DE REGRESO EN EL BACKTRACKING