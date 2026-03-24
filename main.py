# Llamando funciones del sistema de inventario

from src.inventario import *

# Sistema de inventario de productos
print()
print("Sistema de inventario".upper())


# Program Main
while True:

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

    print()

    try:
        accion = int(input("Escoge la opcion a realizar = "))

        if accion not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            print()
            print("Error: Opción inválida")
            print()
            accion = int(input("Intente nuevamente = "))

    except ValueError:
        print("Error: Tienes que ingresar un valor númerico\n")
        continue

    print()

    if accion == 1:
        agregar_producto()

    elif accion == 2:
        mostrar_inventario()

    elif accion == 3:
        pass

    elif accion == 4:
        pass

    elif accion == 5:
        pass

    elif accion == 6:
        calcular_estadisticas(inventario)

    elif accion == 7:
        pass

    elif accion == 8:
        pass

    else:
        print("Saliendo del inventario\n".upper())
        break
