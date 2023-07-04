#RETO CLASE 21/04/23
# Escribir un programa que pida al usuario una palabra y muestre por
# pantalla el número de veces que contiene cada vocal.



def contador_de_vocales(palabra):
    return sum(map(palabra.lower().count, 'aeiouAEIOUáéíóúÁÉÍÓÚ')) # map es una función que te permite transformar un iterable completo usando otra función

palabra1 = input("Ingrese la palabra: ") # Es la palabra solicitada
print(contador_de_vocales(palabra1)) # Imprime en números cuantas vocales tiene la palabra ingresada

# Crear un arreglo aleatorio de tamaño entre 10 a 30. Imprimir el arreglo
# creado y luego solicitar por consola la búsqueda de un elemento en
# específico del arreglo creado. Todo esto utilizando import array.

import array 
import random 

tamaño_arreglo = random.randint(10, 30) # Se define el tamaño del arreglo
arreglo = array.array('i', [random.randint(1, 100) for i in range(tamaño_arreglo)])

print(arreglo) # Imprime el arreglo de números aleatorios, con un rango de tamaño definido

busqueda_elemento = int(input("Introduce el elemento a buscar: "))

if busqueda_elemento in arreglo:
    print("Se encuentra en la posición ", arreglo.index(busqueda_elemento))
else:
    print("Su elemento a buscar, no se encuetra en el arreglo.")
