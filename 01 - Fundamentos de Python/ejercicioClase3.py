# Consigna: ✍️
# Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.
# Para ellos debemos definir una función que reciba parámetros:
# Combinar funciones nativas y funciones definidas,
# condicionales, y bucles.
# Si el usuario ingresa el nro 1, realiza la acción A.
# Si el usuario ingresa el nro 2, realiza la acción B.


print ("1 - Accion A")
print ("2 - Accion B")
opcion = input('ingrese un numero: ')


def calculadoraAritmetica(opcion):

    if (1):
        print("Accion A")
        print("suma de 5 mas 1 hasta llegar a 10")
        suma = 5
        while (suma<10):
            suma +=1

    elif (2):
        print("Accion B")
        print("resta de 5 menos 1 hasta llevar a cero")
        resta = 6
        while (resta>0):
            resta -=1

    else:
        print("opcion no definida")