"""
EJERCICIO

Crear una clase producto que tenga 3 hijos

Esta clase producto va a tener 3 atributos
- 3 Atributos
- Metodo Mostrar() producto que dependiento el producto
va a mostrar diferentes caracteristicas

Libro, Pelicula, Disco - Cdad una va a tener 2 atributos

Crear 3 instancias por clase hijo
Es decir, 3 discos, 3 libros, 3 peliculas

Titulo
Autor
Editorial

"""

class Producto:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio
        
    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Precio: $ {self.precio}')
     
        

class Libro(Producto):
    def __init__(self, titulo, precio,  autor, editorial):
        super().__init__(titulo, precio)
        self.autor = autor
        self.editorial = editorial

    def mostrarProducto(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Precio: {self.precio}')
        print(f'Tipo_tapa: {self.editorial}')
        
class Pelicula(Producto):
    def __init__(self, titulo, precio,  actorPrincipal, productora):
        super().__init__(titulo, precio)
        self.actorPrincipal = actorPrincipal
        self.productora = productora

class Disco(Producto):
    def __init__(self, titulo, precio,  artistaBanda, discografica):
        super().__init__(titulo, precio)
        self.artistaBanda = artistaBanda
        self.editodiscograficarial = discografica
        
        
libro1 = Libro("Titulo 01", "100", "Juan Perez", "Luciernaga")
libro1.mostrarProducto()
libro2 = Libro("Titulo 02", "200", "Pablo Gonzalez", "Rayada")
libro3 = Libro("Titulo 03", "500", "Ramiro Angel", "Periplo")



pelicula1 = Pelicula("Titulo 01", "1500", "Juan Perez", "Luciernaga")
pelicula2 = Pelicula("Titulo 02", "3000", "Juan Perez", "Luciernaga")
pelicula3 = Pelicula("Titulo 03", "4500", "Juan Perez", "Luciernaga")

disco1 = Disco("Titulo 01", "250", "Juan Perez", "Luciernaga")
disco2 = Disco("Titulo 02", "350", "Juan Perez", "Luciernaga")
disco3 = Disco("Titulo 03", "650", "Juan Perez", "Luciernaga")