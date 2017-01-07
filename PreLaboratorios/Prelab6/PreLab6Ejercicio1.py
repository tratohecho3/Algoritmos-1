import sys
"""
# PreLab6Ejercicio1.py


# DESCRIPCION: 

Es un algoritmo que le dice al usuario si un numero ingresado por el mismo es perfecto, deficiente o abundante

# Versión de: 

	Cesar Colina 13-10299
	Orlando Chaparro 12-11499
	


# Ultima modificacion: 24/10/2016





# CONSTANTES:






# VARIABLES:
suma: int // variable donde se almacena la suma de todos los divisores propios del numero dado
numero: int // numero dado por el usuario al cual queremos saber si es perfecto, deficiente o abundante


"""


# Valores iniciales:







# Precondicion: 

def validar(numero):
	
	#Precondicion: True
	#Postcondicion: numero > 0
	
	if numero > 0:
		pass
	elif numero <= 0:
		while numero < 0:
	 		numero = int(input("Introduce un numero natural "))


	return numero

numero = validar(int(input("Introduce un numero natural ")))




	



#Calculos

def calcular(numero):
	#Precondicion: numero > 0
	#Postcondicion: suma == sum(x for x in range(1,numero) if numero % x ==0
	suma = 0
	for i in range(1,numero):
		if numero % i == 0:
			suma = suma + i
	return suma

suma = calcular(numero)






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
