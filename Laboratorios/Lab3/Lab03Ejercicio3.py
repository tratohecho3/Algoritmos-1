"""
# Lab03Ejercicio2.py


# DESCRIPCION: 

Es un algoritmo que calcula el dinero ahorrado por un trabajador

# Versión de: 

	Cesar Colina 13-10299
	David Segura 13-11341


# Ultima modificacion: 04/10/2016





# CONSTANTES:






# VARIABLES:
dia: int // Dia del mes 
mes: int // Mes cursante
i: int // Iterador
suma: int // Suma del ahorro total
inicial: int // valor del dinero obtenido por dia
"""


# Valores iniciales:
dia =int(input("Introduzca el numero de dia"))
mes = int(input("Introduzca el numero del mes"))
i = 2
suma =0
inicial = 3
I=inicial
# Precondicion: 

assert(dia > 0 and dia <= 30 and mes <= 12 and mes > 0)

#Calculos

dia = dia + (mes - 1) * 30

if mes <= 2:
	while i <= dia:

		suma = suma + inicial* 2
		inicial = inicial * 2
		i = i + 1

	suma = suma + 3

elif mes > 2:
	dia = dia - 1
	while i <= dia:

		suma = suma + inicial* 2
		inicial = inicial * 2
		i = i + 1

	suma = suma + 3






# Postcondicion: 
 
assert(suma > 0)

 # Salida:
print(suma)
