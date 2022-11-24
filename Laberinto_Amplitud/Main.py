from Nodo import *

if __name__ == '__main__':                                         #Función principal.
    #Leemos el laberinto del archivo de texto para cargarlo a memoria.
    print('\nL A B E R I N T O   Amplitud \n')
    laberinto.dibujar_muros()   
    print(acciones(laberinto.inicio, estados_explorados))