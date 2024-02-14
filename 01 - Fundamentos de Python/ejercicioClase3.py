# Consigna: ✍️
# Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.
# Para ellos debemos definir una función que reciba parámetros:
# Combinar funciones nativas y funciones definidas,
# condicionales, y bucles.
# Si el usuario ingresa el nro 1, realiza la acción A.
# Si el usuario ingresa el nro 2, realiza la acción B.

def calculadoraAritmetica(opcion):

    if (opcion==1):
        print("**** Suma de dos numeros ****")
        print("La Suma de dos numeros definidos por el usuario")
        #print("ingrese el primer numero: ")
        #num1 = input()
        num1 = int(input("ingrese el primer numero: "))
        #print("ingrese el segundo numero: ")
        #num2 = input()
        num2 = int(input("ingrese el segundo numero: "))
        suma = num1 + num2
        print("el resultado de la suma de", num1, "mas", num2, "es", suma)
        suma = num1 + num2

    elif (opcion==2):
        print("**** Resta de dos numeros ****")
        print("La Resta de dos numeros definidos por el usuario")
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))
        resta = num1 - num2
        print("el resultado de la resta de", num1, "menos", num2, "es", resta)

    else:
        print("opcion no definida")

print ("1 - Suma de dos numeros")
print ("2 - Resta de dos numeros")
opcion = int(input('ingrese una opcion: '))
calculadoraAritmetica(opcion)