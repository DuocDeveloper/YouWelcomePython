"""
Ejercicio 3. Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo) de los 60 primeros numeros natualres. Resolver con for y con while
"""

# While
contador = 0
while contador <= 60:
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1

# FOR
for contador in range(1, 61):
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
