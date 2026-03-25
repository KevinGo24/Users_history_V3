import csv
import os

def cargar_csv(ruta):
    """
    Lee un archivo CSV y lo convierte en la lista de inventario.
    """
    # 1. Verificar si el archivo existe antes de intentar abrirlo
    if not os.path.exists(ruta):
        print(f"El archivo '{ruta}' no existe. Iniciando con inventario vacío.")
        return []

    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            # DictReader usa la primera fila (nombre,precio,cantidad) como llaves
            lector = csv.DictReader(archivo)
            inventario = []
            
            for fila in lector:
                # Convertimos los datos a sus tipos correctos (números)
                # ya que el CSV siempre lee todo como texto (strings)
                producto = {
                    'name': fila['nombre'],
                    'price': float(fila['precio']),
                    'quantity': int(fila['cantidad'])
                }
                inventario.append(producto)
                
            print(f"Inventario cargado exitosamente desde: {ruta}")
            return inventario

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return []
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return []