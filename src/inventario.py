inventario = [
    {"nombre": "Queso", "precio": 200.0, "cantidad": 3},
    {"nombre": "Lulo", "precio": 300.0, "cantidad": 4},
    {"nombre": "Arroz", "precio": 400.0, "cantidad": 4},
]


def agregar_producto():
    print("-------Agregar producto-------\n".upper())
    while True:
        while True:
            # Entrada de los datos del producto y validacion de los datos
            nombre = input("Ingrese el nombre de su producto: ")
            print()

            if nombre.replace(" ", "").isalpha():
                break

            elif nombre == "":
                print(
                    "No dejes el campo vacío, por favor ingresa el nombre del producto\n"
                )
                continue

            else:
                print("Entrada invalida, solo se permiten letras\n")
                continue

        while True:
            try:
                precio = float(input("Ingrese el precio de su producto $"))
                print()

                if precio <= 0:
                    print("Error: Ingrese un precio valido, Intente nuevamente\n")
                    continue
                break
            except ValueError:
                print()
                print("Error: Tienes que ingresar un valor númerico\n")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de su producto: "))
                print()

                if cantidad <= 0:
                    print("Error: Ingrese una cantidad mayor a 0, Intente nuevamente\n")
                    continue
                break
            except ValueError:
                print()
                print("Error: Tienes que ingresar un valor númerico\n")

        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}

        inventario.append(producto)

        print("Producto agregado correctamente.\n")
        continuar = input("¿Quiere agregar otro producto? (Si/No): ").lower()

        print()

        if continuar not in ("si", "s", "yes"):
            print("------Volviendo al menu-------\n".upper())
        break

def mostrar_inventario():
    print("-----Mostrando inventario-----\n".upper())

    print("+---------------+-------------+-----------+")
    print("| PRODUCTO      | PRECIO      | CANTIDAD  |")
    print("+---------------+-------------+-----------+")
    if not inventario:
        print("Inventario Vacio\n")

    else:
        for p in inventario:
            print(f"| {p['nombre']:<13} | ${p['precio']:<10} | {p['cantidad']:<9} |")

    print("+---------------+-------------+-----------+\n")
    print("------Volviendo al menu-------\n".upper())


def calcular_estadisticas(inventario):
    print("----Caculando estadisticas de inventario----\n".upper())

    total_productos = len(inventario)
    valor_total = 0
    unidades_totales = 0

    # Operacion matemática para tener las estadisticas de inventario
    for p in inventario:
        valor_total += p["precio"] * p["cantidad"]
        unidades_totales += p["cantidad"]

    producto_max = max(inventario, key=lambda p: p["precio"])
    max_cantidad = max(inventario, key=lambda p: p["cantidad"])

    print(f"Productos en total: {total_productos}\n")
    print(f"Unidades totales: {unidades_totales}\n")
    print(f"Valor total: ${valor_total}\n")
    print(f"Producto más caro: {producto_max['nombre']} | {producto_max['precio']}\n")
    print(
        f"Producto con mayor stock: {max_cantidad['nombre']} | {max_cantidad['cantidad']}\n"
    )
    print("-------------Volviendo al menú--------------\n".upper())
