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
        print(f'------------------------------')
        print(f'Titulo: {self.titulo}')
        print(f'Precio: $ {self.precio}')
        print(f'Autor: {self.autor}')
        print(f'Editorial: {self.editorial}')
        print(f'------------------------------')

        
class Pelicula(Producto):
    def __init__(self, titulo, precio,  actorPrincipal, productora):
        super().__init__(titulo, precio)
        self.actorPrincipal = actorPrincipal
        self.productora = productora
        
    def mostrarProducto(self):
        print(f'------------------------------')
        print(f'Titulo: {self.titulo}')
        print(f'Precio: $ {self.precio}')
        print(f'Actor Principal: {self.actorPrincipal}')
        print(f'Productora: {self.productora}')
        print(f'------------------------------')

class Disco(Producto):
    def __init__(self, titulo, precio,  artistaBanda, discografica):
        super().__init__(titulo, precio)
        self.artistaBanda = artistaBanda
        self.discografica = discografica
        
    def mostrarProducto(self):
        print(f'------------------------------')
        print(f'Titulo: {self.titulo}')
        print(f'Precio: $ {self.precio}')
        print(f'Artista/Banda: {self.artistaBanda}')
        print(f'Discografia: {self.discografica}')
        print(f'------------------------------')
        
        
libro1 = Libro("Titulo 01", "100", "Juan Perez", "Luciernaga")
libro1.mostrarProducto()
libro2 = Libro("Titulo 02", "200", "Pablo Gonzalez", "Rayada")
libro2.mostrarProducto()
libro3 = Libro("Titulo 03", "500", "Ramiro Angel", "Periplo")
libro3.mostrarProducto()

pelicula1 = Pelicula("Titulo 01", "1500", "Star Wars", "Lucas Films")
pelicula1.mostrarProducto()
pelicula2 = Pelicula("Titulo 02", "3000", "Spiderman", "Sony")
pelicula2.mostrarProducto()
pelicula3 = Pelicula("Titulo 03", "4500", "Jhon Wick", "Universal")
pelicula3.mostrarProducto()

disco1 = Disco("Titulo 01", "250", "Calamaro", "Panchitos")
disco1.mostrarProducto()
disco2 = Disco("Titulo 02", "350", "Dividios", "Nostradamus")
disco2.mostrarProducto()
disco3 = Disco("Titulo 03", "650", "Attaque 77", "Rock and Pop")
disco3.mostrarProducto()