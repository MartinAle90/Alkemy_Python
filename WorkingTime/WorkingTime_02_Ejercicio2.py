"""
2. Crear una clase llamada Animal, otra llamada Perro y otra llamada
Águila.
↪ La clase Animal tiene:
○ atributo cantidad_patas: numérico
○ atributo tipo: vertebrado/invertebrado
○ método comer(): retorna un string “estoy comiendo”
↪ La clase Perro hereda de Animal y agrega:
○ atributo nombre: texto
○ atributo raza: texto
○ método correr(): retorna un string “estoy corriendo”
↪ La clase Aguila hereda de Animal y agrega:
○ método volar(): retorna un string “estoy volando”
● Guardarlo en un archivo llamado ejercicio2.py
"""

class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo    #ENUMS - Enumeraciones
        
    def comer():
        return "estoy comiendo"
    
    def mostrar(self):
        print(f"{self.tipo} de {self.cantidad_patas} patas")

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def correr():
        return "estoy corriendo"
    
class Aguila(Animal):   
    def __init__(self, cantidad_patas, tipo, largoAlas):
        super().__init__(cantidad_patas, tipo)
        self.largoAlas = largoAlas
        
    def volar():
        return "estoy volando"
    
animal0 = Animal(4, "Felino")
animal0.mostrar()

miPerro = Perro("Jamoncito", "Beagle")

aguila0 = Aguila(2, "Volador", 10)
aguila0.mostrar()
