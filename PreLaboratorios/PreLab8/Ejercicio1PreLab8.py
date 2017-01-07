
"""

# Prelab8Ejercicio1.py


# DESCRIPCION: Algoritmo que realiza la concatenacion de dos tipos de variables 
			   dependiendo de una opcion elegida por el usuario


# Versión de: 

Colina Cesar 13-10299
Chaparro Orlando 12-11499 



# Ultima modificacion: 07/11/2016



# VARIABLES:

decision: str // letra para denotar la opcion del usuario
enteroA: int // entero ingresado por el usuario para ser concatenado con otro elemento
enteroB: int // entero ingresado por el usuario para ser concatenado con otro elemento
respuestaA: int // resultado de la concatenacion de elementos para el caso A
strA: str // palabra ingresada por el usuario para ser concatenada con otra palabra
strB: str // palabra ingresada por el usuario para ser concatenada con otra palabra
respuestaB: str // resultado de la concatenacion de elementos para el caso B
arregloA: array // conjunto cuya longitud y elementos son ingresadas por el usuario para ser concatenado con otro elemento
arregloB: array // conjunto cuya longitud y elementos son ingresadas por el usuario para ser concatenado con otro elemento
longitudA: int // numero que denota la cantidad de elementos que tendra el arreglo A
longitudB: int // numero que denota la cantidad de elementos que tendra el arreglo B
elemento: str // palabra para designar cada uno de los elementos que tendran los arreglos
respuestaC: array // resultado de la concatenacion de elementos para el caso C
respuestaD: str // resultado de la concatenacion de elementos para el caso D
resultado: str // resultado de la concatenacion de elementos final

"""

# VALORES INICIALES:

print("A continuacion presione la tecla correspondiente para realizar la concatenacion de elementos de la siguiente manera:")
print(" a.- entero + entero")
print(" b.- string + string")
print(" c.- lista + lista")
print(" d.- entero + string")
print(" e.- entero + lista")
print(" f.- string + lista")


# VERIFICACION DE LA PRECONDICION:

while True:
	try:
		decision = input(": ")
		assert(decision == "a" or decision == "b" or decision == "c" or decision == "d" or decision == "e" or decision == "f")
		break
		
	except:
		print("Recuerde que solo puede ingresar las letras de la 'a' a la 'f' ")
		print("Por favor use solo minusculas")
		

# DECLARACION DE CADA UNA DE LAS FUNCIONES USADAS PARA REALIZAR EL PROGRAMA:

def intMasInt():
	while True:
		try:
			enteroA = int(input("Ingrese un entero a: "))
			enteroB = int(input("Ingrese un entero b: "))	  
			assert(enteroA > -100000000 and enteroB > -10000000)
			break
				
		except:
			print("Hubo un error al ingresar datos al sistema")
			print("Verifique que los datos ingresados al sistema sean del valor correcto")
	
	respuestaA = str(enteroA) + str(enteroB)
		
	assert( len(respuestaA) > 0 )	
	return respuestaA
	

def strMasStr():
	while True:
		try:
			strA = input("Ingrese una palabra a: ")
			strB = input("Ingrese una palabra b: ")	  
			assert(len(strA) > 0 and len(strB) > 0)
			break
				
		except:
			print("Hubo un error al ingresar datos al sistema")
			print("Verifique que los datos ingresados al sistema sean del tipo correcto")
	
	respuestaB = strA + strB	
	
	assert( len(respuestaB) > 0 )
	return respuestaB
	
def arrayMasArray():
	
	arregloA = []
	arregloB = []
		
	while True:
		try:
			longitudA = int(input("Ingrese la longitud del arreglo A: "))
			longitudB = int(input("Ingrese la longitud del arreglo B: "))	  
			assert(longitudA > 0 and longitudB > 0)
			break
					
		except:
			print("Hubo un error al ingresar datos al sistema")
			print("Verifique que los datos ingresados al sistema sean del valor correcto")
			print("Cada arreglo debe contener al menos un elemento")
		
	for i in range(longitudA):
		if len(arregloA) == 0:
			elemento = input("Ingrese un elemento al arreglo A: ")
		else:
			elemento = input("Ingrese otro elemento al arreglo A: ")
		arregloA.append(elemento)
			
	for i in range(longitudB):
		if len(arregloB) == 0:
			elemento = input("Ingrese un elemento al arreglo B: ")
		else:
			elemento = input("Ingrese otro elemento al arreglo B: ")
		arregloB.append(elemento)	


	respuestaC = arregloA + arregloB	
	
	assert( len(respuestaC) > 0 )
	return respuestaC


def intMasStr():
	while True:
		try:
			enteroA = int(input("Ingrese un entero a: "))
			strB = input("Ingrese un palabra b: ")	  
			assert(enteroA > -100000000 and len(strB) > 0)
			break
				
		except:
			print("Hubo un error al ingresar datos al sistema")
			print("Verifique que los datos ingresados al sistema sean del valor correcto")
	
	respuestaD = str(enteroA) + strB	
	
	assert( len(respuestaD) > 0 )	
	return respuestaD
	

def intMasArray():
	
	arregloB = []
		
	while True:
		try:
			enteroA = int(input("Ingrese un entero A: "))
			longitudB = int(input("Ingrese la longitud del arreglo B: "))	  
			assert(enteroA > -100000000 and longitudB > 0)
			break
					
		except:
			print("Hubo un error al ingresar datos al sistema")
			print("Verifique que los datos ingresados al sistema sean del valor correcto")
			print("El arreglo B debe contener al menos un elemento")
					
	for i in range(longitudB):
		if len(arregloB) == 0:
			elemento = input("Ingrese un elemento al arreglo B: ")
		else:
			elemento = input("Ingrese otro elemento al arreglo B: ")
		arregloB.append(elemento)	


	arregloB.append(enteroA)
	
	assert( len(arregloB) > 1 )
	return arregloB

def strMasArray():
	
	arregloB = []
		
	while True:
		try:
			strA = input("Ingrese una palabra A: ")
			longitudB = int(input("Ingrese la longitud del arreglo B: "))	  
			assert(len(strA) > 0 and longitudB > 0)
			break
					
		except:
			print("Hubo un error al ingresar datos al sistema")
			print("Verifique que los datos ingresados al sistema sean del valor correcto")
			print("El arreglo B debe contener al menos un elemento")
					
	for i in range(longitudB):
		if len(arregloB) == 0:
			elemento = input("Ingrese un elemento al arreglo B: ")
		else:
			elemento = input("Ingrese otro elemento al arreglo B: ")
		arregloB.append(elemento)	


	arregloB.append(strA)
	
	assert( len(arregloB) > 0 )
	return arregloB


# CALCULOS:

if decision == "a":
	resultado = intMasInt()

elif decision == "b":
	resultado = strMasStr()

elif decision == "c":
	resultado = arrayMasArray()
	
elif decision == "d":
	resultado = intMasStr()
	
elif decision == "e":
	resultado = intMasArray()

elif decision == "f":
	resultado = strMasArray()


# VALORES DE SALIDA:

print("La concatenacion de los datos resultantes para la decision elegida es: ")
print(resultado)
