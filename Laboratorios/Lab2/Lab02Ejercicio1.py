"""
LABARATORIO # 2

REALIZADO POR CESAR COLINA 13-10299

EJERCICIO 1

Lab02Ejercicio1.py


DESCRIPCION: El algoritmo determina si puede o no votar dentro de un sistema electoral.En  ese  país,  se  permite  votar  
a  los  descendientes directos extranjeros sólo si son mayores a 25 años, pero a los nativos se les permite votar con solo 18 años o más. 

CONSTANTES:
- esDescendienteExtranjero : bool;

- edad : int;
VARIABLES:

puedeVotar: bool;

"""
#DATOS DE ENTRADA

edad = int(input("Por favor ingrese su edad"))
esDescendienteExtranjero = input("es Ud un descendiente extranjero: s/n")

#PRECONDICION

assert(0 < edad < 120)

#CALCULOS

puedeVotar = True





if esDescendienteExtranjero == "s" or esDescendienteExtranjero == "S":
	esDescendienteExtranjero = True 
else:
	esDescendienteExtranjero = False



if esDescendienteExtranjero == True:
	if edad >= 25:
		pass
	elif edad < 25:
		puedeVotar = False

elif esDescendienteExtranjero == False:
	if edad >= 18:
		pass
	elif edad < 18:
		puedeVotar = False 
		
print (puedeVotar)

#POSTCONDICION
assert((esDescendienteExtranjero == True) or (esDescendienteExtranjero == False) )
