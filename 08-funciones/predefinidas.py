nombre = "Joan Toro"

# Funciones generales
print(nombre)
print(type(nombre))


# Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variables es un string")
else:
    print("Esa variables no es un string")

if not isinstance(nombre, float):
    print("Esa variables no es un numero con decimales")

# Limpiar espacios
frase = "       mi contenido "
print(frase)
print(frase.strip())


# Elimpiar variables
year = 2020
print(year)
del year  # Elimino variable de cualquier tipo de datos
# print(year)

# Comprobar variables vacias
texto = " ff   "
if len(texto) <= 0:
    print("Variable esta vacias")
else:
    print("Variable tiene contenido ", len(texto))

# Encontrar caracteres
frase = "Holita mundito!!!"
print(frase.find("mundito"))

# Reemplazar palabras en un string
nueva_frase = frase.replace("Holita", "Chaito")
print(nueva_frase)
print(nueva_frase.upper())
print(nueva_frase.lower())
