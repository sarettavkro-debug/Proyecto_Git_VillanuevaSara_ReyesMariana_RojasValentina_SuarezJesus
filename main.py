#Menú principal y flujo del programa. (Responsable: Dev 1)
#Sara Villanueva 

from inventario import registrar_item
from inventario import listar_items
from inventario import buscar_item


inventario=[]

RUTA_INVENTARIO = "inventario.json"
RUTA_PRESTAMOS = "prestamos.json"


while True:
    print()
    print("=" * 42)
    print('BIBLIOSTOCK CLI - BIBLIOTECA HORIZONTE')
    print("=" * 42)
    print('1. Registrar ítem')
    print('2. Listar ítems')
    print('3. Buscar ítem')
    print('4. Registrar préstamo')
    print('5. Registrar devolución')
    print('6. Salir') 
    print("=" * 42)
    
    opcion = input("Por favor, seleccione una opcion: ")
    
    if opcion == '6':
        print("Saliste del programa, ¡hasta luego!")
        break
    
    elif opcion == '1':
        codigo = input("Ingrese el código: ")
        titulo = input("Ingrese el título: ")
        autor = input("Ingrese el autor: ")
        categoria = input("Ingrese la categoría: ")
        cantidad_total = input("Ingrese la cantidad total: ")
        ubicacion = input("Ingrese la ubicación: ")

        item_creado = registrar_item(inventario, codigo, titulo, autor, categoria, cantidad_total, ubicacion)

        if item_creado:
            print("¡Ítem registrado con éxito!")
            print("\n")
            
        else:
            print("No se pudo registrar el ítem. Verifica los datos ingresados.")
            print("\n")
            
    elif opcion == '2': 
        listar_items(inventario)
        
    elif opcion == '3':
        termino = input("Ingrese el código o título a buscar: ")
        resultados = buscar_item(inventario, termino)

    if resultados:
        print("\n--- Ítems encontrados ---")
        for item in resultados:
            print(f"Código: {item.get('codigo')} | Título: {item.get('titulo')} | Autor: {item.get('autor')} | Cantidad: {item.get('cantidad_total')}")
    else:
        print("No se encontraron ítems que coincidan con la búsqueda.")
        
    
    
    
    
            
        
        