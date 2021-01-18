cantantes = ['2Pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1,3,4,2,8,6,5,7]

# Ordenar
print(numeros)
numeros.sort()
print(numeros)


# Añadir elementos
cantantes.append("Natos y Waor")
print(cantantes)

cantantes.insert(0, "Snoop Dog") # indices, más elemento.
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
print(cantantes)

cantantes.remove('Drake')
print(cantantes)

# Dar la vuielta
print(numeros)

numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Snoop Dog' in cantantes)

# Contar elementos
print(len(cantantes))

# Cuentas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Snoop Dog"))

# Unir listas 
cantantes.extend(numeros)
print(cantantes)