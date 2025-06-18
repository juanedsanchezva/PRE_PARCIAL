import json
import os

class Libro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def __str__(self):
        return f"{self.titulo} - {self.autor} [{self.categoria}]"

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria
        }

class Usuario:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"{self.nombre} (ID: {self.codigo})"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "codigo": self.codigo
        }
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.cargar_datos() 

        
    def registrar_libro(self, titulo, autor, categoria):
        if categoria not in ["Ciencia", "Literatura", "Ingeniería"]:
            print("❌ Categoría no válida. Debe ser Ciencia, Literatura o Ingeniería.")
            return
        libro = Libro(titulo, autor, categoria)
        self.libros.append(libro)
        self.guardar_datos()
        print("✅ Libro registrado exitosamente.")

    def registrar_usuario(self, nombre, codigo):
        usuario = Usuario(nombre, codigo)
        self.usuarios.append(usuario)
        self.guardar_datos()
        print("✅ Usuario registrado exitosamente.")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros registrados.")
        for libro in self.libros:
            print(libro)

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        for usuario in self.usuarios:
            print(usuario)

    def guardar_datos(self):
        datos = {
            "libros": [libro.to_dict() for libro in self.libros],
            "usuarios": [usuario.to_dict() for usuario in self.usuarios]
        }
        with open("C:/Users/eduar/OneDrive/Documents/Programacion de Objetos/Pre_parcial/biblioteca.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_datos(self):
         if os.path.exists("C:/Users/eduar/OneDrive/Documents/Programacion de Objetos/Pre_parcial/biblioteca.json"):
            with open("C:/Users/eduar/OneDrive/Documents/Programacion de Objetos/Pre_parcial/biblioteca.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                self.libros = [Libro(**l) for l in datos.get("libros", [])]
                self.usuarios = [Usuario(**u) for u in datos.get("usuarios", [])]


def mostrar_menu():
    print("\n=== MENÚ BIBLIOTECA ===")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Mostrar libros")
    print("4. Mostrar usuarios")
    print("5. Salir")


biblioteca = Biblioteca()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría (Ciencia/Literatura/Ingeniería): ")
        biblioteca.registrar_libro(titulo, autor, categoria)

    elif opcion == "2":
        nombre = input("Nombre del usuario: ")
        codigo = input("Código del usuario: ")
        biblioteca.registrar_usuario(nombre, codigo)

    elif opcion == "3":
        biblioteca.mostrar_libros()

    elif opcion == "4":
        biblioteca.mostrar_usuarios()

    elif opcion == "5":
        print("📚 Saliendo del sistema. Hasta luego.")
        break

    else:
        print("❗ Opción inválida. Intente nuevamente.")
