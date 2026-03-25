import csv

def save_csv(inventory_list):
    with open('inventory.csv', 'w', newline='', encoding='utf-8') as file:
        if not inventory_list:
            return
        # Usamos las llaves del primer diccionario como encabezados
        writer = csv.DictWriter(file, fieldnames=inventory_list[0].keys())
        writer.writeheader()
        writer.writerows(inventory_list)
    print("¡Datos guardados en inventory.csv!")

def load_csv():
    try:
        with open('inventory.csv', 'r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return [] # Si no existe el archivo, devuelve lista vacía
