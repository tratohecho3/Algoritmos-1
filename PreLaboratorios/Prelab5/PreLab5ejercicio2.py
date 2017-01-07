import sys

"""

# Prelab5Ejercicio2.py


# DESCRIPCION: algoritmo que calcula la suma de 
				los factoriales desde 0 hasta n
				usando la funcion try/except


# Versión de: 

Colina Cesar 13-10299
Chaparro Orlando 12-11499 



# Ultima modificacion: 17/10/2016


# CONSTANTES:





# VARIABLES:
N: int // limite superior hasta donde se cualculara 
			la suma de los factoriales
p: int // elemento neutro de la multiplicacion y posteriormente el resultado de la productoria
suma: int // resultado de la suma total de los factoriales
fact : int // resultado del total de los factoriales
k : int // es el numero que representa por cual iteracion vamos

"""

# Valores iniciales:

suma,fact,k = 0,1,0

# Precondicion: 

while True:
	try:
		N = int(input("Introduzca el numero hasta el cual quiere hacer la suma de los factoriales: "))
		assert(N >= 0)
		break
	except:
		print("Ha introducido un valor incorrecto")
		print("Debe introducir al sistema un valor entero mayor a cero (0)")

# Calculos

while k <= N:
	if k > 0:
		fact = fact * k
	else:
		pass
	suma = suma + fact
	k = k +1


def prod( iterable ): 
	p= 1 
	for n in iterable: 
		p *= n 
	return p

# Verificacion de la Postcondicion: 

try:
	assert(suma == sum(prod(range(1,i+1)) for i in range(0,N+1)))

except:
	print("Hubo un error en los calculos")
	print("El resultado de la operacion no ha podido ser realizada")
	print("Intente de nuevo")
	sys.exit()
	
 # Salida:
print(suma)

