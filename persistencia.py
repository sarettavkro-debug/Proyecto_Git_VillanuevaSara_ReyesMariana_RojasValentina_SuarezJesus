#Guardado y carga de datos en archivos JSON. (Responsable: Dev 4)
#Mariana Reyes 
import json
 
def guardar_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)
 
 
def cargar_json(ruta):

    try:
        with open (ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []