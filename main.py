#Menú principal y flujo del programa. (Responsable: Dev 1)
#Sara Villanueva 

from inventario import registrar_item
inventario=[]

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
    
while True:
    print('BIBLIOSTOCK')
    print('1. Registrar ítem')
    print('2. Listar ítems')
    print('3. Buscar ítem')
    print('4. Registrar préstamo')
    print('5. Registrar devolución')
    print('6. Salir') 
    
    opcion = input("Por favor, seleccione una opcion: ")
    
            
        
        