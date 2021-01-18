"""
Variables local: Se definen dentro de las funciones y solo se accede dentro de ella.

Variable globales: Se definen fuera de las funcines y se accede dentro y fuera de las funciones
"""

# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)


def holaMundo():
    frase = "Hola mundo!!"
    print("Dentro de la funcion.")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "www.google.cl"
    print("Dentro: " + website)

    return "Dato devuelto " + str(year)


print(holaMundo())
print("Fuera: " + website)
