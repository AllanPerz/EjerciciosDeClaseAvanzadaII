#invocaremos la clase animal

import os
os.system('cls' if os.name == 'nt' else 'clear')

from Clase01 import Perro

miPerro=Perro("Carbon")

miPerro.ladrar()
miPerro.correr()