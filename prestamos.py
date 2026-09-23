
#Gestión de préstamos y devoluciones. (Responsable: Dev 3)
#Valentina Rojas 
 
 
def registrar_prestamo(inventario, prestamos, codigo, usuario, fecha):
    """
    Registra un préstamo y descuenta 1 de cantidad_disponible.
    Debe verificar que el ítem exista y que haya disponibilidad.
    Devuelve el préstamo creado (o None si no se pudo registrar).
    """
    print("\n-- REGISTRAR PRÉSTAMO --")

    if codigo not in inventario:
        print(f"El código {codigo} no existe en el inventario.")
        return None

    item = inventario[codigo]
    if item['cantidad_disponible'] <= 0:
        print(f"No hay disponibilidad para el ítem con código {codigo}.")
        return None

    prestamo = {
        'codigo': codigo,
        'usuario': usuario,
        'fecha': fecha,
        'devuelto': False
    }

    prestamos.append(prestamo)

    item['cantidad_disponible'] -= 1

    print(f"Préstamo registrado: {prestamo}")
    return prestamo

def registrar_prestamo(inventario, prestamos, codigo, usuario, fecha):
    
    """Registra un préstamo y descuenta 1 de cantidad_disponible.
    Debe verificar que el ítem exista y que haya disponibilidad.
    Devuelve el préstamo creado (o None si no se pudo registrar).
    """
    print("\n -- REGISTRAR PRÉSTAMO -- ")

    # Verificar si el ítem existe en el inventario
    if codigo not in inventario:
        print(f"El código {codigo} no existe en el inventario.")
        return None

    # Verificar si hay disponibilidad
    item = inventario[codigo]
    if item['cantidad_disponible'] <= 0:
        print(f"No hay disponibilidad para el ítem con código {codigo}.")
        return None

    # Registrar el préstamo
    prestamo = {
        'codigo': codigo,
        'usuario': usuario,
        'fecha': fecha,
        'devuelto': False
    }
    prestamos.append(prestamo)

    # Actualizar la cantidad disponible en el inventario
    item['cantidad_disponible'] -= 1

    print(f"Préstamo registrado: {prestamo}")
    return prestamo

 
 
def registrar_devolucion(inventario, prestamos, codigo, usuario):
    """Marca un préstamo activo como devuelto y suma 1 a cantidad_disponible.
 
    Devuelve True si la devolución se registró, False en caso contrario.
    """
    print("\n -- REGISTRAR DEVOLUCIÓN -- ")

    # Buscar el préstamo activo correspondiente
    for prestamo in prestamos:
        if prestamo['codigo'] == codigo and prestamo['usuario'] == usuario and not prestamo['devuelto']:
            # Marcar como devuelto
            prestamo['devuelto'] = True

            # Actualizar la cantidad disponible en el inventario
            item = inventario[codigo]
            item['cantidad_disponible'] += 1

            print(f"Devolución registrada para el préstamo: {prestamo}")
            return True

    print(f"No se encontró un préstamo activo para el código {codigo} y usuario {usuario}.")
    return False


