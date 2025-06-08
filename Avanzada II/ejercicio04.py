#Tablas de multiplicar con el ciclo while

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Por favor ingrese el numero de la tabla que desee")
num = int (input("La tabla del: "))

i = 0

while i < 10:
    i += 1
    print(f"{num} x {i} = {num*i}")