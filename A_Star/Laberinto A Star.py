#Algoritmo A* para un laberinto
import time             #biblioteca para importar las funciones de Tiempo.

def a_star(estados):                            #Implementación del Algoritmo A*.
    distancias = []                             #Se crea una lista que almacenará la distancia de todos los estados (nodos).
    x, y = laberinto.meta                       #Se toman las coordenadas del punto objetivo del laberinto.
    for estado in estados:                      #Recorremos todos los nodos disponibles que aún no han sido visitados.
        i, j = estado                           #Obtenemos las coordenadas del estado actual.
        manhattan = abs(j - y) + abs(i - x)     #Calculamos la distancia Manhattan entre el estado actual y el estado objetivo. 
        distancias.append((manhattan, estado))  #Agregamos la distancia a nuestra lista.
    distancias.sort()                           #Ordenamos nuestra lista para obtener el menor valor al inicio.
    if distancias:                              #Si nuestra lista NO está vacía (quiere decir que si no nos quedamos sin estados que explorar).
        return distancias[0][1]                 #Regresamos el estado con la menor distancia al estado objetivo.


def filtrar_rutas(ruta_duplicada):                          #Función para filtrar las rutas.
    for num, coordinate in enumerate(ruta_duplicada):       #Recorremos la lista que recibimos.
        if num == len(ruta_duplicada) - 1:                  #Si encontramos que la ruta evaluada es la más corta, la regresamos.  
            return ruta_duplicada
        #Intentamos eliminar las rutas que son más grandes y volvemos a llamar a la función para encontrar la ruta más corta.
        try:                                        
            x1 = ruta_duplicada[num][0]
            x2 = ruta_duplicada[num + 1][0]
            y1 = ruta_duplicada[num][1]
            y2 = ruta_duplicada[num + 1][1]
            if ((x1 == x2) and (abs(y2 - y1) == 1)) or ((y1 == y2) and (abs(x2- x1) == 1)):
                pass
            else:
                del ruta_duplicada[num + 1]
                filtrar_rutas(ruta_duplicada)
        except IndexError:
            pass


def acciones(estado):
    fila, columna = estado
    #Movimientos disponibles en el laberinto. Derecha, Izquierda, Arriba y Abajo.
    movimientos = [(fila + 1, columna), (fila - 1, columna), (fila, columna + 1), (fila, columna - 1)] 
    #Se eligen los movimientos válidos para el estado actual y se almacenan en una lista que se regresa posteriormente.
    #Se agrega el movimiento si no ha sido explorado anteriormente, si no es un muro y si está dentro del rango del laberinto. 
    moves = [move for move in movimientos if move not in Nodo.estados_explorados
             and move not in laberinto.muro and move[0] in range(laberinto.altura) and
             move[1] in range(laberinto.ancho)]
    return moves

class Nodo:                                     #Clase nodo para moverse por el laberinto.
    estados_explorados = []                     #Lista en la que vamos a guardar los nodos que ya visitamos.
    frontera = []                               #Lista en la que vamos a guardar
    ruta = []                                   #Lista en la que vamos a guardar
    ruta_mas_corta = []                         #Lista en la que vamos a guardar

    def __init__(self, estado, nodoPadre, accion):  #Constructor de la clase.
        self.estado = estado
        self.nodoPadre = nodoPadre
        self.accion = accion
        self.frontera.append(self.estado)

        while True:                             #Hacemos un ciclo while que durará hasta encontrar la solución o encontrar que no tiene solución.
            if not self.frontera:               #Si la lista de frontera está vacía, no hay más nodos que expandir, por lo que no hay solución.
                print("\nNo hay solución.")
                break
            elif self.estado == laberinto.meta: #Si el estado actual es igual a la meta, entonces guardamos la ruta del estado.
                self.ruta.append(self.estado)
                break
            #Con ayuda del algoritmo A* evaluamos la distancia de cada uno de los estados respecto al estado final o meta.
            #A partir de esto, obtenemos el estado que tiene la ruta más corta y generamos a los nodos hijos o los movimientos que se pueden hacer.
            self.accion = acciones(a_star(self.frontera))
            #Agregamos a la lista de estados explorados el estado actual para no volver a expandirlo y evitar caer en la recursividad.
            self.estados_explorados.append(self.estado)

            #Si la lista de acciones está vacía, eliminamos el estado de la frontera debido a que es un nodo nulo.
            if not self.accion:
                self.frontera.remove(self.estado)
            #Si tenemos acciones, entonces agregamos a cada uno de estos nuevos nodos a la lista de nodos frontera para expandirlos en un futuro.
            else:
                for i in self.accion:
                    self.frontera.append(i)
                self.nodoPadre = self.estado      #Asignamos el nodo actual al nodo padre.
                self.ruta.append(self.estado)     #Asignamos el la ruta del nodo actual a la variable para guardarla.
                self.frontera.remove(self.estado) #Removemos el nodo actual de la frontera.

            self.estado = a_star(self.frontera)   #Evaluamos con A* los nodos que tenemos en la lista de frontera.
        self.ruta.reverse()                       #Invertimos la lista.
        ruta_1 = []                               #Creamos una lista que nos ayudará a guardar cada una de las rutas que tenemos para comprobar si son duplicadas.
        for i in self.ruta: 
            ruta_1.append(i)

        for i in filtrar_rutas(ruta_1):          #Evaluamos a todas las rutas que copiamos para encontrar las repetidas y regresar las rutas más cortas hacia el objetivo.
            self.ruta_mas_corta.append(i)
        self.ruta_mas_corta.reverse()            #Invertimos la ruta más corta.
        self.ruta.reverse()                      #Invertimos nuevamente la lista de rutas.


class Laberinto:

    def __init__(self, archivo):                    #Constructor de la clase, recibe un archivo para extraer el laberinto.
        self.archivo = archivo                      #Variable con la que leeremos el archivo.
        self.inicio = None                          #Atributo donde se guardará la posición de inicio.
        self.meta = None                            #Atributo donde se guardará la posición de fin.
        self.muro = []                              #Lista donde se guardará la posición de los muros.

        with open(self.archivo) as archivo:          #Leemos el contenido del archvivo y lo cargamos a memoria.
            self.contenido = archivo.read()

        self.contenido = self.contenido.splitlines()                        #Separamos los renglones del contenido que hemos leído del archivo.
        self.altura = len(self.contenido)                                   #Obtenemos la longitud del contenido para saber la altura.
        self.ancho = max(len(contenido) for contenido in self.contenido)    #Obtenemos la anchura del contenido para saber la extensión del laberinto.

    def dibujar_muros(self):                                                #Función para dibujar los muros.
        for i, fila in enumerate(self.contenido):                           #Recorremos todo el contenido de la matriz en memoria.
            for j, columna in enumerate(fila):
                if columna == ' ':                                          #Si la ubicación no contiene nada, entonces.
                    if (i, j) in Nodo.ruta_mas_corta:                       #Si es el camino más corto al objetivo en ese momento se marca con *.
                        print('*', end='')
                    elif (i, j) in Nodo.ruta:                               #Si esta ubicación ya se encuentra en los nodos expandidos, se marca con -.
                        print('-', end='')
                    else:
                        print(' ', end='')                                  #Si no se deja vacío.
                elif columna == 'A':                                        #Si el contenido es la letra A (el inicio), la mostramos en pantalla.
                    print('A', end='')
                    self.inicio = (i, j)                                    #Establecemos la posición de A (el inicio) en el atributo designado.
                elif columna == 'B':                                        #Si el contenido es la letra B (el final), la mostramos en pantalla.
                    print('B', end='')                              
                    self.meta = (i, j)                                      #Establecemos la posición de B (el final) en el atributo designado.
                else:
                    print('█', end='')                                      #Si es el signo de numeral o cualquier otro, imprimimos el muro.
                    self.muro.append((i, j))                                #Agregamos la posición del muro a nuestra lista.
            print()                                                         #Para evitar que el laberinto se vea mal.

if __name__ == '__main__':                                         #Función principal.
    laberinto = Laberinto('laberinto.txt')                         #Leemos el laberinto del archivo de texto para cargarlo a memoria.
    print('\nL A B E R I N T O   A * \n')
    laberinto.dibujar_muros()                                      #Dibujamos el laberinto al usuario para que pueda verlo.
    print('\n\n^ Este es el laberinto inicial. ^\n\n')
    time_duration = 3.0
    time.sleep(time_duration)                                          #Pausar un momento la ejecución del programa.
    node = Nodo(estado=laberinto.inicio, nodoPadre=None, accion=None)  #Iniciamos el proceso de crear la solución.
    print('\nSolución: \n')                                            #Imprimimos la solución o el fin del algoritmo si no hay más nodos a visitar.
    laberinto.dibujar_muros()                                          #Dibujamos el estado final alcanzado.
    input()                                                            #Pausamos el programa para que no se cierre.