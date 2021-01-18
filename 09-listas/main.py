"""
LISTAS (Arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.
Para acceder a estos valores podemos usar un indice numero.
"""

pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Thor", "Superman"]
cantantes = list(("2pac", "Drake", "SnoopDog"))
años = list(range(2020,2050))
variada = ["Joan", 1986, 96.5, True, "Toro"]

print(pelicula)
print(peliculas)
print(cantantes)
print(años)
print(variada)

# Indices
print(peliculas[1]) #Posivo, de izquierda a derecha
print(peliculas[-2]) #Negativo, de derecha a izquierda
print(cantantes[0:2]) #Rango de elementos por indice X a N-1, aplica negativos.
print(peliculas[1:]) #Rango de elemento por indice a partir del N al final.

peliculas[1] = "Los Vengadores"
print(peliculas[1])

# Añadir elementos
cantantes.append("Kase O") #append agrega al final de la lista 

print(cantantes)

nuevo_cantante = "Parar"
while nuevo_cantante != "Parar":
    nuevo_cantante = input("Introduce la nueva pelicula: ")
    if nuevo_cantante != "Parar":
        cantantes.append(nuevo_cantante)

# Recorrer lista
print(">> Listado cantantes")
for item in cantantes:
    print(f"{cantantes.index(item)}.- {item}")


# Listas multidimensionales
print(">> Lista de contactos")
contactos = [
    [ 'Joan', 'joan@gmail.com' ], 
    [ 'Jami', 'jami@gmail.com' ],
    [ 'Joaquín', 'joaquin@gmail.com']
]    

print(contactos[2][1])
print(contactos)

for contacto in contactos:
    for item in contacto:
        if contacto.index(item) == 0:
            print("Nombre: " + item)
        else:
            print("Email: " + item)