import random
import numpy as np

# Se determinan las filas y columnas
filas = 3
columnas = 3

matriz = []

for i in range (filas):
	matriz.append( [0] * columnas)

for i in range(filas):
	for j in range(columnas):
		matriz[i][j] = int(random.randint(5, 10))

matriz_np= np.array(matriz)

# Se obtiene la determinante
determinante = np.linalg.det(matriz_np)


import random
import numpy as np

# Se determinan las filas y columnas de ambas matrices
filas = 3
columnas = 3

matriz_uno = []
matriz_dos = []
for i in range (filas):
	matriz_uno.append( [0] * columnas)
	matriz_dos.append( [0] * columnas)

for i in range(filas):
	for j in range(columnas):
		matriz_uno[i][j] = int(random.randint(-10, -5 ))
		matriz_dos[i][j] = int(random.randint(-10, -5 ))
	
# Se transforman las matrices a arreglos numpy
matriz1 = np.array(matriz_uno)
matriz2 = np.array(matriz_dos)
print(f"Matriz uno: \n{matriz1}\n")
print(f"Matriz dos: \n{matriz2}\n")
resultado = np.matmul(matriz_uno, matriz_dos)

# Condicional que determina las dimensiones de las matrices uno y dos
if filas == columnas:
	print(f"Resultado de matriz uno por matriz dos: \n{resultado}")
else:
    print("Las matrices no son de igual dimensión.")

# Se define la matriz identidad 
matriz_identidad = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Se multiplica el resultado anterior con la matriz identidad
matriz_final = np.matmul(resultado, matriz_identidad)
print(f"\nMatriz resultante por identidad: \n{matriz_final}")
