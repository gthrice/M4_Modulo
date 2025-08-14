from libro import Libro

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, estado, formato, tamano_archivo):
        super().__init__(titulo, autor, anio, estado)
        self.formato = formato
        self.tamano_archivo = tamano_archivo

    def __str__(self):
        return super().__str__() + f" Formato: {self.formato}, Tamaño: {self.tamano_archivo} MB."
