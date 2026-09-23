
#Gestión de inventario. (Responsable: Dev 2)
#Jesus-Perez
#funciones terminadas: registrar_item, listar_items, buscar_item
#estoy de nuevo en mi rama
def registrar_item(inventario, codigo, titulo, autor, categoria, cantidad_total, ubicacion):
    """Registra un ítem nuevo en el inventario.

    Debe validar que el código no esté vacío ni repetido y que
    cantidad_total sea un entero mayor que 0.
    Devuelve el ítem creado (o None si no se pudo registrar).
    """
    if inventario is None:
        return None

    codigo = str(codigo).strip() if codigo is not None else ""
    titulo = str(titulo).strip() if titulo is not None else ""
    autor = str(autor).strip() if autor is not None else ""
    categoria = str(categoria).strip() if categoria is not None else ""
    cantidad_total = str(cantidad_total).strip() if cantidad_total is not None else ""
    ubicacion = str(ubicacion).strip() if ubicacion is not None else ""

    if codigo == "" or titulo == "" or autor == "" or categoria == "" or ubicacion == "":
        return None
    
    if codigo in inventario:
        return None

    try:
        cantidad_total = int(cantidad_total)
    except (TypeError, ValueError):
        return None

    if isinstance(cantidad_total, bool) or cantidad_total <= 0:
        return None

    item = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "cantidad_total": cantidad_total,
        "cantidad_disponible": cantidad_total,
        "ubicacion": ubicacion
    }

    inventario[codigo]= item
    return item


def listar_items(inventario):
    items = inventario.values() if isinstance(inventario, dict) else inventario
    
    for item in items:
        print(f"Código: {item.get('codigo', '')} | Título: {item.get('titulo', '')} | Autor: {item.get('autor', '')}")


def buscar_item(inventario, termino):
    termino = termino.strip().lower()
    resultados = []
    
    items = inventario.values() if isinstance(inventario, dict) else inventario

    for item in items:
        codigo = str(item.get("codigo", "")).strip().lower()
        titulo = str(item.get("titulo", "")).strip().lower()

        if termino in codigo or termino in titulo:
            resultados.append(item)

    return resultados
