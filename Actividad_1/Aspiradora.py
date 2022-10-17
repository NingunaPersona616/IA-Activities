INACTIVE = 0
CLEANING = 1
MOV_A = 2
MOV_B = 3

class Aspiradora:
    def __init__(self, env_A, env_B, location): #Inicializacion de variables
        self.env_A = env_A
        self.env_B = env_B
        self.status = INACTIVE  #status de la accion
        self.statusPrev = INACTIVE #status de la accion anterior
        self.location = location  #Localizacion de la aspiradora
        self.actions = 0
        self.energy = 100   #Cantidad de energia del robot

    def start(self):    #Inicio del funcionamiento de la aspiradora
        print("Hay: ", self.env_A.trash, "basuras en el Entorno A")
        print("Hay: ", self.env_B.trash, "basuras en el Entorno B")
        while(self.env_A.isClean() == False or self.env_B.isClean() == False):  #Mientras no esten limpios los dos entornos seguir ejecutando la funcion clean()
            self.clean()

        print("Esta todo limpio apagando ...")  #Una vez que termine de limpiar se apaga
        self.statusPrev = self.status
        self.status = INACTIVE

    def clean(self):    #Funcion que le indica a la aspiradora como limpiar en cada momento
        self.statusPrev = INACTIVE
        self.status = INACTIVE
        if(self.location == 'A'):   #Si la aspiradora se encuentra en A hay 2 opciones
            if(self.env_A.isClean()):   #La primera: el entorno A esta limpio y se mueve a B
                print("Limpio A")
                self.statusPrev = self.status
                self.status = MOV_B
                print("Moviendo a B")
                self.location = 'B'
                self.actions += 1
                self.energy -= 5    #Disminuye la energia y aumenta la cant de movs
            else:                       #La segunda: El entorno A esta sucio, se limpia y se mueve a B
                self.statusPrev = self.status
                self.status = CLEANING
                for i in range(self.env_A.trash):
                    print('Aspirando A ...')
                    self.env_A.trash -= 1
                
                print("Limpio A")
                self.statusPrev = self.status
                self.status = MOV_B
                print("Moviendo a B")
                self.location = 'B'
                self.actions += 2
                self.energy -= 10    #Disminuye la energia y aumenta la cant de movs
        
        elif(self.location == "B"): #Si la aspiradora se encuentra en B hay 2 opciones
            if(self.env_B.isClean()):   #La primera: el entorno B esta limpio y se mueve a el entorno A
                print("Limpio B")   
                self.statusPrev = self.status
                self.status = MOV_A
                print("Moviendo a A")
                self.location = 'A'
                self.actions += 1
                self.energy -= 5    #Disminuye la energia y aumenta la cant de movs

            else:                       #La segunda: El entorno B esta sucio, se limpia y se mueve al entorno A
                self.status = CLEANING
                for i in range(self.env_B.trash):
                    print('Aspirando B ...')
                    self.env_B.trash-=1

                print("Limpio B")
                self.statusPrev = self.status
                self.status = MOV_A
                print("Moviendo a A")
                self.location = 'A'
                self.actions += 2
                self.energy -= 10    #Disminuye la energia y aumenta la cant de movs
