"""
Diccionarios: Es un tipo de datos que almacena un conjunto de datos, en formato clave > valor. 
Es parecido a un array asociativo o un objeto json. 
"""

persona = {
    "nombre": "Joan",
    "apellidos": "Toro Ortiz",
    "fecha_nacimiento": "09/05/1986"    
}

print(persona)
print(type(persona))
print(persona['nombre'])

# Lista con diccionarios

contactos = [
    {"nombre": "Joan", "apellidos": "Toro Ortiz", "fecha_nacimiento":"09/05/1986"},
    {"nombre": "Jami", "apellidos": "Arancibia Peña", "fecha_nacimiento":"10/09/1986"},
    {"nombre": "Joaquín", "apellidos": "Toro Arancibia", "fecha_nacimiento":"21/07/2017"},
]

print(contactos)
print(contactos[0]["nombre"])

contactos[2]["fecha_nacimiento"] = "21/07/2018"

print("\nListado de contactos:")
for contacto in contactos:
    print(f"Nombre contacto: {contacto['nombre']} {contacto['apellidos']}")
    print(f"Fecha Nacimiento: {contacto['fecha_nacimiento']}")
    print("****************************************************")