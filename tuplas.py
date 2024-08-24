
# Acceder a elementos -> tupla[0]
lenguajes = ("javascript", "Java", "python", "go")

#print(type(lenguajes))

#print(lenguajes.count("java"))

#Acceder a elementos -> tupla[0]
# Cortar tuplas -> tupla[0:3]
print(lenguajes[1:3])

# Convertir tuplas a listas.
lenguajes = ("javascript", "Java", "python", "go")

# Convertir tuplas a listas.
lenguajes = list(lenguajes)
lenguajes[1] = "JAVA"
lenguajes = tuple(lenguajes)
print(type(lenguajes))
print(lenguajes)

# Comprobar si un elemento se encuentra en la tupla
lenguajes = ("javascript", "Java", "python", "go")

print("C#" in lenguajes)

# Unir tuplas.
lenguajes1 = tuple("javascript", "Java", "python", "go")
lenguajes2 = tuple("C#")

print(type(lenguajes1))
print(type(lenguajes2))

lenguajes = lenguajes1 + lenguajes2

print(lenguajes)


# eliminar tuplas

lenguajes = ("javascript", "Java", "python", "go")
print(lenguajes)
del lenguajes
print(lenguajes)