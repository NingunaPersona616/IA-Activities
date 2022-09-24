from Aspiradora import Aspiradora
from Enviroment import *
import os

trash_A = int(input('Ingrese can. de basura en A: '))
trash_b = int(input('Ingrese can. de basura en B: '))

env_A = Enviroment(trash_A)
env_B = Enviroment(trash_b)
os.system ("cls")

location = input('Ingrese A o B para elegir el area donde iniciara la aspiradora: ').upper()
os.system ("cls")

aspiradora1 = Aspiradora(env_A, env_B, location)

aspiradora1.start()


print("Cantidad total de movimientos: ", aspiradora1.actions)