from producto import Producto


class Inventario:
    """
    Clase que gestiona una lista de productos.
    """

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """
        Añade un producto al inventario asegurando que el ID sea único.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print(" Producto añadido correctamente.")

    def eliminar_producto(self, producto_id):
        """
        Elimina un producto por su ID.
        """
        for p in self.productos:
            if p.get_id() == producto_id:
                self.productos.remove(p)
                print(" Producto eliminado correctamente.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto.
        """
        for p in self.productos:
            if p.get_id() == producto_id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(" Producto actualizado correctamente.")
                return
        print(" Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos que contengan el nombre ingresado.
        """
        resultados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

        if resultados:
            print(" Productos encontrados:")
            for p in resultados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print(" Lista de productos:")
            for p in self.productos:
                print(p)
