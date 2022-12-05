import copy             #Función especial para copiar varios elementos.
import time             #biblioteca para importar las funciones de Tiempo.
import random           #Biblioteca con la que se elige un orden aleatorio de números del 0-8 para el 8-puzzle.

def mostrarNodo(node):    #Función para imprimir el estado actual del 8 Puzzle
    print(node[0],node[1],node[2])
    print(node[3],node[4],node[5])
    print(node[6],node[7],node[8])
    global numeroNodos
    print('Nodo:', numeroNodos)
    print('Profundidad:', len(node[9:]))
    print('Nodos Visitados:', node[9:])
    print('------')
    numeroNodos += 1

def NodoObjetivo(node):               #Función para revisar si el nodo actual es el estado objetivo
    if node[:9]==nodoFinal:         #Si todos los elementos desde el inicio hasta el final-1 son iguales a los elementos del estado objetivo entonces se encontró la solución.
        mostrarNodo(node)
        return True
    if node[:9] not in listaVisitados: #Si los nodos desde el primer elemento hasta el último elemento del nodo no están 
        mostrarNodo(node)              #en visitados se muestra el nodo, se agrega a la cola y se agrega a la lista de visitados.
        listaNodos.append(node)        #Agregamos el nodo a la lista de nodos.
        listaVisitados.append(node[:9])#Agregamos el nodo a la lista de visitados.
    return False

def calcularHeuristica(node):            #Función para calcular la heurística.
    distance = 0                        #Variable en la que se guardará el valor de la heurística.
    for actual, objetivo in enumerate(node):#Hacemos un ciclo for que recorra todos los valores en el nodo con dos variables, una actual y otra objetivo.
        currentRow = int(actual/3)          #Dividimos el valor del elemento x entre tres. 
        currentColumn = actual%3            #Hacemos el módulo al valor del elemento x entre tres.
        targetRow = int(objetivo/3)         #Dividimos el valor del elemento x entre tres.
        targetColumn = objetivo%3           #Hacemos el módulo al valor del elemento x entre tres.
        distance += abs(currentRow-targetRow) + abs(currentColumn-targetColumn) #Hacemos que distancia sume el valor absoluto de la resta entre el valor actual y el valor final.
    return distance #Retornamos el valor de distancia.
    

if __name__ == '__main__':
    numbers = [0,1,2,3,4,5,6,7,8]   #Declaracón del arreglo de números válidos en el 8 Puzzle.

    #nodoInicial = random.sample(numbers,9)   #Elección aleatoria del orden de los números para el 8 Puzzle.
    nodoFinal = [0,1,2,3,4,5,6,7,8]          #Declaración del estado objetivo.
    nodoInicial = [8,0,4,2,3,1,7,5,6]       #Ejemplo sencillo

    print('B Ú S Q U E D A    A* ')

    estadoFinalEncontrado = False        #Bandera para cuando se encuentre el nodo/estado objetivo.
    numeroNodos = 0                      #Para contar los nodos que hemos visitado.
    listaVisitados = []                  #Declaración de la lista de nodos visitados.
    listaNodos = []                      #Declaración de la lista de nodos disponibles que se pueden expandir. Sirve como una cola de prioridad.
    listaNodos.append(nodoInicial)       #Agregamos el estado inicial del nodo a la lista de nodos disponibles que se pueden expandir.
    listaVisitados.append(nodoInicial)   #Agregamos el estado inicial del nodo a la lista de visitados.
    mostrarNodo(nodoInicial)             #Imprimimos el nodo inicial.
    print('\n\n^ Este es el nodo inicial ^\n\n')
    time_duration = 3.0
    time.sleep(time_duration)            #Pausar un momento la ejecución del programa.
    tInicio = time.time()                #Obtención del tiempo de inicio del programa.

    estadoFinalEncontrado = NodoObjetivo(nodoInicial)              #Revisamos si el primer estado no es un estado objetivo.

    while (not estadoFinalEncontrado and not len(listaNodos)==0):            #Mientras no se haya encontrado el estado final y la lista no esté vacia, hacer...
        fList = []                                                           #Creamos una lista para almacenar los valores de la heurística.
        for node in listaNodos:                                              #Hacemos un ciclo for que calcule la heurística de cada nodo en la lista de nodos.
            h = calcularHeuristica(node[:9])                        #Calculamos la heurística. Obtenemos el valor estimado desde la celda actual a la final.
            g = len(node[9:])                                                #El número de nodos que hemos visitado desde el nodo inicial al actual.
            f = g+h                                                          #Calculamos el coste real desde el estado inicial al estado obejtivo.
            fList.append(f)                                                  #Guardamos el valor de la heurística del nodo.
        nodoActual = listaNodos.pop(fList.index(min(fList)))                 #Elegimos como nodo actual al nodo que tenga el menor valor de la heurística de la lista de nodos a expandir.
        cero = nodoActual.index(0)                                           #Se obtiene la posición del 0 en la lista del nodo actual.
        if cero!=0 and cero!=1 and cero!=2:                                  #Si la posición del 0 no es en las tres casillas superiores, generamos la el movimiento hacia arriba del 0.
            superior = copy.deepcopy(nodoActual)                             #Copiamos el nodo actual entero para hacer el movimiento.
            superior[cero] = superior[cero-3]                                #Cambiamos la posición de los dos elementos, el cero y el otro número.
            superior[cero-3] = 0
            superior.append('Arriba') 
            estadoFinalEncontrado = NodoObjetivo(superior)                   #Revisamos si es un estado final.
        if cero!=0 and cero!=3 and cero!=6 and estadoFinalEncontrado==False: #Si la posición del 0 no es en las tres casillas izquierdas, generamos la el movimiento hacia la izquierda del 0.
            izquierdo = copy.deepcopy(nodoActual)
            izquierdo[cero] = izquierdo[cero-1]                              #Cambiamos la posición de los dos elementos, el cero y el otro número.
            izquierdo[cero-1] = 0
            izquierdo.append('Izquierda')
            estadoFinalEncontrado = NodoObjetivo(izquierdo)                  #Revisamos si es un estado final.
        if cero!=6 and cero!=7 and cero!=8 and estadoFinalEncontrado==False: #Si la posición del 0 no es en las tres casillas inferiores, generamos la el movimiento hacia abajo del 0.
            inferior = copy.deepcopy(nodoActual)
            inferior[cero] = inferior[cero+3]                                #Cambiamos la posición de los dos elementos, el cero y el otro número.
            inferior[cero+3] = 0
            inferior.append('Abajo')
            estadoFinalEncontrado = NodoObjetivo(inferior)                   #Revisamos si es un estado final.
        if cero!=2 and cero!=5 and cero!=8 and estadoFinalEncontrado==False: #Si la posición del 0 no es en las tres casillas derechas, generamos la el movimiento hacia la derecha del 0.
            derecho = copy.deepcopy(nodoActual)
            derecho[cero] = derecho[cero+1]                                  #Cambiamos la posición de los dos elementos, el cero y el otro número.
            derecho[cero+1] = 0
            derecho.append('Derecha')
            estadoFinalEncontrado = NodoObjetivo(derecho)                    #Revisamos si es un estado final.

    tFin = time.time()             #Obtención del tiempo de finalización del programa, en el que se encuentra la solución o se acaban los nodos.
    print('Tiempo:', tFin-tInicio) #Impresión del tiempo total del programa, Tiempo de Final - Tiempo de inicio.
    print('------')
