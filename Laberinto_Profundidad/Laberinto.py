
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
            print()

    def dibujar_solucion(self, ruta, estadosExplorados):                                               #Función para dibujar los muros.
        for i, fila in enumerate(self.contenido):                           #Recorremos todo el contenido de la matriz en memoria.
            for j, columna in enumerate(fila):
                if columna == ' ':                                          #Si la ubicación no contiene nada, entonces.
                    if (i, j) in ruta:                       #Si es el camino más corto al objetivo en ese momento se marca con *.
                        print('*', end='')
                    elif (i, j) in estadosExplorados:                               #Si esta ubicación ya se encuentra en los nodos expandidos, se marca con -.
                        print('-', end='')
                    else:
                        print(' ', end='')

                elif columna == '#':
                    print('█', end='')

                else:
                    print(columna, end='')  
            print()
