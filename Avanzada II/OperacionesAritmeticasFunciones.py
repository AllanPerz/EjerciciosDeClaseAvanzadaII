#Operaciones aritmeticas con Funciones

import os
os.system('cls' if os.name == 'nt' else 'clear')


def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def potencia(a,b):
    return a**b

print("Por favor ingrese dos numero para realizar las operaciones aritmeticas")
a = int(input("Por favor ingrese el primer numero: "))
b = int(input("Por favor ingrese el segundo numero: "))

print(f"La suma es: {suma(a,b)}")
print(f"La resta es: {resta(a,b)}")
print(f"La multiplicacion es: {multiplicacion(a,b)}")
print(f"La division es: {division(a,b)}")
print(f"La potencia es: {potencia(a,b)}")