#Guardado y carga de datos en archivos JSON. (Responsable: Dev 4)
#Mariana Reyes 
import json
 
def guardar_json(ruta, datos):
    """Guarda la lista de datos en el archivo JSON indicado."""
    with open (ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)
 
 
def cargar_json(ruta):
    """Carga y devuelve los datos del archivo JSON.
 
    Si el archivo no existe, devuelve una lista vacía [].
    """
    pass
