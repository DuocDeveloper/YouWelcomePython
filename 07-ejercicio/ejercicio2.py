"""

Ejercicio 2. Escribir un script que nos muestre por pantalla todos los numeros pares del 1 al 120.

"""

contador = 1

for contador in range(1, 121):
    modulo = contador % 2
    if modulo == 0:
        print(contador)
