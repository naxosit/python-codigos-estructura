# Crear dos matrices solicitando los datos por consola (cantidad de filas y columnas), y
# los elementos de estas matrices deben ser aleatorios del 1 al 5, no se deben ingresar
# por consola. Luego se deben sumar en una función las matrices, y en otra función
# restarlas. En este caso no se puede utilizar numpy, solo estructuras propias de Python.
import random

filas = int(input ("Introduzca el numero de filas de sus matrices: "))
columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))

matriz1 = []
matriz2 = []
matriz3 = []
matriz_resta = []

for i in range (filas):
	matriz1.append( [0] * columnas)
	matriz2.append( [0] * columnas)
	matriz3.append( [0] * columnas)


for i in range(filas):
	for j in range(columnas):
		matriz1[i][j] = float((random.randint(1, 5)))
print('Su primera matriz es\n', matriz1)


for i in range(filas):
	for j in range(columnas):
		matriz2[i][j] = float((random.randint(1, 5)))
print('Su segunda matriz es\n', matriz2)

# Suma
for i in range(filas):
	for j in range(columnas):
			matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
print('Su matriz suma es\n')
print(matriz3)

# Resta
for i in range(filas):
	for j in range(columnas):
			matriz3[i][j] = matriz1[i][j] - matriz2[i][j]
print('Su matriz resta es\n')
print(matriz3)