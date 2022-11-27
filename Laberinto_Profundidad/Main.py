from DFS import *


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