nada = None
cadena = "Hola soy un texto"
entero = 99
flotante = 6.4
booleano = True
lista = [1,2,3,4]
listaCadena = [1, "Dos", "Tres", 4]
tuplaNoCambia = ("Joan", "Toro", "Ortiz")
diccionario = {
    "nombre": "Joan",
    "apellido": "Toro",
    "correo": "jtoro@gmail.com"
}
rango = range(9)
dato_byte = b"Probando"

# Imprimir variable
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(listaCadena)
print(tuplaNoCambia)
print(diccionario)
print(rango)
print(dato_byte)

# Mostrar tipo de datos
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(listaCadena))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))


# Casting o Parse de tipos de datos, tipo de datos + ( y variable )
texto = "Hola soy un texto"
numerito = 520
print(texto + " " + str(numerito))