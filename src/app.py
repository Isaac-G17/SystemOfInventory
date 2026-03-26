from src.servicios import *
from src.style_msg import exito,alerta,error

inventario = [
    {"nombre": "Queso", "precio": 200, "cantidad": 5},
    {"nombre": "lulo", "precio": 300, "cantidad": 4},
]


def pedir_nombre():
    """
    Solicita un nombre válido (solo letras y espacios).
    """
    nombre = ""

    while nombre == "" or not nombre.replace(" ", "").isalpha():
        nombre = input("Ingrese el nombre del producto: ").lower()
        print()

        if nombre == "":
            alerta("Alerta: No dejes el campo vacío\n")
        elif not nombre.replace(" ", "").isalpha():
            error("Error: Solo se permiten letras\n")

    return nombre


def pedir_float(mensaje):
    valor = -1

    while valor <= 0:
        try:
            valor = float(input(mensaje))

            if valor <= 0:
                alerta("Alerta: El precio debe ser mayor a 0\n")

        except ValueError:
            error("Error: Entrada inválida solo se permiten números\n")
            valor = -1
    return valor


def pedir_int(mensaje):
    """
    Solicita un número entero válido al usuario.

    Parámetros:
        mensaje (str): Texto a mostrar.

    Retorna:
        int: Valor ingresado válido.
    """
    valor = -1

    while valor <= 0:
        try:
            valor = int(input(mensaje))

            if valor <= 0:
                alerta("Alerta: La cantidad debe ser mayor a 0\n")

        except ValueError:
            error("Error: Entrada inválida solo se permiten números\n")
            valor = -1

    return valor


def menu():
    """
    Muestra el menú principal y controla el flujo del programa.

    Retorna:
        None
    """
    accion = 0

    while accion != 9:

        print("-Menu-----------------------------".upper())
        print("| 1 → Agregar producto           |")
        print("| 2 → Mostrar inventario         |")
        print("| 3 → Buscar producto            |")
        print("| 4 → Actualizar producto        |")
        print("| 5 → Eliminar producto          |")
        print("| 6 → Estadísticas de inventario |")
        print("| 7 → Guardar CSV                |")
        print("| 8 → Cargar CSV                 |")
        print("| 9 → Salir                      |")
        print("-" * 34)
        try:
            accion = int(input("Seleccione una opción: "))

            print()

        except ValueError:
            error("Opción inválida\n")
            continue

        if accion == 1:
            print("-------Agregar producto-------\n".upper())

            continuar = "si"

            while continuar in ("si", "s", "yes"):

                nombre = pedir_nombre()
                print()
                precio = pedir_float("Ingrese el precio de su producto $")
                print()
                cantidad = pedir_int("Ingrese la cantidad de su producto: ")
                print()

                agregar_producto(inventario, nombre, precio, cantidad)

                exito(f"Producto agregado correctamente\n")

                continuar = input("¿Quiere agregar otro producto? (Si/No): ").lower()

                print()

                if continuar not in ("si", "s", "yes"):
                    print("------Volviendo al menu-------\n".upper())

        elif accion == 2:
            mostrar_inventario(inventario)

        elif accion == 3:
            print("-------Buscar producto-------\n".upper())
            
            continuar = "si"
            
            while continuar in ("si", "s", "yes"):
                
                nombre = pedir_nombre()
                producto = buscar_producto(inventario, nombre)

                if producto:
                    print(f"{producto}\n")
                else:
                    alerta(f"Producto no encontrado\n")
                
                continuar = input("¿Quiere buscar otro producto? (Si/No): ").lower()
                print()

                if continuar not in ("si", "s", "yes"):
                    print("------Volviendo al menu-------\n".upper())

        elif accion == 4:
            print("------Actulizar producto------\n".upper())
            
            continuar = "si"
            
            while continuar in ("si", "s", "yes"):
                
                nombre = pedir_nombre()
                producto = buscar_producto(inventario, nombre)
                
                if producto is None:
                    alerta(f"Producto no encontrado\n")

                else:
                    editar_precio = input("Quieres editar el precio del producto? (Si/No):").lower()
                    
                    if editar_precio == "si":
                        print()

                        nuevo_precio = pedir_float("Ingrese el nuevo precio de su producto: $")

                        print()
                    else:
                        nuevo_precio = None

                    editar_cantidad = input("Quieres editar la cantidad del producto? (Si/No):").lower()

                    if editar_cantidad == "si":
                        print()
                        nueva_cantidad = pedir_int("Ingrese la nueva cantidad de su producto: ")
                        print()
                    else:
                        nueva_cantidad = None

                    if nuevo_precio is not None or nueva_cantidad is not None:
                        actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
                    else:
                        alerta("No se realizaron cambios\n")

                continuar = input("¿Quiere actualizar otro producto? (Si/No): ").lower()

                print()

                if continuar not in ("si", "s", "yes"):
                    print("------Volviendo al menu-------\n".upper())

        elif accion == 5:
            print("------Eliminar producto------\n".upper())
            
            continuar = "si"
            
            while continuar in ("si", "s", "yes"):
                
                nombre = pedir_nombre()
                
                eliminar_producto(inventario, nombre)

                continuar = input("¿Quiere eliminar otro producto? (Si/No): ").lower()

                print()

                if continuar not in ("si", "s", "yes"):
                    print("------Volviendo al menu-------\n".upper())

        elif accion == 6:
            print("----Estadisticas de inventario----\n".upper())

            stats = calcular_estadisticas(inventario)

            if stats:
                print(f"Total productos: {stats['productos_registrados']}\n")
                print(f"Unidades totales: {stats['unidades_totales']}\n")
                print(f"Valor total: ${stats['valor_total']:.2f}\n")
                print(f"Producto más caro: {stats['producto_mas_caro']['nombre']} | ${stats['producto_mas_caro']['precio']:.2f}\n")
                print(f"Mayor stock: {stats['producto_mayor_stock']['nombre']} | {stats['producto_mayor_stock']['cantidad']:.2f}\n")
            else:
                print("Inventario vacío\n")

            print("------Volviendo al menu-------\n".upper())

        elif accion == 9:
            exito("Saliendo del inventario\n".upper())
        else:
            error("Error: Opción inválida\n")
            