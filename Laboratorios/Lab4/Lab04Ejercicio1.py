"""
# Lab04Ejercicio1.py


# DESCRIPCION: 

Es un algoritmo que lee los coeficientes de un polinomio hasta que se introduzca el valor cero y los almacena en un arreglo. El programa muestra en 
pantalla el grado del polinomio y luego escribe el polinomio en notacion polinomial. El grado del polinomio no es mayor que M(Valor ingresado por el  usuario)

# Versión de: 

	Cesar Colina 13-10299
	Gustavo Castellanos 14-10192



# Ultima modificacion: 11/10/2016





# CONSTANTES:






# VARIABLES:
M : int // mayor grado del polinomio
lista: lista // lista donde se almacena los coeficientes de las variables
x: int // entero que guarda el input
p: int // potencia
cadena: str // Cadena que guarda el output

"""


# Valores iniciales:
lista = []
M = int(input("Introduzca el valor del grado mayor del polinomio"))

#Precondicion:
assert(M >= 0) 

#Calculos

for i in range(M):
	x = int(input("Introduce los coeficientes de las variables "))
	if x == 0:
		break
	lista.append(x)

p = len(lista) - 1
cadena = ""
for i in range(len(lista)):
	
	cadena += (str(lista[i]) + "x**" + str(p))
	if i < len(lista) - 1:
		cadena += "+"
	p -= 1


		





# Postcondicion: 
 
assert(True)
 # Salida:

print("P(x)= ", cadena)
