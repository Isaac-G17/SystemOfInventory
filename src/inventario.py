print("Sistema de inventario\n")

#Entrada de los datos del producto y validacion de los datos
nombre = input("Ingrese el nombre de su producto: ")
print()

while True:
    if nombre.replace(" ","").isalpha():
        break

    elif nombre == "":
        print()
        print("Por favor ingresa el nombre del producto, no dejes el campo vacío")
        print()
        nombre = input("Ingrese el nombre de su producto: ")
        print()

    else:
        print()
        print("Entrada invalida, solo se permiten letras")
        print()
        nombre = input("Ingrese el nombre de su producto: ")
        print()


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


#Operacion matemática para sacar el total

costo_total = precio * cantidad

#Mostras resultado en consola

print("PRODUCTO =", nombre)
print("PRECIO =", precio)
print("CANTIDAD =", cantidad)
print("TOTAL =", costo_total)