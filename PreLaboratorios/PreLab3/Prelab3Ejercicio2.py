"""

# Prelab3Ejercicio2.py


# DESCRIPCION: algoritmo que calcula la suma de los digitos de un numero
entero N de 10 digitos maximo

# Versión de: 

Colina Cesar 13-10299
Chaparro Orlando 12-11499 



# Ultima modificacion: 02/10/2016


# CONSTANTES:





# VARIABLES:
N : int // este es el numero en el que haremos las operaciones
suma : int // este es el resultado total de la suma
cociente: int // este es el cociente que nos queda despues de cada iteracion
"""

# Valores iniciales:
import sys		
N = int(sys.argv[1])
suma, cociente = 0, N

# Precondicion: 

assert(0 < N < 10000000000)

# Calculos

while cociente > 0:
	suma = suma + cociente % 10
	cociente = cociente // 10



# Postcondicion: 
 
assert(suma == sum((N//(10**(i)))%10 for i in range(0, 11) if (N//(10**(i)) != 0)))

 # Salida:
print(suma)

