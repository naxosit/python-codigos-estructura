# Se crea la clase Contacto de atributos: nombre, telefono y correo.

class Contacto:

    # Método constructor de la clase contacto

    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

# Se crea la clase ListaContactos de atributos: contactos y primero.

class ListaContactos:

    # Método constructor de la clase ListaContactos.
     
    def __init__(self):
        self.contactos = [] # Lista que almacena los contactos creados de la clase Contacto.
        self.primero = None


    # B) Método que permite agregar un contacto

    def agregar_contacto(self, nombre, telefono, correo):
        nuevo_contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo_contacto)

        if self.primero is None:
            self.primero = nuevo_contacto
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            nuevo_contacto.siguiente = self.primero
            nuevo_contacto.anterior = self.primero.anterior
            self.primero.anterior.siguiente = nuevo_contacto
            self.primero.anterior = nuevo_contacto


    # C) Método que permite mostrar la lista de contactos.

    def mostrar_contactos(self):
        if self.primero is None:
            print("La lista de contactos está vacía.")
        else:
            contacto_actual = self.primero
            while True: # Ciclo que muestra la lista de contactos de forma vertical con todos los atributos de la clase Contacto.
                print(f"Nombre: {contacto_actual.nombre}")
                print(f"Teléfono: {contacto_actual.telefono}")
                print(f"Correo: {contacto_actual.correo}")
                print()
                contacto_actual = contacto_actual.siguiente
                if contacto_actual == self.primero:
                    break

    # D) Método que permite buscar un contacto por su nombre.

    def buscar_contacto(self, nombre):
        if self.primero is None:
            print("La lista de contactos está vacía.")
        else:
            contacto_actual = self.primero
            encontrado = False
            while True: # Ciclo que si encuentra el contacto por el nombre, muestra la lista de con todos los atributos de ese objeto contacto de la clase Contacto.
                if contacto_actual.nombre == nombre:
                    print(f"Nombre: {contacto_actual.nombre}")
                    print(f"Teléfono: {contacto_actual.telefono}")
                    print(f"Correo: {contacto_actual.correo}")
                    encontrado = True
                    break
                contacto_actual = contacto_actual.siguiente
                if contacto_actual == self.primero:
                    break

            if not encontrado:
                print("No se encontró el contacto.")

    # E) Método que permite eliminar un contacto por su nombre

    def eliminar_contacto(self, nombre):
        if self.primero is None:
            print("La lista de contactos está vacía.")
        else:
            contacto_actual = self.primero
            encontrado = False
            while True:
                if contacto_actual.nombre == nombre:
                    contacto_actual.anterior.siguiente = contacto_actual.siguiente
                    contacto_actual.siguiente.anterior = contacto_actual.anterior
                    self.contactos.remove(contacto_actual)
                    encontrado = True
                    break
                contacto_actual = contacto_actual.siguiente
                if contacto_actual == self.primero:
                    break

            if encontrado:
                print("Contacto eliminado.")
            else:
                print("No se encontró el contacto.")


    # F) Método que verifica si la lista está vacía o no.

    def esta_vacia(self):
        return self.primero is None


# Pruebas de los métodos creados.


lista_contactos = ListaContactos()

# B) Se agregan contactos

lista_contactos.agregar_contacto("Juan", "+56988762345", "juan@alumnos.ulagos.cl") # Son números aleatorios, ni idea si realmente existen.
lista_contactos.agregar_contacto("Sofía", "+56922332345", "sofia@alumnos.ulagos.cl")
lista_contactos.agregar_contacto("Paloma", "+56988769054", "paloma@alumnos.ulagos.cl")

# C) Se muetran la lista de contactos añadidos.

lista_contactos.mostrar_contactos()

# D) Se busca el contacto de nombre "Sofía".

lista_contactos.buscar_contacto("Sofía")

# E) Se elimina el contacto de nombre "Paloma".

lista_contactos.eliminar_contacto("Paloma")



# F) Verificar si la lista de contactos está vacía

if lista_contactos.esta_vacia():
    print("La lista de contactos está vacía.")
else:
    print("La lista de contactos no está vacía.")

# Ejecutando el código, en la terminal retorna:

# Nombre: Juan
# Teléfono: +56988762345
# Correo: juan@alumnos.ulagos.cl  

# Nombre: Sofía
# Teléfono: +56922332345
# Correo: sofia@alumnos.ulagos.cl 

# Nombre: Paloma
# Teléfono: +56988769054
# Correo: paloma@alumnos.ulagos.cl

# Nombre: Sofía
# Teléfono: +56922332345
# Correo: sofia@alumnos.ulagos.cl
# Contacto eliminado.
# La lista de contactos no está vacía.



    

