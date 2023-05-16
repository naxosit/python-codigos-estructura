# Crear dos matrices solicitando la cantidad de filas y columnas por teclado.
# Los elementos deben ser enteros generados de manera aleatoria (números
# del 1 al 5).
# Ítem uno
print("ITEM I")
import random

filas = int(input("Introduzca el número de filas: "))
columnas = int(input("Introduzca el número de columas: "))

matriz_uno = []
matriz_dos = []
matriz_tres = []
for i in range(filas):
	matriz_uno.append( [0] * columnas)
	matriz_dos.append( [0] * columnas)
	matriz_tres.append( [0] * columnas)
for i in range(filas):
	for j in range(columnas):
		matriz_uno[i][j] = int((random.randint(1,5)))
		matriz_dos[i][j] = int((random.randint(1,5)))
print(f"Primera matriz {matriz_uno}")
print(f"Segunda matriz {matriz_dos}")

def suma_matrices(matriz1, matriz2):
	for i in range(filas):
		for j in range(columnas):
			matriz_tres[i][j] = matriz1[i][j] + matriz2[i][j]
	return matriz_tres
            
print(f"La suma de matriz uno, más la matriz dos es {suma_matrices(matriz_uno, matriz_dos)}")



# Ítem dos
print("\nITEM II")
import numpy as np
k = int(input("Ingrese un escalar del 1-10: "))
if k < 1 or k > 10:
	print("Valor de k no válido.")
else:
    matriz_tres_np = np.array(matriz_tres)
    mult_matriz3 = np.multiply(matriz_tres_np, k)
    print(f"La multiplicación de {k} * {matriz_tres}, es {mult_matriz3}")

# Ítem tres

print("\nITEM III")
filas_matriz_final = int(input("Ingrese el número de filas de su nueva matriz: "))
columnas_matriz_final = int(input("Ingrese el número de columnas de su nueva matriz: "))
matriz_final = []
for i in range(filas_matriz_final):
	matriz_final.append([0] * columnas_matriz_final)
for i in range(filas_matriz_final):
	for j in range(columnas_matriz_final):
		matriz_final[i][j] = int(input("Elementos nueva matriz: "))

matriz_final_np = np.array(matriz_final)
print(f"Matriz final es \n{matriz_final_np}")

if columnas == filas_matriz_final:
	print(f"Finalmente, se tiene la matriz \n{np.matmul(mult_matriz3, matriz_final_np)}")
else:
	print("No se cumple que la cantidad de columnas de la primera matriz, sea semejante a la cantidad de filas de la segunda matriz.")
