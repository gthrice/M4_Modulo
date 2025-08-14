
from biblioteca import Biblioteca
from libro import Libro

if __name__ == "__main__":
    biblioteca = Biblioteca()
    while True:
        print("Bienvenido al sistema de gestión de biblioteca")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Buscar libro")
        print("4. Eliminar libro")
        print("5. Marcar libro como prestado")
        print("6. Devolver libro")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            titulo = input("Ingrese el título del libro: ").strip()
            autor = input("Ingrese el autor del libro: ").strip()
            while True:
                anio = input("Ingrese el año de publicación: ").strip()
                if anio.isdigit() and 0 < int(anio) <= 2100:
                    break
                print("Año inválido. Debe ser un número entre 1 y 2100.")
            while True:
                estado = input("Ingrese el estado del libro (disponible/no disponible): ").strip().lower()
                if estado in ["disponible", "no disponible"]:
                    break
                print("Estado inválido. Escriba 'disponible' o 'no disponible'.")
            libro = Libro(titulo, autor, anio, estado)
            biblioteca.agregar_libro(libro)
        elif opcion == "2":
            biblioteca.listar_libros()
        elif opcion == "3":
            titulo = input("Ingrese el título del libro a buscar: ").strip()
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                print("Libro encontrado:")
                print(libro)
            else:
                print("Libro no encontrado.")
        elif opcion == "4":
            if not biblioteca.libros:
                print("No hay libros para eliminar.")
            else:
                print("Libros disponibles:")
                for idx, libro in enumerate(biblioteca.libros):
                    print(f"{idx+1}. {libro}")
                while True:
                    try:
                        seleccion = int(input("Ingrese el número del libro a eliminar: "))
                        if 1 <= seleccion <= len(biblioteca.libros):
                            break
                        else:
                            print("Número fuera de rango.")
                    except ValueError:
                        print("Ingrese un número válido.")
                libro = biblioteca.libros[seleccion-1]
                biblioteca.eliminar_libro(libro.titulo)
        elif opcion == "5":
            if not biblioteca.libros:
                print("No hay libros para marcar como prestado.")
            else:
                print("Libros disponibles:")
                for idx, libro in enumerate(biblioteca.libros):
                    print(f"{idx+1}. {libro}")
                while True:
                    try:
                        seleccion = int(input("Ingrese el número del libro a marcar como prestado: "))
                        if 1 <= seleccion <= len(biblioteca.libros):
                            break
                        else:
                            print("Número fuera de rango.")
                    except ValueError:
                        print("Ingrese un número válido.")
                libro = biblioteca.libros[seleccion-1]
                biblioteca.marcar_libro_como_prestado(libro.titulo)
        elif opcion == "6":
            if not biblioteca.libros:
                print("No hay libros para devolver.")
            else:
                print("Libros disponibles:")
                for idx, libro in enumerate(biblioteca.libros):
                    print(f"{idx+1}. {libro}")
                while True:
                    try:
                        seleccion = int(input("Ingrese el número del libro a devolver: "))
                        if 1 <= seleccion <= len(biblioteca.libros):
                            break
                        else:
                            print("Número fuera de rango.")
                    except ValueError:
                        print("Ingrese un número válido.")
                libro = biblioteca.libros[seleccion-1]
                biblioteca.devolver_libro(libro.titulo)
        elif opcion == "7":
            print("Saliendo del sistema...")
            biblioteca.guardar_en_archivo()
            break
        else:
            print("Opción inválida. Intente nuevamente.")
