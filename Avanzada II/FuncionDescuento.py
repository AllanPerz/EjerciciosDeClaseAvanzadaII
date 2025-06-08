#Elaborar un programa que muestre el total de una compra de un solo producto calculado el ISV y 
#dar un descuento solo cuando el importe de la cuenta sea mayor a 10k el descuento sera del 25%

#Usando Funciones

def Descuento():
    return 

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Agrocomercial Pérez")

PrecioProducto = 500
CantidadProducto= float(input("Cantidad: "))
SubTotal = CantidadProducto * PrecioProducto
ISV = SubTotal * 0.15
Total = SubTotal + ISV

if Total >= 10000:
    Descuento = Total * 0.25
    Total2= Total - Descuento
    ISV2 = Total2 * 0.15
    print(f"ISV: {ISV2}")
    print(f"Su descuento fue de: {Descuento}")
    print(f"Su total a pagar es: {Total2}")

else:
    print(f"ISV: {ISV}")
    print(f"Su total a pagar es {Total}")