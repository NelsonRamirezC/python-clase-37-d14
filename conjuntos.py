conjunto = set({1,2,3,4,5})

print(type(conjunto))


# Longitud de un set -> len()
conjunto = set({1,2,3,4,5})

print(len(conjunto))

# Comprobación de un elemento -> ‘elemento’ in st

print(6 in conjunto)


# Agregar elementos -> add()
conjunto = set({1,2,3,4,5})

conjunto.add(int(input("Agrega un nuevo valor: ")))
print(conjunto)

# Eliminar elementos -> remove()
conjunto = set({1,2,3,4,5})
conjunto.remove(10)
print(conjunto)

# Agregar varios elementos -> update()
conjunto = set({1,2,3,4,5})
conjunto.update([2, 5, 8, 9])
print(conjunto)

# Remover de forma aleatoria -> pop()
conjunto = set({1,2,3,4,5})
conjunto.pop()

print(conjunto)

# Limpiar / vaciar -> clear()
conjunto = set({1,2,3,4,5})
conjunto.clear()
print(conjunto)

# Unir conjuntos -> union()
conjunto1 = set({1, 2, 3, 4, 5})
conjunto2 = set({1, 2, 8, 9, 10})
conjuntos = conjunto1.union(conjunto2)

print(conjuntos)

# Intersección de elementos entre tuplas -> intersection()
conjunto1 = set({1, 5, 7, 2})
conjunto2 = set({2, 5, 9})

interseccion = conjunto1.intersection(conjunto2)

print(interseccion)

# diferencias
conjunto1 = set({1, 5, 7, 2})
conjunto2 = set({2, 5, 9})

diferentes = conjunto2.difference(conjunto1)
print(diferentes)
