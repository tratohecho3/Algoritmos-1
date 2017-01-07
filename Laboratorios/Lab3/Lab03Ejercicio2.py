"""
# Lab03Ejercicio2.py


# DESCRIPCION: 

Es un algoritmo que calcula la raiz digital de un numero n

# Versión de: 

	Cesar Colina 13-10299
	David Segura 13-11341


# Ultima modificacion: 04/10/2016





# CONSTANTES:






# VARIABLES:
n : int // numero al cual se le calculara la raiz digital
suma: int // valor que calcula la suma digital de un numero
raiz: int // valor final de la raiz digital de un numero
N: int // valor inicial de n

"""


# Valores iniciales:
n = int(input("Introduzca un numero entero: "))
N = n
suma = 0
raiz = 0

# Precondicion: 

assert(n < 10000000000)

#Calculos


while n > 0:
	suma = suma +  n % 10
	n = n // 10
	
while suma > 0:
	raiz = raiz + suma % 10 
	suma= suma // 10






# Postcondicion: 
 
assert(raiz >= 0 and raiz < 10)

 # Salida:

print("La raiz digital de ", N," es: ",raiz)