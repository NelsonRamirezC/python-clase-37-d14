
names =[
    'Harry Houdini', 
    'Newton', 
    'David Blaine', 
    'Hawking', 
    'Messi',
    'Teller', 
    'Einstein', 
    'Pele', 
    'Juanes'
] #descubrí que es de Juan Esteban, y no 'Juánez'

magicians = ['Harry Houdini', 'David Blaine', 'Teller'] #especifico los nombres de magos

scientists=['Einstein', 'Hawking', 'Newton'] #especifico los nombres de científicos

not_magicians_nor_scientists = [name for name in names if name not in magicians and name not in scientists]

print(not_magicians_nor_scientists)
#creo una compresión de lista que recorra la lista names, y que lo haga 'nombre por nombre' (
#name for name) y que los saque si no están en magicians o scientists
#esta parte fue la más difícil :(
#básicamente crea una lista de ni magos ni científicos si el nombre no está especificado en ningún grupo arriba

def hacer_grandioso(magicians):
    return(f'El gran {x}' for x in magicians)
    #modifico el texto pa los magos

def imprimir_nombres(names):
    for name in names:  #acá 'name' toma un valor efímero, es sólo para recorrer la lista names, y así q imprima todo; pero perfectamente podría ser x, y, z o cualquier cosa
        print(name)

print('Esta es la lista con todas las personas: ')
print() #para dejar un espacio
imprimir_nombres(names) #acá invoqué la función (fx desde ahora) de imprimir todos los nombres en la lista names
print() #para dejar un espacio

grand_magicians = hacer_grandioso(magicians)
print('--------------------------') #líneas para dar estética y separar
print() #para dejar un espacio
print('Estos son los mejores magos de todos los tiempos:')
imprimir_nombres(grand_magicians) #acá invoco la fx para imrpimir todo en la lista grand_magicians
print()

print('-----------------------')
print()
print('Estos fueron grandes científicos en su momento:')
imprimir_nombres(scientists) #acá invoco la fx para nombrar a todos los scientists
print()

print('--------------------------------')
print()
print('Estos son otras personas famosas:')
imprimir_nombres(not_magicians_nor_scientists) #acá invoqué la fx para nombrar al 3er grupo


'''
DESCRIPCIÓN
Dada la siguiente lista de nombres:
• Harry Houdini
• Newton
• David Blaine
• Hawking
• Messi
• Teller
• Einstein
• Pele
• Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
frase ‘El gran‘ antes del nombre de cada mago.
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.
'''