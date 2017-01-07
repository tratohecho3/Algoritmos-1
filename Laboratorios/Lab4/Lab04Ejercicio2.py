"""
# Lab04Ejercicio1.py


# DESCRIPCION: 

Es un algoritmo que encripta o desencripta frases

# Versión de: 

	Cesar Colina 13-10299
	Gustavo Castellanos 14-10192



# Ultima modificacion: 11/10/2016





# CONSTANTES:
a: int // llave para frase 1
b: int // llave para frase 2





# VARIABLES:
n: int // llave
pregunta: str // Respuesta de si quieres encriptar o desencriptar
frase: str // frase ingresada por el usuario
lista: lista// lista con todas las letras del abecedario
s: str // frase encriptada o desencriptada
s1: str // frase 1 desencriptada
s2: str // frase 2 encriptada
frase1: str // informacion del enunciado
frase2: str // informacion del enunciado  


"""


# Valores iniciales:
n = int(input("Introduce la llave "))

pregunta = input("Quieres Encriptar(1) o Quieres desencriptar(2)")

frase = input("Introduce la frase	")

frase = frase.lower()

lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Precondicion: 

assert( n >= 0 and (pregunta == "1" or pregunta == "2") and len(frase) > 0)

#Calculos

if pregunta == "1":
	s = ""
	for i in frase:
		if i == " ":
			s += " "
		else: 
			for k in range(len(lista)):
				if lista[k] == i:
					s += lista[(k+n)%len(lista)]



if pregunta == "2":
	s = ""
	for i in frase:
		if i == " ":
			s += " "
		else: 
			for k in range(len(lista)):
				if lista[k] == i:
					s += lista[(k-n)%len(lista)]



a = 3
frase1 = "Dqlpr frq orv vljxlhqwhv hmhuflflrv"
frase1 = frase1.lower()
s1 = ""
for i in frase1:
	if i == " ":
		s1 += " "
	else: 
		for k in range(len(lista)):
			if lista[k] == i:
				s1 += lista[(k-a)%len(lista)]


b = 10
frase2 = "Pablito clavo un clavito"
frase2 = frase2.lower()

s2 = ""
for i in frase2:
	if i == " ":
		s2 += " "
	else: 
		for k in range(len(lista)):
			if lista[k] == i:
				s2 += lista[(k+b)%len(lista)]

















# Postcondicion: 
 assert(True)

 # Salida:
if pregunta == "1":
 	print("La frase encriptada es ",s)

if pregunta == "2":
	print("La frase desencriptada es ", s)

print("Este mensaje Dqlpr frq orv vljxlhqwhv hmhuflflrv desencriptado es   ", s1)
print("Este mensaje Pablito clavo un clavito encriptado es   ", s2)

