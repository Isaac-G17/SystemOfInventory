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

    try:
        accion = int(input("Escoge la opcion a realizar = "))
        
        if accion not in (1, 2, 3, 4):
            print()
            print("Opción inválida")
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
        calcular_estadisticas() 

    else:
        print("Saliendo del inventario\n".upper())
        break
        