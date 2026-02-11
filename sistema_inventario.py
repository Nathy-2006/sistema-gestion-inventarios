"""
Sistema de Gestión de Inventarios
nombre: Nathalia Teresa Barreiro Castro
Asignatura: Programación Orientado a Objetos "E"
Fecha: 15/02/2026
Descripción: Aplicación en consola para gestionar productos de una tienda
"""

from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                producto_id = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(producto_id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "2":
            producto_id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(producto_id)

        elif opcion == "3":
            producto_id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")

            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None

            inventario.actualizar_producto(producto_id, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción no válida.")


if __name__ == "__main__":
    main()
