# Sistema de inventario de productos
print("Sistema de inventario\n".upper())

inventario = []

while True:
    print("¿Que acción va a realizar?".upper())

    print()

    print("1 → Agregar producto")
    print("2 → Mostrar inventario")
    print("3 → Calcular estadísticas")
    print("4 → Salir")

    print()

    accion = int(input("Escoge la opcion a realizar = "))

    while accion not in (1, 2, 3, 4):

        print()
        print("Opción inválida")
        print()

        accion = int(input("Intenta nuevamente = "))

    print()

    if accion == 1:
        print("----Agregar producto----\n".upper())
        while True:
            while True:
                # Entrada de los datos del producto y validacion de los datos
                nombre = input("Ingrese el nombre de su producto: ".upper())
                print()

                if nombre.replace(" ", "").isalpha():
                    break

                elif nombre == "":
                    print()
                    print(
                        "Por favor ingresa el nombre del producto, no dejes el campo vacío"
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
                        print("Ingrese un precio valido, Intente nuavamente")
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
                        print("Ingrese una cantidad mayor a 0, Intente nuavamente")
                        print()
                        continue
                    break

                except ValueError:
                    print("Error: Tienes que ingresar un valor númerico")
                    print()

            producto = {
                "Nombre": nombre,
                "Precio": precio,
                "Cantidad": cantidad
            }

            inventario.append(producto)
                
            print("Producto agregado correctamente.\n")
           
            continuar = input("¿Quiere agregar otro producto? (Si/No): ".lower())

            print()
        
            if continuar != "si":
                print("----Volviendo al menu----".upper())
                break  

    elif accion == 2:
        print("----Mostrando inventario----\n".upper())

        if not inventario:
            print ("Inventario Vacio\n")

        else:
            for p in inventario:
                print(f"Producto: {p['Nombre']} | Precio: ${p['Precio']} | Cantidad: {p['Cantidad']}")
        
        print("----Volviendo al menu----\n".upper())

    #elif accion == 3:
        

    else:
        print("Saliendo del inventario".upper())
        break

    # Operacion matemática para sacar el total

    # costo_total = precio * cantidad

    # Mostras resultado en consola

    # print("PRODUCTO =", nombre)
    # print("PRECIO =", precio)
    # print("CANTIDAD =", cantidad)
    # print("TOTAL =", costo_total)
