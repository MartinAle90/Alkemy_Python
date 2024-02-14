# band = True

# while (band):
#     print("comida")
#     band=False



#LISTAS
"""edades = [19, 54, 16, 54, 23, 21, 51, 12, 33]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

for dia in dias:
    print(f'#: {dias.index(dia)} {dia}')

dias.extend(edades)"""

#BUCLES

"""print(edades)
while (edades[3]<18):
    print("Tenes menos de 18")
    
print("Fin")

for edad in edades:
    print(f'Print aparte: {edades.index(edad)} {edad}')"""


#TUPLAS
"""miTupla=("Lunes",
          "Martes",
          "Miercoles",
          "Jueves",
          "Viernes",
          "Sabado",
          "Sabado",
          "Sabado",
          "Sabado",
          "Sabado",
          "Domingo")"""

# print(miTupla.count("Sabado"))

#DICCIONARIO
"""persona01 = {"nombre": "Juan", "apellido": "Perez", "edad": 34}
persona02 = {"nombre": "Carlos", "apellido": "Gomez", "edad": 40}
persona03 = {"nombre": "Carla", "apellido": "Gimenez", "edad": 24}

print(persona02["nombre"])

print(persona02.keys())
print(persona02.values())
print(persona02.items())

print(persona01.get("nombre"))"""

#FUNCIONES del USUARIO

# DECLARAR
# DEFINIR
# INVOCAR / LLAMAR

# ALGORITMO.
    # ENTRADA - el precio sin impuestos
    # PROCESAMIENTO -  multiplicar por 1.21
    # RETORNO - el precio con IVA

precio = 100
def sumarIva(precioSinIva): #Tomo como entrada el precio sin iva
    precioConIva = precioSinIva * 1.21 # multiplico el precio sin iva por el iva
    return precioConIva # retorno esa variable

print(sumarIva(1650))
print(sumarIva(4700))
print(sumarIva(9300))









