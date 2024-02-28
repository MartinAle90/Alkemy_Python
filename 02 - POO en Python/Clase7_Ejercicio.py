"""
Una fabrica de instrumentos musicales posee una lista con todas sus sucursales.
Cada sucursal tiene su nombre y una lista con todos los instrumentos a la venta.
De cada uno de ellos se sabe su Id alfanumerico, su precio y su tipo (Persusion, Viento y Cuerda)

Puntos a desarrollar
1) Desarrollar el diagrama de clases UML que modele lo enunciado y donde consten las clases con sus
atributos, metodos y relaciones (los constructores pueden omitirse).

2) Crear un proyecto en Python que resuelva:

    A) La explotación del método listarInstrumentos que muestre en la consola todos los
    datos de cada uno de los instrumentos.
    
    B) La explotación del método instrumentosPorTipo que devuelva una lista de
    instrumentos cuyo tipo coincida con el recibido por parámetro.
    
    C) La explotación del método borrarInstrumento que reciba un ID y elimine el
    instrumento asociado a tal ID de la sucursal donde se encuentre.
    
    D) La explotación del método porcInstrumentosPorTipo que reciba el nombre de una
    sucursal y retorne los porcentajes de instrumentos por tipo que hay para tal sucursal.
"""

from enum import Enum


class TipoInstrumento(Enum):
    Percusión = "Percusión"
    Viento = "Viento"
    Cuerda = "Cuerda"
    
class Fabrica:
    def __init__(self):
        self.listaSucursales = []

    def agregarSucursal(self, sucursal):
        self.listaSucursales.append(sucursal)

    def listarInstrumentos(self):
        for sucursal in self.listaSucursales:
            for instrumentos in sucursal.mostrarInstrumento():
                print(instrumentos.id, instrumentos.precio, instrumentos.tipoInstrumento)

    def instrumentosPorTipo(self, tipo):
        for sucursal in self.listaSucursales:
            for instrumentos in sucursal.mostrarInstrumento():
                if(instrumentos.tipo == tipo):
                    print(instrumentos.id, instrumentos.precio, instrumentos.tipoInstrumento)

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaIntrumentos = []

    def listarInstrumentos(self):
        for instrumento in self.instrumentos:
            print(instrumento)

    def agregarInstrumento(self, instrumento):
        self.listaIntrumentos.append(instrumento)

    def mostrarInstrumento(self):
        return self.listaIntrumentos


class Instrumento:
    def __init__(self, id, precio, tipoInstrumento):
        self.id = id
        self.precio = precio
        self.tipoInstrumento = tipoInstrumento


fabrica = Fabrica()

suc01 = Sucursal("Sucursal 1")
suc02 = Sucursal("Sucursal 2")


instr01 = Instrumento("1","1700", TipoInstrumento.Cuerda)
instr02 = Instrumento("2","2700", TipoInstrumento.Percusión)

fabrica.agregarSucursal(suc01)
fabrica.agregarSucursal(suc02)

suc01.agregarInstrumento(instr01)
suc01.agregarInstrumento(instr02)

fabrica.listarInstrumentos()


