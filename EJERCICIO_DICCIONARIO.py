import json
import os

# Menú disponible (tuplas)
menu = [
    ("Café", 2500),
    ("Té", 2000),
    ("Chocolate", 3000),
    ("Pan de queso", 1800),
    ("Croissant", 2200)
]

# Lista de pedidos
pedidos = []

# === Guardar pedidos en JSON ===
def guardar_datos():
    with open("C:/Users/eduar/OneDrive/Documents/Programacion de Objetos/Pre_parcial/pedidos.json", "w", encoding="utf-8") as archivo:
        json.dump(pedidos, archivo, indent=4, ensure_ascii=False)
        
# === Cargar pedidos desde JSON ===
def cargar_datos():
    if os.path.exists("C:/Users/eduar/OneDrive/Documents/Programacion de Objetos/Pre_parcial/pedidos.json"):
        with open("C:/Users/eduar/OneDrive/Documents/Programacion de Objetos/Pre_parcial/pedidos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            # Reconstruir tuplas
            for pedido in datos:
                pedido["productos"] = [tuple(prod) for prod in pedido["productos"]]
                pedidos.append(pedido)

def mostrar_menu():
    print("\n=== MENÚ DE LA CAFETERÍA ===")
    for i, (nombre, precio) in enumerate(menu):
        print(f"{i}. {nombre} - ${precio}")

def hacer_pedido():
    nombre_cliente = input("Ingrese el nombre del cliente: ")

    mostrar_menu()
    seleccion = input("Escriba los números de los productos separados por comas (ej: 0,2,3): ")
    indices = [int(i.strip()) for i in seleccion.split(",") if i.strip().isdigit()]

    productos_seleccionados = [menu[i] for i in indices if 0 <= i < len(menu)]
    total = sum(p[1] for p in productos_seleccionados)

    pedido = {
        "cliente": nombre_cliente,
        "productos": productos_seleccionados,
        "total": total
    }

    pedidos.append(pedido)
    guardar_datos()
    print(f"✅ Pedido registrado para {nombre_cliente} - Total: ${total}")

def mostrar_pedidos():
    print("\n=== TODOS LOS PEDIDOS ===")
    if not pedidos:
        print("No hay pedidos aún.")
        return

    for i, pedido in enumerate(pedidos, start=1):
        print(f"\nPedido {i} - Cliente: {pedido['cliente']}")
        for prod in pedido["productos"]:
            print(f"  - {prod[0]}: ${prod[1]}")
        print(f"Total: ${pedido['total']}")

# === Iniciar ===
cargar_datos()

while True:
    print("\n=== CAFETERÍA ===")
    print("1. Hacer un pedido")
    print("2. Ver pedidos")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        hacer_pedido()
    elif opcion == "2":
        mostrar_pedidos()
    elif opcion == "3":
        print("👋 Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("❌ Opción inválida. Intente de nuevo.")
