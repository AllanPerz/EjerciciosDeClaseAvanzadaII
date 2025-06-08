#Crearemos  la clase animal

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} Esta comiendo")

    def correr(self):
        print(f"{self.nombre} viene corriendo! ")

class Perro(Animal):

    def ladrar(self):
        print(F"Grrrrrrrrr grrrrr guaaau guaaaaa grrrrrrrr")

class Gato(Animal):
    
    def maullar(self):
        print("Miauuuuu Miauuuuuuuuuuuuuu")

#Definir objeto para usar la clase

# miPerro=Perro("Canducho")

# miPerro.ladrar()
# miPerro.comer()
# miPerro.correr()

# miGato=Gato("Misifus")

# miGato.comer()
# miGato.maullar()
# miGato.correr()


#perro=Animal("Firulais")

#perro.correr()
#perro.ladrar()
#perro.comer()
    

