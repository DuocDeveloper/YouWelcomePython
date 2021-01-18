"""
SET es un tipo de dato, para tener una colecciones de valores, pero no tiene ni indice, ni orden.
"""

personas = {"Joan", "Jami", "Jesus", "Joaquín"}

personas.add("Manuel")

print(type(personas))
print(personas)

personas.remove("Manuel")

print(personas)
