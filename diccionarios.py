# iniciando / creando un diccionario

#nombre, correo, telefono, run, direccion
carlos = {
    "nombre": "Carlos",
    "correo": "carlos@gmail.com",
    "telefono": "+569 123456877",
    "run": "1.111.111-1",
    "direccion": "direccion #1"
}

print(type(carlos))

# Acceder a un elemento por el nombre de la clave -> [“llave”] / get()

#print(carlos["telefono2"])
print(carlos.get("telefono2"))

# Agregar elementos.
carlos = {
    "nombre": "Carlos",
    "correo": "carlos@gmail.com",
    "telefono": "+569 123456877",
    "run": "1.111.111-1",
    "direccion": "direccion #1",
    "edad": 25,
    "preferencias": ["python", "javascript", "java"]
}

carlos["rol"] = "cliente"
carlos["nombre"] = "Carlos Soto"

print(carlos)
print("edad: ", carlos["edad"])
carlos["preferencias"].append("go")
carlos["preferencias"].remove("javascript")

print("Preferencias: ", carlos["preferencias"])


# lista de diccionarios

usuario1 = {"nombre":"Carlos"}
usuario2 = {"nombre":"Pedro"}

usuarios = [usuario1, usuario2]

# usuarios.append(usuario1)
# usuarios.append(usuario2)

print(usuarios[0])


# Comprobación de llaves -> ‘key’ in diccionario

usuario1 = {"nombre":"Carlos", "apellido": "Soto"}
usuario2 = {"nombre":"Pedro"}

print("apellido" in usuario2)

# Eliminar elementos -> pop(‘item’) / popitem() / del
llave = usuario1.pop("apellido")
print("Se ha eliminado", llave)
#del usuario1["apellido"]
print(usuario1)

# Limpiar un diccionario -> clear()
usuario1 = {"nombre":"Carlos", "apellido": "Soto"}
usuario1.clear()
print(usuario1)

# Copiar un diccionario -> copy()

usuario1 = {"nombre":"Carlos", "apellido": "Soto"}
usuario2 = usuario1.copy() # copia superficial

usuario2["nombre"] = "Pedro"
print("Usuario 1: ", usuario1)
print("Usuario 2: ", usuario2)

# Obtener las claves de un diccionario -> keys()

usuario1 = {"nombre":"Carlos", "apellido": "Soto"}

llaves = usuario1.keys()

usuario1["direccion"] = "Pasaje 1"

print(llaves)

# Obtener valores de un diccionario -> values()
usuario1 = {"nombre":"Carlos", "apellido": "Soto"}

valores = tuple(usuario1.values())
print(valores)