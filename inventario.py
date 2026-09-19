
#Gestión de inventario. (Responsable: Dev 2)
#Jesus-Perez
 
 
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
    ubicacion = str(ubicacion).strip() if ubicacion is not None else ""

    if codigo == "" or titulo == "" or autor == "" or categoria == "" or ubicacion == "":
        return None

    if any(item.get("codigo") == codigo for item in inventario):
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

    inventario.append(item)
    return item
 
 
def listar_items(inventario):
    """Muestra en consola todos los ítems registrados."""
    if not inventario:
        print("No hay ítems registrados.")
        return []

    for item in inventario:
        print(
            f"Código: {item.get('codigo', '')} | "
            f"Título: {item.get('titulo', '')} | "
            f"Autor: {item.get('autor', '')} | "
            f"Categoría: {item.get('categoria', '')} | "
            f"Disponible: {item.get('cantidad_disponible', 0)}/{item.get('cantidad_total', 0)} | "
            f"Ubicación: {item.get('ubicacion', '')}"
        )

    return inventario
 
 
def buscar_item(inventario, termino):
    """Busca ítems por código (exacto) o por título (parcial).
 
    Devuelve una lista con los ítems encontrados.
    """
    if inventario is None:
        return []

    termino = str(termino).strip().lower() if termino is not None else ""
    if termino == "":
        return []

    encontrados = []
    for item in inventario:
        codigo = str(item.get("codigo", "")).strip().lower()
        titulo = str(item.get("titulo", "")).strip().lower()

        if codigo == termino or termino in titulo:
            encontrados.append(item)

    return encontrados
