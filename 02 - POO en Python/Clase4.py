# Sintaxis para crear un objeto
class Auto:

    # Propiedades/Atributos de un objeto
    def __init__(self, marca, modelo, color, tipoCombustible, cantidadPuertas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipoCombustible = tipoCombustible
        self.cantidadPuertas = cantidadPuertas

    # Comportamiento/s del objeto. Acciones que puede realizar el objeto
        
    #
    def tocarBocina(self):
        return "pi pi"

    # Dentro tenemos getter and setter
    # set - setear - establecer un valor
    # get - obtener un valor
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo
       
    def getColor(self):
        return self.color
    
    def getTipoCombustible(self):
        return self.tipoCombustible
    
    def getCantidadPuertas(self):
        return self.cantidadPuertas
    
    def mostrarAuto(self):
        print(f'Marca: {self.getMarca()}')
        print(f'Modelo: {self.getModelo()}')
        print(f'Color: {self.getColor()}')
        print(f'TipoCombustible: {self.getTipoCombustible()}')
        print(f'CantidadPuertas: {self.getCantidadPuertas()}')


# setters
inputMarca = input("Ingresar marca:")
inputModelo = input("Ingresar modelo:")
inputColor = input("Ingresar color:")
inputTpoCombustible = input("Ingresar tipo de combustible:")
inputCantidadPuertas = input("Ingresar cantidad de puertas:")

# Como crear un objeto y asignarles valores
auto1 = Auto(inputMarca, inputModelo, inputColor, inputTpoCombustible, inputCantidadPuertas)
"""
O tambien se puede hardcodear:
auto1 = Auto("Toyota", "Prius", "Rojo", "Hibrido", "4")
"""
auto1.mostrarAuto()
