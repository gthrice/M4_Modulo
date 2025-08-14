# Sistema de Gestión de Biblioteca

Este proyecto es una aplicación de consola en Python para gestionar una biblioteca de libros físicos y digitales. Permite agregar, listar, buscar, eliminar, prestar y devolver libros, almacenando la información en un archivo de texto.

## Características principales
- **Agregar libros físicos y digitales**
- **Listar todos los libros**
- **Buscar libros por título**
- **Eliminar libros**
- **Marcar libros como prestados o devueltos**
- **Persistencia de datos en `biblioteca.txt`**
- **Manejo de excepciones para operaciones inválidas**

## Estructura de archivos
- `main.py`: Menú principal y lógica de interacción con el usuario.
- `biblioteca.py`: Clase `Biblioteca` para gestionar la colección de libros y la persistencia.
- `libro.py`: Clase `Libro` (libro físico) con getters y setters.
- `libro_digital.py`: Clase `LibroDigital` (hereda de `Libro`), añade formato y tamaño de archivo.
- `biblioteca.txt`: Archivo donde se guardan los datos de los libros.

## Formato de almacenamiento
- Libros físicos: `titulo,autor,anio,estado`
- Libros digitales: `DIGITAL,titulo,autor,anio,formato,tamano_archivo`

## Uso
1. Ejecuta `main.py`.
2. Usa el menú para gestionar los libros.
3. Los cambios se guardan automáticamente al salir.

## Requisitos
- Python 3.x

## Notas
- El sistema maneja errores como intentar eliminar o prestar libros inexistentes o ya prestados.
- Puedes modificar y ampliar las clases para agregar más funcionalidades.

---