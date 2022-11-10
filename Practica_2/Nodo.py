Upper_X=3
Upper_Y=3
maxLevel = 100


class Node:
    def __init__(self):
        self.Nodes = []
        self.Data = None
        self.x_Pos = None
        self.y_Pos = None

        # Flags para saber a donde se puede mover el espacio en blanco
        self.up = True
        self.down = True
        self.left = True
        self.right = True


    def setSolucion(self, Solution):
        self.Data = Solution

        for i in range(Upper_X):    #Busca donde se encuentra el espacio en blanco
            for j in range(Upper_Y):
                if self.Data[i][j] == 0:
                    position = {"X":i, "Y":j}
                    break
        
        self.x_Pos = position["X"]
        self.y_Pos = position["Y"]

        if self.x_Pos == 0: #si esta en el primer renglon no puede moverse hacia arriba
            self.up = False
        
        if self.x_Pos == Upper_X: #si esta en el ultimo renglon no puede moverse hacia abajo
            self.down = False

        if self.y_Pos == 0: #si esta en la primer columna no se puede mover a la izquierda
            self.left = False

        if self.y_Pos == Upper_Y:   #si esta en la ultima columna no se puede mover a la derecha
            self.right = False

    
    def expandNodes(self, openNodes, level):
        if level == maxLevel:
            return

        #Hacer esto para cada caso y rezar pq funcione
        if self.up == True:
            newData = self.Data #Copia de la data actual

            aux = newData[self.x_Pos-1][self.y_Pos] #guarda el dato que esta arriba de el
            newData[self.x_Pos-1][self.y_Pos] = 0  #mueve el espacio en blanco hacia arriba
            newData[self.x_Pos][self.y_Pos] = aux  #mueve el de arriba hacia abajo

            #Suponiendo que in hace comparaciones de matrices uno a uno
            if newData in openNodes == False:    #Si el nodo por abir no ha sido abierto
                newNode = Node()                
                newNode.setSolucion(newData)    #Guarda el nuevo nodo

                self.Nodes.append(newNode)
                openNodes.append(newData)
                self.Nodes[0].expandNodes(openNodes, level+1) #Expandimos el nuevo nodo creado

        #Si sue puede mover hacia abajo
        if self.down == True:
            newData = self.Data

            aux = newData[self.x_Pos+1][self.y_Pos] #guarda el dato que esta abajo de el
            newData[self.x_Pos+1][self.y_Pos] = 0  #mueve el espacio en blanco hacia abajo
            newData[self.x_Pos][self.y_Pos] = aux  #mueve el de abajo hacia arriba

            if newData in openNodes == False:    #Si el nodo por abir no ha sido abierto
                newNode = Node()                
                newNode.setSolucion(newData)    #Guarda el nuevo nodo

                self.Nodes.append(newNode)
                openNodes.append(newData)
                self.Nodes[0].expandNodes(openNodes, level+1) #Expandimos el nuevo nodo creado

        #Si sue puede mover hacia la izquierda
        if self.left == True:
            aux = newData[self.x_Pos][self.y_Pos-1] #guarda el dato que esta a su izquierda
            newData[self.x_Pos][self.y_Pos-1] = 0   #mueve el espacio en blanco hacia la izquierda
            newData[self.x_Pos][self.y_Pos] = aux   #mueve el dato hacia la derecha

            if newData in openNodes == False:    #Si el nodo por abir no ha sido abierto
                newNode = Node()                
                newNode.setSolucion(newData)    #Guarda el nuevo nodo

                self.Nodes.append(newNode)
                openNodes.append(newData)
                self.Nodes[0].expandNodes(openNodes, level+1) #Expandimos el nuevo nodo creado
        pass

        #FALTA BORRAR LOS NODOS CUANDO VENGA DE REGRESE EN EL BACKTRACKING