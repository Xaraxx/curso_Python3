# Un diccionario es un mapa de llaves a valores. Los valores puede ser de cualquier tipo.

# se crea con {} o con la palabra reservada dict()

# Iterar los diccionarios 

#for key in diccionario:

import os 
os.system('cls')

calificaciones = {}

calificaciones['algoritmos'] = 9
calificaciones['matematica'] = 10
calificaciones['web'] = 8
calificaciones['bases_de_datos'] = 10

# iteración a lo largo de las llaves
for key in calificaciones:
   print(key)

# iteración a lo largo de los valores

for value in calificaciones.values():
   print(value)

# iteración entre llaves y valores

for key, value in calificaciones.items():
   print('llave: {}, valor: {}'.format(key,value))

suma_de_calificaciones = 0

for calificacion in calificaciones.values():
   suma_de_calificaciones += calificacion

promedio = suma_de_calificaciones/len(calificaciones.values())

print('Tu promedio es {}'.format(promedio))
