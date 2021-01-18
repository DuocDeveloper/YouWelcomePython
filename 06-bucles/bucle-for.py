"""
# FOR

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0

for contador in range(0, 5):
    print(f"Voy por el {contador}")

print("\nTablas de multiplicas")

tabla = int(input("Ingrese la tabla de multiplicar: "))
incrementador = 1

for incrementador in range(1, 11):
    resultado = tabla * incrementador
    if resultado < 45:
        print(f"{tabla} x {incrementador} = {resultado}")
    else:
        print("Se excede del numero 45")
        break
