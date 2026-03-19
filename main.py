#Llamando funciones del sistema de inventario 

from src.inventario import *

# Sistema de inventario de productos
print()
print("Sistema de inventario".upper())
 

#Program Main    
while True:

    print("-Menu-------------------------".upper())
    print("| 1 → Agregar producto       |")
    print("| 2 → Mostrar inventario     |")
    print("| 3 → Calcular estadísticas  |")
    print("| 4 → Salir                  |")
    print("-"*30)

    print()

    accion = int(input("Escoge la opcion a realizar = "))

    while accion not in (1, 2, 3, 4):

        print()
        print("Opción inválida")
        print()

        accion = int(input("Intente nuevamente = "))

    print()

    if accion == 1:       
        agregar_producto()

    elif accion == 2:
        mostrar_inventario()
              
    elif accion == 3:
        print("----Caculando estadisticas de inventario----\n".upper())

        calcular_estadisticas() 

        print("----Volviendo al menu----".upper())

    else:
        print("Saliendo del inventario\n".upper())
        break