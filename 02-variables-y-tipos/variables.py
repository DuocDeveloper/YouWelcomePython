'''
Una variables es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto. 
'''

# Crear variables y asignación de valor.

texto = "Máster en Python"
texto2 = "con Joan Toro"
numero = 34
decimal = 6.4

print(texto)
print(texto2)
print(numero)
print(decimal)

# Sustituir el valor de algunas variables / reasignado valores

numero = 77
decimal = 8.9

print(numero)
print(decimal)

# Contactenación 

nombre = "Joan"
apellido = "Toro"
web = "gmail.com"

print(nombre + " " + apellido + " || " + web)
print(f"{nombre} {apellido} || {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))
print(nombre, apellido, web)
