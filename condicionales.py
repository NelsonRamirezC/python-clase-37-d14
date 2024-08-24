elementos = [1,2,3]

opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    print("Ha elegido la opción N° 1")
elif opcion == 2:
    print("Ha elegido la opción N° 2")
elif opcion == 3:
    print("Ha elegido la opción N° 3")
else:
    print("Opción no válida")
    
    
if not False:
    print("Es falso")
    

# REQUISITOS PARA APROBAR EL CURSO
asistencia_req = 75
promedio_req = 60
trabajos_req = 8

asistencia = 80
promedio = 65
trabajos = 7

a_asistencia = asistencia >= asistencia_req
a_promedio = promedio >= promedio_req
a_trabajos = trabajos >= trabajos_req

print(a_asistencia, a_promedio, a_trabajos)
if a_asistencia and a_promedio and a_trabajos:
    print("cumple")
else:
    print("No cumple")
    

#short hand 
valor = -1
print("Es verdadero") if valor >= 0 else print("Es falso")
