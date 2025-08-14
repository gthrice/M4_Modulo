class Biblioteca:
    def __init__(self):
        self.libros = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self, archivo="biblioteca.txt"):
        """Carga los libros desde un archivo de texto. Soporta libros normales y digitales."""
        import os
        if not os.path.exists(archivo):
            return
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    from libro import Libro
                    titulo, autor, anio, estado = datos
                    libro = Libro(titulo, autor, anio, estado)
                    self.libros.append(libro)
                elif len(datos) == 6 and datos[0] == "DIGITAL":
                    from libro_digital import LibroDigital
                    _, titulo, autor, anio, formato, tamano_archivo = datos
                    # Estado por defecto: disponible
                    libro = LibroDigital(titulo, autor, anio, "disponible", formato, tamano_archivo)
                    self.libros.append(libro)

    def guardar_en_archivo(self, archivo="biblioteca.txt"):
        """Guarda los libros en un archivo de texto. Soporta libros normales y digitales."""
        with open(archivo, "w", encoding="utf-8") as f:
            for libro in self.libros:
                if libro.__class__.__name__ == "LibroDigital":
                    linea = f"DIGITAL,{libro.titulo},{libro.autor},{libro.anio},{libro.formato},{libro.tamano_archivo}\n"
                else:
                    linea = f"{libro.titulo},{libro.autor},{libro.anio},{'disponible' if libro.estado else 'no disponible'}\n"
                f.write(linea)

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        print("-" * 40)
        for libro in self.libros:
            print(libro)
        print("-" * 40)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                return libro
        return None
    
    def eliminar_libro(self, titulo):
        try:
            libro = self.buscar_libro(titulo)
            if libro:
                self.libros.remove(libro)
                print(f"El libro '{titulo}' ha sido eliminado.")
            else:
                raise ValueError(f"El libro '{titulo}' no se encontró.")
        except ValueError as e:
            print(f"Error al eliminar libro: {e}")
        print("-" * 40)
    def marcar_libro_como_prestado(self, titulo):
        try:
            libro = self.buscar_libro(titulo)
            if libro:
                if not libro.estado:
                    raise ValueError(f"El libro '{titulo}' ya está prestado.")
                libro.estado = False
                print(f"El libro '{titulo}' ha sido marcado como prestado.")
            else:
                raise ValueError(f"El libro '{titulo}' no se encontró.")
        except ValueError as e:
            print(f"Error: {e}")
        print("-" * 40)
    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.estado = True
            print(f"El libro '{titulo}' ha sido devuelto y está disponible.")
        else:
            print(f"El libro '{titulo}' no se encontró.")
        print("-" * 40)
