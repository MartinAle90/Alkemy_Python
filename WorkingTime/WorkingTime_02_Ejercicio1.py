"""
1. Crear una clase llamada Bicicleta y luego aplica los siguientes
accionables:
↪ Agregar al menos 3 atributos
↪ Agregar al menos 3 métodos
↪ Agregar el método constructor de la clase.
● Guardarlo en un archivo llamado ejercicio1.py
"""
# Crear una clase llamada Bicicleta
class Bicicleta:
    # Agregar al menos 3 atributos
    def __init__(self, marca, rodado, precio, velocidad):
        self.marca = marca
        self.rodado = rodado
        self.precio = precio
        self.velocidad = velocidad
        
    # Agregar al menos 3 métodos
    def frenar(self):
        # 7 6 5 4 3 2 1 0 (frenó)
        while (self.velocidad >0 ):
            self.velocidad -=1
            print(f' Velocidad Actual: {self.velocidad}')
        print("Ya frenaste")
            
        
    def andar(self):
        # 1 2 3 4 5 6 7 (frenó)
        while (self.velocidad <7 ):
            self.velocidad +=1
            print(f' Velocidad Actual: {self.velocidad}')
        print("Ya llegamos a la velocidad deseada")
        
    def mostrarBici(self):
        print(f'Marca: {self.marca}')
        print(f'Rodado: {self.rodado}')
        print(f'Precio: {self.precio}')
        print(f'Velocidad: {self.velocidad}')

miBici = Bicicleta("Venzo", 29, 150000, 12)

miBici.frenar()
miBici.andar()
miBici.mostrarBici()


