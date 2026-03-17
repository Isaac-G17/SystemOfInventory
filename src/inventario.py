# Sistema de inventario de productos
print("Sistema de inventario\n".upper())

inventario = []

def agregar_producto():
    while True:
            while True:
                # Entrada de los datos del producto y validacion de los datos
                nombre = input("Ingrese el nombre de su producto: ")
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
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }

            inventario.append(producto)
                
            print("Producto agregado correctamente.\n")
           
            continuar = input("¿Quiere agregar otro producto? (Si/No): ".lower())

            print()
        
            if continuar != "si":
                print("----Volviendo al menu----".upper())
                break  

def mostrar_inventario():
    if not inventario:
            print ("Inventario Vacio\n")

    else:
        for p in inventario:
            print(f"Producto: {p['nombre'].upper()} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}\n")

def calcular_estadisticas():
    total_productos = len(inventario)
    total_precio = 0
    total_unidades = 0

     # Operacion matemática para sacar el total
    for p in inventario:
        total_precio += p['precio'] * p['cantidad']
        total_unidades += p['cantidad']


    print(f"El total de productos es: {total_productos}\n")
    print(f"La cantidad total de productos registrados es: {total_unidades}\n")
    print(f"El valor total del inventario es: ${total_precio}\n")
    
#Program Main    
while True:

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
        
        agregar_producto()

    elif accion == 2:
        print("----Mostrando inventario----\n".upper())

        mostrar_inventario()
        
        print("----Volviendo al menu----".upper())

    elif accion == 3:
        print("----Caculando estadisticas de inventario----\n".upper())

        calcular_estadisticas() 

        print("----Volviendo al menu----".upper())

    else:
        print("Saliendo del inventario".upper())
        break