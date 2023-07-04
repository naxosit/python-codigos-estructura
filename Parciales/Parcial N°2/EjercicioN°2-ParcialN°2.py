# Se crea la clase nodo, de atributos: codigo, nombre, descripcion y cantidad.

class Nodo:
    def __init__(self, codigo, nombre, descripcion, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.anterior = None
        self.siguiente = None

# Se crea la clase Inventario.

class Inventario:
    def __init__(self):
        self.cabeza = None

    # A) Método que nos permite agregar artículo al inventario ingresando todos los atributos correspondientes.

    def agregar_articulo(self, codigo, nombre, descripcion, cantidad):
        nuevo_articulo = Nodo(codigo, nombre, descripcion, cantidad)
        if self.cabeza is None:
            self.cabeza = nuevo_articulo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_articulo
            nuevo_articulo.anterior = actual
    
    # B) Método que nos permite eliminar un artículo del inventario utilizando su código.

    def eliminar_articulo(self, codigo): # Únicamente se requiere el código del objeto artículo para la eliminación del mismo.
        actual = self.cabeza
        while actual:
            if actual.codigo == codigo:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = actual.anterior
                else:
                    self.cabeza = actual.siguiente
                    if actual.siguiente:
                        actual.siguiente.anterior = None
                return
            actual = actual.siguiente

    # C) Método que nos permite buscar un artículo del inventario utilizando su código.

    def buscar_articulo(self, codigo): # Únicamente se requiere el código del objeto artículo para la eliminación del mismo.
        actual = self.cabeza
        while actual:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None
    
    # D) Método que nos permite actualizar la cantidad disponible de un artículo.

    def actualizar_cantidad(self, codigo, nueva_cantidad):
        articulo = self.buscar_articulo(codigo)
        if articulo:
            articulo.cantidad = nueva_cantidad

    # E) Mostrar todos los artículos del inventario de forma 
    
    def mostrar_inventario(self):
        inventario = [] # Se crea una lista vacía que almacena los artículos
        pass # Debería de crear un algoritmo que ordene de forma ascendente los artículos según el número de su código.
        # Para ello, creo que se utilizaría la instrucción de lista 'sort'.

# Ejemplos de uso y pruebas de código.

# Se crea el inventario usando la clase Inventario.

inventario = Inventario()

# A) Se agregan los artículos al inventario creado anteriormente.

inventario.agregar_articulo("001", "iPhone 12 pro max", "Teléfono IOS.", 7)
inventario.agregar_articulo("002", "Huawei 10T", "Teléfono android.", 5)
inventario.agregar_articulo("003", "Acer nitro 5", "Notebook intel core i5.", 8)

# B) Eliminar un artículo del inventario

inventario.eliminar_articulo("002")

# C) Buscar un artículo por su código

articulo = inventario.buscar_articulo("003")
if articulo:
    print(f"Artículo encontrado: Código: {articulo.codigo}, Nombre: {articulo.nombre}, Descripción: {articulo.descripcion}, Cantidad: {articulo.cantidad}")
else:
    print("Artículo no encontrado"
          )
# D) Actualizar la cantidad disponible de un artículo

inventario.actualizar_cantidad("001",5)

# E) Mostrar todos los artículos del inventario de forma ascentente.

inventario.mostrar_inventario() # Teóricamente, esto debiese de ser que muestre primero el iPhone, segundo el Huawei y tercero el Acer nitro 5.

# Ejecutando el código, en la terminal retorna :

# Artículo encontrado: Código: 003, Nombre: Acer nitro 5, Descripción: Notebook intel core i5., Cantidad: 8




           