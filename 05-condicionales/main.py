"""
# Condicional IF 

SI se_cumple_esta_condicion: 
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

# Sintaxis

if condicion:
    instrucciones 
else:
    otras instrucciones
"""

# Ejemplo 1
print("################ Ejemplo 1 ################")
color = input("Adivina el color : ")

if color.upper() == "ROJO":
    print("El color ingresado es rojo")
else:
    print("El color ingresado no es rojo")

"""
# Operadores de comparación

== Igual
!= diferente
< menor que 
> mayor que 
<= menor o igual que
>= mayor o igual que

"""

# Ejemplo 2
print("################ Ejemplo 2 ################")

year = int(input("¿En que año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un año anterior a 2021")


# Ejemplo 3
print("################ Ejemplo 3 ################")

nombre = "Joan Toro"
ciudad = "Santiago"
continente = "Sudamerica"
edad = 34
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} ES MAYOR DE EDAD")
    if continente != "Sudamerica":
        print(f"{nombre} NO ES SUDAMERICANO")
    else:
        print(f"{nombre} ES SUDAMERICANO, de la ciuidad {ciudad}")
else:
    print(f"{nombre} NO ES MAYOR DE EDAD")
