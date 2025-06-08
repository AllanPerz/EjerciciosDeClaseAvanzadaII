#Funciones

import os
os.system('cls' if os.name == 'nt' else 'clear')

#Definimos la funcion
def saludo(nombre):
    print(f"Hola {nombre}")

def _PI():
    return 3.1416

def suma(a,b):
    return a+b

#Invocamos la funcion
saludo("Allan Pérez")

#Calcular el diametro de un circulo
r=10
diametro=2*_PI()*r
print(f"Diametro: {diametro}")

#Funcion suma
print(f"La suma de {suma(1,1)}")