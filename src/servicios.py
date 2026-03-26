from src.style_msg import exito,alerta

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto (>= 0).
        cantidad (int): Cantidad disponible (>= 0).

    Retorna:
        None
    """
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario en consola.

    Parámetros:
        inventario (list): Lista de productos.

    Retorna:
        None
    """
    print("-----Mostrando inventario-----\n".upper())
    
    if not inventario:
        alerta("Inventario Vacio\n")

    else:
        print("+---------------+-------------+-----------+")
        print("| PRODUCTO      | PRECIO      | CANTIDAD  |")
        print("+---------------+-------------+-----------+")
        for p in inventario:
            print(
                f"| {p['nombre']:<13} | {f'${p['precio']:.2f}':>11} | {p['cantidad']:>9} |"
            )
        print("+---------------+-------------+-----------+\n")
    print("------Volviendo al menu-------\n".upper())

def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre en el inventario.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a buscar.

    Retorna:
        dict: Producto encontrado.
        None: Si el producto no existe.
    """
    for p in inventario:
        if p["nombre"].lower() == nombre:
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a actualizar.
        nuevo_precio (float, opcional): Nuevo precio.
        nueva_cantidad (int, opcional): Nueva cantidad.

    Retorna:
        None
    """
    producto = buscar_producto(inventario, nombre)

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    exito("Producto actualizado correctamente\n")

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Parámetros:
        inventario (list): Lista de productos.
        nombre (str): Nombre del producto a eliminar.

    Retorna:
        None
    """
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        exito("Producto eliminado correctamente\n")
    else:
        alerta("Producto no encontrado\n")

def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Parámetros:
        inventario (list): Lista de productos.

    Retorna:
        dict: Contiene:
            - unidades_totales (int)
            - valor_total (float)
            - producto_mas_caro (dict)
            - producto_mayor_stock (dict)
        None: Si el inventario está vacío.
    """

    if not inventario:
        return None

    # Suma total de productos registrados
    productos_registrados = len(inventario)
    
    # Suma total de unidades
    unidades_totales = sum(p["cantidad"] for p in inventario)

    # Valor total del inventario
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    # Producto más caro
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])

    # Producto con mayor stock
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "productos_registrados": productos_registrados,
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
    