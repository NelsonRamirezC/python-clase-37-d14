#1.- Crear listas -> lista = list() / lista = []

animales = ["conejo", "perro", "gato"]

print(type(animales))

#2  Acceder a elementos de una lista
print(animales[-2]) # perro
print(animales[-3]) # IndexError: list index out of range

# Separar elementos  ->  lista[2:2]

personas = ["Carlos", "Juan", "Pedro", "Marta"]

print(personas[0:2]) # ['Carlos', 'Juan'] -> [inicio, fin]
print(personas[0:4:3]) # ['Carlos', 'Marta']


# Agregar elementos -> append()
personas = ["Carlos", "Juan", "Pedro", "Marta"]

personas.append("Juan")

print(personas)

# Insertar elementos -> insert()
personas = ["Carlos", "Juan", "Pedro", "Marta"]
personas.insert(1, "Matías")
print(personas)

# Remover elementos -> remove()
personas = ["Carlos", "Juan", "Pedro", "Marta", "Pedro"]
personas.remove("Pedro")
print(personas)

# Vaciar una lista -> clear()
personas = ["Carlos", "Juan", "Pedro", "Marta", "Pedro"]
# personas.clear()
print(personas)
    
# Unir listas -> extend()
productos1 = ["producto 1", "producto 2"]
productos2 = ["producto 3", "producto 4"]
productos3 = ["producto 5", "producto 6"]

# productos1.extend(productos2)
# productos1.extend(productos3)
productos = productos1 + productos2 + productos3
print(productos)

# Contar elementos -> count()
numeros = [1, 3, 5, 3, 5, 7, 8, 9, 1, 2, 3]

print(numeros.count(5)) # retorna la cantidad de ocurrencias -> 2
print(len(numeros)) # retorna la cantidad de elementos de la lista

print(numeros[-1])

# Obtener el índice de un element -> index
personas = ["Carlos", "Juan", "Pedro", "Marta", "Pedro", "Carla"]
indice_pedro = personas.index("Pedro")
# print(personas[indice_pedro])
indice_pedro = personas.index("Pedro", 5)
#print(indice_pedro)

meses = ["enero", "marzo"]
indice_enero = meses.index("marzo")
print(indice_enero)
meses.insert(indice_enero, "febrero")
print(meses)

help(list.index) # muestra la documentación de la función

help(print) # importantw

print(1,2,3,"carlos", True, sep="\n")

# Invertir lista -> reverse()
numeros = [2, 3, 1, 4, 5, 6, 8, 9]
numeros.reverse()
print(numeros)

# Ordenar lista -> sort()
numeros = [2, 3, 1, 4, 5, 8, 9]
numeros.sort() # por defecto el orden es ascendente
numeros.sort(reverse=True) # ordena de forma descendente
print(numeros)

