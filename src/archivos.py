from src.style_msg import exito,alerta,error
import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
        inventario (list): Lista de productos.
        ruta (str): Ruta del archivo.
        incluir_header (bool): Si incluye encabezado.

    Retorna:
        None
    """
    if not inventario:
        alerta("Inventario está vacío, no se puede guardar.\n")
        return

    try:
        ruta_final = os.path.join("data", ruta)

        with open(ruta_final, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        exito(f"Inventario guardado en: {ruta_final}\n")

    except PermissionError:
        error("Error: No tienes permisos para escribir en esa ruta.\n")
    except Exception as e:
        error(f"Error al guardar el archivo: {e}\n")


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV con validaciones.

    Parámetros:
        ruta (str): Ruta del archivo.

    Retorna:
        tuple: (lista_productos, errores)
    """
    inventario = []
    errores = 0

    try:

        ruta = os.path.join("data", ruta)

        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            # Leer encabezado
            try:
                encabezado = next(reader)
            except StopIteration:
                print("El archivo está vacío.\n")
                return [], 0

            # Validar encabezado
            if encabezado != ["nombre", "precio", "cantidad"]:
                error("Encabezado inválido. Debe ser: nombre,precio,cantidad\n")
                return [], 0

            # Leer filas
            for fila in reader:

                # Validar columnas
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # Validar valores no negativos
                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except ValueError:
                    errores += 1

        return inventario, errores

    except FileNotFoundError:
        error("Error: Archivo no encontrado.\n")
    except UnicodeDecodeError:
        error("Error: Problema de codificación del archivo.\n")
    except Exception as e:
        error(f"Error inesperado: {e}\n")

    return [], 0