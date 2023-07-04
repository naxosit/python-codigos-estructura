#Crear un algoritmo donde se solicite dos matrices por consola. Tanto la cantidad de columnas
#como de filas, deben ser ingresadas por teclado. Los elementos de las matrices deben ser
#generados de forma aleatoria (0 al 5). Estas dos matrices se deben sumar. Luego se solicita
#una tercera matriz. Al igual que las dos anteriores, se ingresan columnas y filas por consola, y
#sus elementos son generados aleatoriamente (0 a 5). Esta última matriz se restará con la
#matriz resultante entre la operación de suma.
import random
m1_filas = int(input("Ingrese la cantidad de filas para la primera matriz: "))
m1_columnas = int(input("Ingrese la cantidad de columnas para la primera matriz: "))
m1 = [[random.randint(0,5) for j in range(m1_columnas) for i in range(m1_filas)]]
print("La primera matriz, es: ", m1)
m2_filas = int(input("Ingrese la cantidad de filas para la segunda matriz: "))
m2_columnas = int(input("Ingrese la cantidad de columnas para la segunda matriz: "))
m2 = [[random.randint(0,5) for j in range(m2_columnas) for i in range(m2_filas)]]
print("La segunda matriz, es: ", m2)
m_suma = m1 + m2
print("La suma de la primera y segunda matriz, es ", m_suma)
m3_filas = int(input("Ingrese la cantidad de filas para la tercera matriz: "))
m3_columnas = int(input("Ingrese la cantidad de columnas para la tercera matriz: "))
m3 = [[random.randint(0,5) for j in range(m2_columnas) for i in range(m2_filas)]]
m_final = m3 - m_suma
print("La matriz resultante de la resta de la tercera matriz, con la suma de la primera y segunda matriz, es: ", m_final) # Marca un error de que no se puede restar en una lista.


#Crear una matriz la cual se debe solicitar por teclado la cantidad de filas y columnas que va a
#contener. También ingresar por consola un escalar. Los elementos de la matriz deben ser
#generados aleatoriamente (0 al 10). Por último, se debe multiplicar la matriz generada por el
#escalar ingresado.
import random

m1_filas = int(input("Ingrese la cantidad de filas para la primera matriz: "))
m1_columnas = int(input("Ingrese la cantidad de columnas para la primera matriz: "))
m1 = [[random.randint(0,10) for j in range(m1_columnas) for i in range(m1_filas)]]
escalar = int(input("Ingrese el escalar: "))
print("La matriz 1, es: ", m1)
matriz_resultante = escalar * m1
print(matriz_resultante) #En vez de multiplicar el escalar por cada componente de la matriz, me repetía la lista por el escalar ingresado.
