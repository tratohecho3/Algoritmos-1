
"""

# Prelab8Ejercicio2.py


# DESCRIPCION: Algoritmo que devuelve la operacion matematica entre dos enteros
			   ingresados por el usuario dependiendo del valor de uno de ellos


# Versión de: 

Colina Cesar 13-10299
Chaparro Orlando 12-11499 



# Ultima modificacion: 07/11/2016



# VARIABLES:

m: int // entero ingresado por el usuario que especifica que tipo de operacion sera realizada
n: int // entero ingresado por el usuario para ser operado junto con el entero m
resultado: float // resultado de la operacion de m y n
r: float: // valor de retorno para las funciones

"""

while True:
	try:
		m = int(input("Ingrese un entero m: "))
		n = int(input("Ingrese un entero n: "))
		assert(m > -100000000 and n > -10000000)
		break
				
	except:
		print("Hubo un error al ingresar datos al sistema")
		print("Verifique que los datos ingresados al sistema sean del valor y tipo correcto")

def mIgualADiez(m: int, n: int):
	assert(m == 10)
	resultado = m / n
	
	return resultado
	assert(resultado == m/n)

def mIgualACinco(m: int, n: int):
	assert(m == 5)
	resultado = m * n
	
	return resultado
	assert(resultado == m * n)
	
def mIgualADos(m: int, n: int):
	assert(m == 2)
	resultado = m ** n
	
	return resultado
	assert(resultado == m ** n)

def CualquierOtroCaso(m: int, n: int):
	assert(m != 10 and m != 5 and m != 2)
	resultado = m
	
	return resultado
	assert(resultado == m)

if m == 10:
	r = mIgualADiez(m, n)
	
elif m == 5:
	r = mIgualACinco(m, n)

elif m == 2:
	r = mIgualADos(m, n)

else:
	r = CualquierOtroCaso(m, n)

print("La respuesta para los enteros m y n elegidos es: ")
print(r)
