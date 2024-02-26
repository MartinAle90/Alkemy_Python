"""
Enunciado
Cierta empresa requiere una aplicación informática para administrar los datos de su personal, del cual se conoce:

- número de DNI
- nombre
- apellido 
- año de ingreso.

Existen dos categorías de empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo, 
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes captados no llega a cubrir el salario mínimo, cobrará el salario mínimo. 

-----

Los empleados con salario fijo tienen un sueldo básico y un porcentaje adicional en función del número de años que llevan la empresa: 
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con mayor cantidad de clientes captados (se supone único).

creen 10 empleados

"""

class Empleado:
    def __init__(self, dni, nombre, apellido, año_ingreso):
        #Constructor de la clase Empleado.
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.año_ingreso = año_ingreso
        
    def mostrar_salario(self):
        #Muestra por consola el salario del empleado.
        pass

class EmpleadoFijo:
    def __init__(self, dni, nombre, apellido, año_ingreso, sueldo_basico):
        #Constructor de la clase EmpleadoFijo.
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.año_ingreso = año_ingreso
        self.sueldo_basico = sueldo_basico

    def calcular_salario(self):
        #Calcula el salario del empleado fijo.
        año_actual=2024
        if((año_actual-self.año_ingreso) < 2):
            salarioFinal = self.sueldo_basico
            
        elif(((año_actual-self.año_ingreso) >= 2) & (año_actual-self.año_ingreso) <= 5):
            salarioFinal = self.sueldo_basico + (self.sueldo_basico)*0.05
            
        elif((año_actual-self.año_ingreso) > 5):
            salarioFinal = self.sueldo_basico + (self.sueldo_basico)*0.1
            
        print(salarioFinal)
        return salarioFinal
        
    def mostrar_salario(self):
        #Muestra por consola el salario del empleado fijo.
        salarioFinal = self.calcular_salario
        print(salarioFinal)
        pass

class EmpleadoComision:

    def __init__(self, dni, nombre, apellido, año_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        #Constructor de la clase EmpleadoComision.
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.año_ingreso = año_ingreso
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente
        
    def calcular_salario(self):
        #Calcula el salario del empleado a comisión.
        pass
    def mostrar_salario(self):
        #Muestra por consola el salario del empleado a comisión.
        pass

empleadoFijo01 = EmpleadoFijo ("123456789", "Juan", "Perez", 2000, 1000)
empleadoFijo01.calcular_salario()
