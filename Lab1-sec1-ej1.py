# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y
# se debe añadir uno por uno los elementos de ambas matrices. Luego se deben sumar
# estas matrices en una función, y en otra función restarlas. Solo utilizando las funciones
# de la biblioteca numpy.

import numpy as np
filas = int(input ("Introduzca el numero de filas de sus matrices: "))
columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))

matriz1 = []
matriz2 = []
for i in range (filas):
	matriz1.append( [0] * columnas)
	matriz2.append( [0] * columnas)

print('Ingrese los elementos de su primera matriz')

for i in range(filas):
	for j in range(columnas):
		matriz1[i][j] = float(input('Elemento (%d, %d): ' % (i,j)))

print('Ingrese los elementos de su segunda matriz')

for i in range(filas):
	for j in range(columnas):
		matriz2[i][j] = float(input('Elemento (%d, %d): ' % (i,j)))
		
# Suma
suma = np.array(matriz1) + np.array(matriz2)
print('La matriz suma es')
print(suma)

# Resta 
resta = np.array(matriz1) - np.array(matriz2)
print('La matriz resta es')
print(resta)
