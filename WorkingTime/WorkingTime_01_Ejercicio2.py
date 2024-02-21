import random


#Crear una lista con 5 elementos y luego aplica los siguientes accionables:
list = ["Perro", "Gato", "Canario", "Iguana", "Raton"]
print(list)

#↪ Imprimir el último elemento
print(list[-1])

#↪ Modificar el valor del tercer elemento
list[2]="Guacamallo"
print(list)

#↪ Agregar dos elementos
list.append("Tiburon")
print(list)

#↪ Eliminar algún elemento
b=len(list)-1
randomNumber = random.randint(0, b)
print(randomNumber)
list.remove(list[randomNumber])
print(list)


#● Guardar en un archivo llamado ejercicio2.py
