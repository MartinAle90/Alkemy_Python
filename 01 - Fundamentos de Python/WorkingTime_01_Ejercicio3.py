#Crea una función llamada verificar_calificacion que reciba tres
#parámetros: nota1, nota2 y nota3
#↪ Dentro de la función calcular el promedio de notas
#↪ Si el promedio es mayor o igual a 6, entonces la función debe
#retornar un mensaje “Aprobado”, en caso contrario
#“Reprobado”
#● Guardar en un archivo llamado ejercicio3.py

import random


def verificar_calificacion (nota1, nota2, nota3):
    """ Funcion que retorna el promedio de tres notas. """
    promedio=((nota1+nota2+nota3)/3)

    """ Vamos a verificar si el promedio de las notas es mayor o igual a 6. """
    if (promedio>=6):
        print ("Aprobado")
    else:
        print ("Reprobado")

nota1 = random.randint(1, 10)
nota2 = random.randint(1, 10)
nota3 = random.randint(1, 10)

print("Nota 1 =", nota1)
print('Nota 2 =', nota2)
print('Nota 3 =', nota3)

resultdado = verificar_calificacion (nota1, nota2, nota3)

#print(resultdado)

