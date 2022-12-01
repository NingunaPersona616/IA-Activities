import copy
from collections import deque
from Laberinto import *
laberinto = Laberinto('laberinto.txt')  
estados_explorados = []
ruta = []


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


def BFS(estado, estadosExplorados):
    root = Nodo(estado, None)
    nodoActual = root
    candidatos = deque()
    candidatos.append(copy.copy(nodoActual))

    i = 0
    while True:
        #print(nodoActual.estado)
        if len(candidatos) == 0:    #Si ya no hay mas candidatos
            print("\nNo hay solución.")
            return None
        
        elif nodoActual.estado == laberinto.meta:   #Si encontro solucion
            print("\nSi se encontro solución en la iteracion:", i)
            print("\nCon un total de ", len(estadosExplorados), "Nodos visitados")
            Solution = copy.copy(nodoActual)
            return Solution
        
        nodoActual.setAcciones(nodoActual.estado, estadosExplorados)    #Busca a que coordenadas se puede mover desde el actual

        if not nodoActual.moves:  #Si el nodo actual no tiene movs
            candidatos.popleft()    #Quitamos el nodo recien agregado porque es un nodo Nulo

        else:   #Si se pueden generar movimientos con el nodo actual
            aux = Nodo(None, None)
            for move in nodoActual.moves:   #Agregamos los nuevos nodos dependiendo de sus movimientos
                aux.nodoPadre   = nodoActual
                aux.estado      = move
                candidatos.append(copy.copy(aux))
                nodoActual.nodos.append(copy.copy(aux))
                estadosExplorados.append(aux.estado)

            candidatos.popleft()    #Eliminamos el nodoActual de los candidatos

        if len(candidatos) > 0: #Si aun quedan candidatos
            nodoActual = candidatos[0]

        i += 1
        if i == 1000:
            print("Murio")
            return

if __name__ == '__main__': 
    print("Laberinto inicial:")
    laberinto.dibujar_muros()  
    print("Inicio:", laberinto.inicio)
    print("Meta:", laberinto.meta)
    print()
    print("\nLaberinto resuelto:")
    solution = BFS(laberinto.inicio, estados_explorados)

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