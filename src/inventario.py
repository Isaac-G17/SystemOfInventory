inventario = [
    {
      "nombre": "Queso",
      "precio": 2000000,
      "cantidad": 3
    },
    {
      "nombre": "Lulo",
      "precio": 300,
      "cantidad": 4
    }
]

def agregar_producto():
    while True:
            while True:
                print("-------Agregar producto-------\n".upper())

                # Entrada de los datos del producto y validacion de los datos
                nombre = input("Ingrese el nombre de su producto: ")
                print()

                if nombre.replace(" ", "").isalpha():
                    break

                elif nombre == "":
                    print()
                    print(
                        "No dejes el campo vacío, por favor ingresa el nombre del producto"
                    )
                    continue

                else:
                    print()
                    print("Entrada invalida, solo se permiten letras")
                    continue

            while True:
                try:
                    precio = float(input("Ingrese el precio de su producto $"))
                    print()

                    if precio <= 0:
                        print("Ingrese un precio valido, Intente nuevamente")
                        print()
                        continue
                    break
                    

                except ValueError:
                    print("Error: Tienes que ingresar un valor númerico")
                    print()

            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad de su producto: "))
                    print()

                    if cantidad <= 0:
                        print("Ingrese una cantidad mayor a 0, Intente nuevamente")
                        print()
                        continue
                    break
                except ValueError:
                    print("Error: Tienes que ingresar un valor númerico")
                    print()
            
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }

            inventario.append(producto)
                
            print("Producto agregado correctamente.\n")
            continuar = input("¿Quiere agregar otro producto? (Si/No): ").lower()

            print()
        
            if continuar not in ("si","s","yes"):
                print("------Volviendo al menu-------\n".upper())
            break  

def mostrar_inventario():
    print("-----Mostrando inventario-----\n".upper())
        
    print("+---------------+-------------+-----------+")
    print("| PRODUCTO      | PRECIO      | CANTIDAD  |")
    print("+---------------+-------------+-----------+")
    if not inventario:
            print ("Inventario Vacio\n")

    else:
        for p in inventario:
            print(f"| {p['nombre']:<13} | ${p['precio']:<10} | {p['cantidad']:<9} |")

    print("+---------------+-------------+-----------+\n")
    print("------Volviendo al menu-------\n".upper())


def calcular_estadisticas():
    print("----Caculando estadisticas de inventario----\n".upper())

    total_productos = len(inventario)
    total_precio = 0
    total_unidades = 0

    # Operacion matemática para tener las estadisticas de inventario
    for p in inventario:
        total_precio += p['precio'] * p['cantidad']
        total_unidades += p['cantidad']


    print(f"El total de productos es: {total_productos}\n")
    print(f"La cantidad total de productos registrados es: {total_unidades}\n")
    print(f"El valor total del inventario es: ${total_precio}\n")

    print("-------------Volviendo al menú--------------\n".upper())
