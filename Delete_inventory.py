def delete(inventory_list):
    if not inventory_list:
        print("El inventario está vacío.")
        return

    target = input("Ingrese el ID o Nombre del producto a eliminar: ")
    encontrado = False

    for item in inventory_list:
        # Suponiendo que tus llaves son 'id' o 'name'
        if item.get('name') == target or item.get('price') == target:
            inventory_list.remove(item)
            encontrado = True
            print(f"Producto '{target}' eliminado con éxito de la memoria.")
            break 
    
    if not encontrado:
        print("No se encontró el producto.")
