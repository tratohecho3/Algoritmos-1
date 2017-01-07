import sys
"""
# Lab05Ejercicio1.py


# DESCRIPCION: 

Es un algoritmo que le dice al usuario si un numero ingresado por el mismo es perfecto, deficiente o abundante

# Versión de: 

	Cesar Colina 13-10299
	


# Ultima modificacion: 18/10/2016





# CONSTANTES:






# VARIABLES:
suma: int // variable donde se almacena la suma de todos los divisores propios del numero dado
numero: int // numero dado por el usuario al cual queremos saber si es perfecto, deficiente o abundante


"""


# Valores iniciales:


suma = 0




# Precondicion: 

while True:
	try:
		numero = int(input("Introduce un numero natural"))
		assert(numero > 0)
		break
	except:
		print("Ha introducido un valor incorrecto")
		print("Debe introducir al sistema un numero natural mayor a cero (0)")


#Calculos

for i in range(1,numero):
	if numero % i == 0:
		suma = suma + i






# Postcondicion: 

try:
	assert(suma == sum(x for x in range(1,numero) if numero % x ==0))

except:
	print("Hubo un error en los calculos")
	print("El resultado de la operacion no ha podido ser realizada")
	print("Intente de nuevo")
	sys.exit()

 # Salida:
if suma == numero:
	print("El numero ", numero, "es perfecto")
elif suma < numero:
	print("El numero ", numero, "es deficiente")
elif suma > numero:
	print("El numero ", numero, "es abundante")
