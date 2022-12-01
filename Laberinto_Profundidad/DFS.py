import copy
from Laberinto import *

class Nodo:
    def __init__(self, estado, nodoPadre):
        self.estado = estado
        self.moves = None
        self.nodoPadre  = nodoPadre
        self.nodos = []

    def setAcciones(self, estado, estados_explorados):
        fila, columna = estado
        #Movimientos disponibles en el laberinto. Derecha, Izquierda, Arriba y Abajo.
        movimientos = [(fila + 1, columna), (fila - 1, columna), (fila, columna + 1), (fila, columna - 1)] 
        #Se eligen los movimientos válidos para el estado actual y se almacenan en una lista que se regresa posteriormente.
        #Se agrega el movimiento si no ha sido explorado anteriormente, si no es un muro y si está dentro del rango del laberinto. 
        self.moves = [move for move in movimientos if move not in estados_explorados
                and move not in laberinto.muro and move[0] in range(laberinto.altura) and
                move[1] in range(laberinto.ancho)]
        #print(self.moves)


def DFS_Interface(estado, estadosExplorados):
    root = Nodo(estado, None)
    solution = DFS(root, estadosExplorados, 0)
    return solution
    

def DFS(nodoActual, estadosExplorados, depth):
    if depth == maxDepth:
        print("Murio")
        return None
    estadosExplorados.append(nodoActual.estado)
    
    if nodoActual.estado == laberinto.meta:   #Si encontro solucion
        Solution = copy.copy(nodoActual)
        return Solution
    
    nodoActual.setAcciones(nodoActual.estado, estadosExplorados)    #Busca a que coordenadas se puede mover desde el actual

    if not nodoActual.moves:  #Si el nodo actual no tiene movs
        return None

    else:   #Si se pueden generar movimientos con el nodo actual
        nodoSig = Nodo(None, None)
        for move in nodoActual.moves:   #Agregamos los nuevos nodos dependiendo de sus movimientos
            nodoSig.nodoPadre   = nodoActual
            nodoSig.estado      = move
            nodoActual.nodos.append(copy.copy(nodoSig))

            Solution = DFS(nodoSig, estadosExplorados, depth+1)

            if Solution is not None and Solution.estado == laberinto.meta:   #Si encontro solucion
                return Solution

    return None #Si ninguno de sus nodos tiene la solucion regresa none

laberinto = Laberinto('laberinto.txt')  
estados_explorados = []
ruta = []
maxDepth = 40
if __name__ == '__main__': 
    print("Laberinto inicial:")
    laberinto.dibujar_muros()  
    print("Inicio:", laberinto.inicio)
    print("Meta:", laberinto.meta)
    print()
    print("\nLaberinto resuelto:")
    solution = DFS_Interface(laberinto.inicio, estados_explorados)

    if solution is not None:
        ruta.append(solution.estado)
        Aux = solution.nodoPadre
        while True:
            if Aux.nodoPadre == None:
                ruta.append(Aux.estado)
                break
            else:
                ruta.append(Aux.estado)
                Aux = Aux.nodoPadre
    
        laberinto.dibujar_solucion(ruta, estados_explorados)
        print("\nLa ruta que recorrio fue:\n")
        print(ruta[::-1])
    else:
        print("El laberinto fallo y realizo la busqueda en todo esto:")
        laberinto.dibujar_falla(estados_explorados)