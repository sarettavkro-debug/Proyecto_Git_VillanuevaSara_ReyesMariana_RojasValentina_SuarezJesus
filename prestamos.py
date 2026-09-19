
#Gestión de préstamos y devoluciones. (Responsable: Dev 3)
 
 
def registrar_prestamo(inventario, prestamos, codigo, usuario, fecha):
    """Registra un préstamo y descuenta 1 de cantidad_disponible.
 
    Debe verificar que el ítem exista y que haya disponibilidad.
    Devuelve el préstamo creado (o None si no se pudo registrar).
    """
    pass
 
 
def registrar_devolucion(inventario, prestamos, codigo, usuario):
    """Marca un préstamo activo como devuelto y suma 1 a cantidad_disponible.
 
    Devuelve True si la devolución se registró, False en caso contrario.
    """
    pass

