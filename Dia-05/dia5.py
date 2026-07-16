compras = []

while True:
    menu = """
    === Menu ===
    1. Agregar item
    2. Quitar item
    3. Mostrar lista
    4. Salir
    """
    print(menu)
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        item = input("Ingresa item: ")
        compras.append(item)
        print(f"Item guardado correctamente")
    elif opcion == 2:
        item_remove = input("Ingresa item a eliminar: ")
        compras.remove(item_remove)
        print(f"Item eliminado correctamente")
    elif opcion == 3:
        if len(compras) < 1:
            print("No tienes elementos guardados")
        else:
            print("=== Lista Items")
            for item in compras:
                print(f"-> {item}")
    elif opcion == 4:
        print("Saliendo...")
        break
    else:
        print("opcion invalida intente de nuevo") 