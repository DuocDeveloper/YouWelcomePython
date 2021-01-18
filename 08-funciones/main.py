def HolaMundo(nombre):
    print(f"Mi nombre es {nombre}")


def tabla(numero):
    incrementador = 1
    while incrementador <= 10:
        resultado = numero * incrementador
        print(f"{numero} x {incrementador} = {resultado}")
        incrementador += 1


# Parametros opcionales
def Presentante(nombre, rut=None):
    if nombre != None and rut != None:
        print(f"Nombre: {nombre}")
        print(f"Rut: {rut}")

# Funciones con return
def Multiplica(numero1, numero2):
    return numero1 * numero2

# Funciones anidadas
def getNombre(nombre):
    return nombre


def getApellido(apellido):
    return apellido


def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + " " + getApellido(apellido)
    return texto


nombre = input("Cual es tu nombres?: ")
HolaMundo(nombre)

numero = int(input("Que tabla de multiplicar desea?: "))
tabla(numero)

Presentante("Joan", "15932623-3")
Presentante("Joan")

resultado = Multiplica(5, 5)
print(f"5 x 5: {resultado}")


print(devuelveTodo("Joan", "Toro"))

# Funciones lambda
def dime_el_year(year): return f"El año es {year}"


print(dime_el_year(2020))
