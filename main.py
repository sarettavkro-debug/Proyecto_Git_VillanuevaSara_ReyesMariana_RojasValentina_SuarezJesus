"""BiblioStock CLI - Biblioteca Horizonte.

Menú principal y flujo del programa. (Responsable: Dev 1)
"""

import inventario
import prestamos
import persistencia

RUTA_INVENTARIO = "inventario.json"
RUTA_PRESTAMOS = "prestamos.json"


def mostrar_menu():
    """Imprime el menú principal en consola."""
    pass


def opcion_registrar_item(inventario_datos):
    """Pide por consola los datos de un ítem y lo registra."""
    pass


def opcion_listar_items(inventario_datos):
    """Muestra todos los ítems registrados."""
    pass


def opcion_buscar_item(inventario_datos):
    """Pide un título o código y muestra los resultados."""
    pass


def opcion_registrar_prestamo(inventario_datos, prestamos_datos):
    """Pide ítem, usuario y fecha, y registra el préstamo."""
    pass


def opcion_registrar_devolucion(inventario_datos, prestamos_datos):
    """Pide ítem y usuario, y registra la devolución."""
    pass


def main():
    """Carga los datos, ejecuta el bucle del menú y guarda al salir."""
    pass


if __name__ == "__main__":
    main()
    