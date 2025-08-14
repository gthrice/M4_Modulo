class Libro:
    def __init__(self, titulo, autor, anio, estado):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.estado = True if estado.lower() == 'disponible' else False 

    def __str__(self): # Método para mostrar información del libro
        return f"{self.titulo}. Escrito por -{self.autor}- en {self.anio}. Estado: {'Disponible' if self.estado else 'No disponible'}."

    # Métodos getters y setters
    # Los métodos getters permiten obtener (leer) el valor de los atributos del objeto.
    # Los métodos setters permiten modificar (escribir) el valor de los atributos del objeto.
    # Esto ayuda a proteger los datos internos y controlar cómo se accede o modifica cada atributo.

    # Getter: devuelve el valor del atributo 'titulo'
    def get_titulo(self):
        return self.titulo

    # Getter: devuelve el valor del atributo 'autor'
    def get_autor(self):
        return self.autor

    # Getter: devuelve el valor del atributo 'anio'
    def get_anio(self):
        return self.anio

    # Getter: devuelve el valor del atributo 'estado'
    def get_estado(self):
        return self.estado

    # Setter: permite modificar el valor del atributo 'titulo'
    def set_titulo(self, titulo):
        self.titulo = titulo

    # Setter: permite modificar el valor del atributo 'autor'
    def set_autor(self, autor):
        self.autor = autor

    # Setter: permite modificar el valor del atributo 'anio'
    def set_anio(self, anio):
        self.anio = anio

    # Setter: permite modificar el valor del atributo 'estado'
    def set_estado(self, estado):
        self.estado = True if estado.lower() == 'disponible' else False
