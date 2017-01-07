"""
# Lab06Ejercicio1.py


# DESCRIPCION: 

Es un algoritmo que lee los coeficientes de un polinomio hasta que se introduzca el valor cero y los almacena en un arreglo. El programa muestra en 
pantalla el grado del polinomio y luego escribe el polinomio en notacion polinomial. El grado del polinomio no es mayor que M(Valor ingresado por el  usuario)

# Versión de: 

	Cesar Colina 13-10299

	



# Ultima modificacion: 25/10/2016





# CONSTANTES:






# VARIABLES:
M : int // mayor grado del polinomio
lista: lista // lista donde se almacena los coeficientes de las variables
x: int // entero que guarda el input
p: int // potencia
cadena: str // Cadena que guarda el output

"""


# Valores iniciales:


M = int(input("Introduzca el valor del grado mayor del primer polinomio "))
M2 = int(input("Introduzca el valor del grado mayor del segundo polinomio "))

#Precondicion:
assert(M >= 0 and M>= 2) 

#Calculos
def agregar(M):
	#Precondicion: M >=0 
	#Postcondicion: len(lista) == M - 1 
	lista = []
	for i in range(M + 1):
		x = int(input("Introduce los coeficientes de las variables "))
		if x == 0:
			break
		lista.append(x)
	return lista

print("Datos para el primer polinomio")
lista = agregar(M)

print("Datos para el segundo polinomio")
lista2 = agregar(M2)





def size(lista):
	#Precondicion: len(lista) = M - 1
	#Postcondicion: len(lista) = M - 1
	print("El grado del polinomio es", len(lista) - 1)

size(lista)
size(lista2)


def polinomio(lista):
	#Precondicion: len(lista) = M
	#Postcondicion: True
	p = len(lista) - 1
	cadena = ""
	for i in range(len(lista)):
	
		cadena += (str(lista[i]) + "x**" + str(p))
		if i < len(lista) - 1:
			cadena += "+"
		p -= 1
	return cadena

cadena = polinomio(lista)
cadena2 = polinomio(lista2)
		
operador = input("Favor introduzca el operador aritmetico: +,-,*,/")


def suma(lista,lista2,M,M2):
	resultado = []



	if M == M2:
		for i in range(len(lista)):
			resultado.append(lista[i] + lista2[i])
		return resultado

"""
NO LOGRE HACERLO (POR TIEMPO) PARA LISTAS DE DIFERENTE TAMAÑO
	if M > M2:
		diferencia = len(lista) - len(lista2)

		for i in range(diferencia):
			lista.append(0)
		return lista

		for i in range(len(lista)):
			resultado.append(lista[i] + lista2[i])
		return resultado



	if M2 > M:
		diferencia = len(lista2) - len(lista)

		for i in range(diferencia):
			lista.append(0)
		return lista

		for i in range(len(lista)):
			resultado.append(lista[i] + lista2[i])
		return resultado


"""


def resta(lista,lista2,M,M2):
	resultado = []

	if M == M2:
		for i in range(len(lista)):
			resultado.append(lista[i] - lista2[i])
		return resultado

def multiplicacion(lista,lista2,M,M2):
	resultado = []

	if M == M2:
		for i in range(len(lista)):
			resultado.append(lista[i] * lista2[i])
		return resultado

def division(lista,lista2,M,M2):
	resultado = []

	if M == M2:
		for i in range(len(lista)):
			resultado.append(lista[i] / lista2[i])
		return resultado






# Postcondicion: 

assert(True)


 # Salida:

if M == 0:
	print("P(x)= 0")
else:
	print("P1(x)= ", cadena)
	print("P2(x)= ", cadena2)

if operador == "+":
	resultado =suma(lista,lista2,M,M2)
	cadena3 = polinomio(resultado)
	print("La suma de los polinomios es el siguiente: " , cadena3)

if operador == "-":
	resultado =resta(lista,lista2,M,M2)
	cadena3 = polinomio(resultado)
	print("La suma de los polinomios es el siguiente: " , cadena3)

if operador == "*":
	resultado =multiplicacion(lista,lista2,M,M2)
	cadena3 = polinomio(resultado)
	print("La suma de los polinomios es el siguiente: " , cadena3)

if operador == "/":
	resultado =division(lista,lista2,M,M2)
	cadena3 = polinomio(resultado)
	print("La suma de los polinomios es el siguiente: " , cadena3)
