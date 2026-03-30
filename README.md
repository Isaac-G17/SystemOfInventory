# 🧾 Sistema de Inventario en Python

Aplicación de consola desarrollada en Python para gestionar un inventario de productos utilizando estructuras de datos, modularización y persistencia en archivos CSV.

---

## 🚀 Funcionalidades

### 📦 Gestión de productos (CRUD)
- Agregar productos
- Mostrar inventario
- Buscar productos
- Actualizar productos
- Eliminar productos

### 📊 Estadísticas
- Total de productos registrados
- Unidades totales
- Valor total del inventario
- Producto más caro
- Producto con mayor stock

### 💾 Persistencia de datos
- Guardar inventario en archivos CSV
- Cargar inventario desde archivos CSV
- Validación de datos al cargar

### 🎨 Interfaz de consola
- Mensajes de éxito, error y alerta con colores usando Colorama

---

## ⚙️Tecnologías
- 🐍Python 3
- CSV (manejo de archivos)
- Colorama (estilos en consola)

---

## 🗂️ Estructura del Proyecto

```bash
proyecto_inventario/
│
├── main.py
├── data/
│ └── inventario.csv
│
└── src/
  └──app.py
  ├── servicios.py
  ├── archivos.py
  └── style_msg.py
```
---
## 📦 Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu equipo:

### Clonar el repositorio

```bash
git clone https://github.com/Isaac-G17/proyecto_inventario.git
```
### Abre la carpeta del proyecto
```bash
cd SystemOfInventory
```
### Crear ambiente virtual

```bash
python3 -m venv .venv
```
### Activar ambiente virtual
#### Linux / macOs
```bash
source venv/bin/activate
```
#### Windows
```bash
venv\Scripts\activate
```
### Ejecuta el programa

```bash
python3 main.py
```

---

## ⚙️ Requisitos

Para ejecutar este proyecto necesitas:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Dependencias

Instala la librería necesaria con:

```bash
pip install colorama
```

---

## 👨‍💻 Autor

This project was created by **[Isaac Guzmán Mora](https://github.com/Isaac-G17)**.

