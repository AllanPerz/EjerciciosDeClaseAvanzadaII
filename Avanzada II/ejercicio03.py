#Ejercicio usando el ciclo for de una tabla de multiplicar que el usuario elija la tabla ah mostrar

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Por favor ingrese el numero de la tabla que desee")
num = int (input("La tabla del: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")