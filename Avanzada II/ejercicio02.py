import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa para calcular  la edad de una persona 

AñoActual= 2025
AñoNacimiento = int(input("Ingrese su año de nacimiento: "))

Edad= AñoActual-AñoNacimiento

print(f"Su anio de nacimiento es {AñoNacimiento} por lo tanto su edad es {Edad}")

if Edad >= 21:
    if Edad >= 18:
        print(f"Ya puedes votar")
    else:
        print(f"Eres mayor de edad")
else:
    print(f"Eres menor de edad")
