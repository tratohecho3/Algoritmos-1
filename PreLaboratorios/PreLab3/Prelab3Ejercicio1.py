"""

# Prelab3Ejercicio1.py


# DESCRIPCION: algoritmo que calcula la suma de 
				los factoriales desde 0 hasta n


# Versión de: 

Colina Cesar 13-10299
Chaparro Orlando 12-11499 



# Ultima modificacion: 02/10/2016


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
N = int(input("Introduzca el numero hasta el cual quiere hacer la suma de los factoriales"))
# Precondicion: 

assert(N >= 0)

# Calculos

assert(N >= 0 and k >= 0 and k <= N)

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

# Postcondicion: 
 
assert(suma == sum(prod(range(1,i+1)) for i in range(0,N+1)))

 # Salida:
print(suma)

