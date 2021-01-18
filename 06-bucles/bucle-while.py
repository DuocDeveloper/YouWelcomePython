"""

# Bucle While

while condición:
    bloque de instrucciones
    actualización de contador

"""

print("\nTablas de multiplicas")

tabla = int(input("Ingrese la tabla de multiplicar: "))
incrementador = 1

while incrementador <= 10:
    resultado = tabla * incrementador
    print(f"{tabla} x {incrementador} = {resultado}")
    incrementador += 1
