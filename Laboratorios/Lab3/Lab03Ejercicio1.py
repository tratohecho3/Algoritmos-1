"""
# Lab03Ejercicio1.py


# DESCRIPCION: 

Es un algoritmo que dado un numero n, te calcula si es un numero perfecto

# Versión de: 

	Cesar Colina 13-10299
	David Segura 13-11341


# Ultima modificacion: 04/10/2016





# CONSTANTES:






# VARIABLES:

n : int // Valor que deseamos saber si es perfecto
i : int // Numero que iteramos entre 1 y n-1
suma: int // Valor de la suma total de los divisores propios de n
perfecto: bool // Booleano que nos dice si n es perfecto

"""


# Valores iniciales:

n = int(input("Introduzca un numero entero positivo: "))
i = 1
suma = 0
perfecto = True

# Precondicion: 

assert(n > 0)

#Calculos

while i >= 1 and i < n:

	if n % i == 0:
		suma = suma + i
	else:
		pass

	i = i + 1

if n == suma:
	pass
else:
	perfecto = False





# Postcondicion: 
 
assert(suma == sum( i for i in range(1,n) if n % i== 0))

 # Salida:
if perfecto == True:
	print("Es perfecto")
else:
	print("No es perfecto") 
