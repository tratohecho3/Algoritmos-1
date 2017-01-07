"""Realizado por Cesar Colina 13-10299
				 Orlando Chaparro 12-11499

Obviamente a nuestro proyecto le faltan algunas cosas.

Cabe acotar que todas las piezas tienes bien las validaciones de sus movimientos y que 
la carga de las cartas desafios se modifican a traves del archivo "cartaDeDesafio2.txt"

Actualmente nuestro juego se juega mediante la terminal y funciona perfectamente.

Para esta primera entrega solo sirve el nivel facil. Lastimosamente no nos dio el tiempo
para codear las pocas lineas restantes para abrir los otros niveles

"""


import pygame, sys

from pygame.locals import *


M = [['a4', 'b4', 'c4', 'd4', 'a3', 'b3', 'c3', 'd3', 'a2','b2','c2','d2', 'a1','b1','c1','d1'],   
	 ['00', '01', '02', '03', '10', '11', '12', '13', '20','21','22','23', '30','31','32','33']]

cantidadDePiezas = []
EnJuego = True



#FUNCION QUE PERMITE ABRIR UN ARCHIVO Y CREAR MI LISTA POSICIONES
def AbrirArchivo(Nombre):

    try:
        f = open(Nombre, 'r+')
        for line in f.readlines():
            l = line.split('-')

        ultimoCaracter = l[len(l) - 1].split('\n')
        ultimoCaracter = ultimoCaracter[0]

        for i in range(len(l)):
            if int(len(l[i])) == 2:
                posiciones.append(l[i])
            if int(len(l[i])) == 3:
                posiciones.append(l[i])

        posiciones.append( ultimoCaracter )
        assert(len(Nombre) != 0)

    except:
        print("Ha introducido un nombre invalido por favor reinicie e intente de nuevo")    


#FUNCION QUE A PARTIR DE LA LISTA POSICIONES, LLENA MI LISTA TABLEROBLANCO
def LlenarTableroBlanco(posiciones):

    try: 
    	for i in range(len(posiciones)):

    		#FRAGMENTO QUE COLOCA EN POSICION LOS PEONES DENTRO DEL ARREGLO DEL TABLERO:

    		if len(posiciones[i]) == 2:
    			if posiciones[i][0] == 'a':
    				for j in range(1,5):
    					if posiciones[i][1] == str(j):
    						TableroBlanco[4 - j][0] = posiciones[i]

    			if posiciones[i][0] == 'b':
    				for j in range(1,5):
    					if posiciones[i][1] == str(j):
    						TableroBlanco[4 - j][1] = posiciones[i]

    			if posiciones[i][0] == 'c':
    				for j in range(1,5):
    					if posiciones[i][1] == str(j):
    						TableroBlanco[4 - j][2] = posiciones[i]

    			if posiciones[i][0] == 'd':
    				for j in range(1,5):
    					if posiciones[i][1] == str(j):
    						TableroBlanco[4 - j][3] = posiciones[i]

    		#FRAGMENTO QUE COLOCA EN POSICION LAS DEMAS PIEZAS DEL TABLERO:

    		if len(posiciones[i]) == 3:
    			if posiciones[i][1] == 'a':
    				for j in range(1,5):
    					if posiciones[i][2] == str(j):
    						TableroBlanco[4 - j][0] = posiciones[i]

    			if posiciones[i][1] == 'b':
    				for j in range(1,5):
    					if posiciones[i][2] == str(j):
    						TableroBlanco[4 - j][1] = posiciones[i]

    			if posiciones[i][1] == 'c':
    				for j in range(1,5):
    					if posiciones[i][2] == str(j):
    						TableroBlanco[4 - j][2] = posiciones[i]

    			if posiciones[i][1] == 'd':
    				for j in range(1,5):
    					if posiciones[i][2] == str(j):
    						TableroBlanco[4 - j][3] = posiciones[i]

    	assert(len(posiciones) >= 0)

    except:
    	print("Ha ingresado al sistema una Carta De Desafio incorrecta. Intente de nuevo")


#FUNCION QUE DADO UN TABLERO, PUEDES SELECCIONAR UNA DE SUS PIEZAS
def seleccionDePieza(TableroBlanco,EnJuego):

	global pieza
	global coordenadaA
	global coordenadaB

	try:
		if EnJuego:
			while True:
				try:

					a = input("ingrese las coordenas de la casilla que contiene la pieza que desea mover: ")
					coordenadaA = a[0]
					coordenadaB = int(a[1])

					if coordenadaA == 'a':
						coordenadaA = 0

					elif coordenadaA == 'b':
						coordenadaA = 1

					elif coordenadaA == 'c':
						coordenadaA = 2

					elif coordenadaA == 'd':
						coordenadaA = 3

					if coordenadaB == 1:
						coordenadaB = 3

					elif coordenadaB == 2:
						coordenadaB = 2

					elif coordenadaB == 3:
						coordenadaB = 1

					elif coordenadaB == 4:
						coordenadaB = 0
					print(TableroBlanco[coordenadaB][coordenadaA])

					assert( TableroBlanco[coordenadaB][coordenadaA] != 0 )
					break

				except:
					print("Ha introducido una posicion incorrecta, pues esta vacia o no existe")
					print("Recuerde que solo debe seleccionar alguna que casilla que contenga una pieza")
					print("Intente seleccionando de nuevo la casilla")

		pieza = TableroBlanco[coordenadaB][coordenadaA]	
		assert(len(TableroBlanco) > 0)

	except:
		print('Ha elegido un tablero de forma incorrecta. Por intente de nuevo')

	return pieza, coordenadaB, coordenadaA


#FUNCION QUE NOS DEVUELVE UN TableroBlanco NUEVO
def validarJugada(TableroBlanco, pieza, B, A):

	try:

		figura = str
		if len(pieza) == 2 or pieza == "p":
			pieza = 'p'
			figura = 'Peon'

		if len(pieza) == 3 or len(pieza) == 1 and pieza != "p":
			if pieza[0] == 'C':
				figura = 'Caballo'

			elif pieza[0] == 'T':
				figura = 'Torre'

			elif pieza[0] == 'A':
				figura = 'Alfil'

			elif pieza[0] == 'R':
				figura = 'Rey'

			elif pieza[0] == 'D':
				figura = 'Dama'

		while True:
			try:

				casillaNueva = input("Indique la casilla a la cual desea mover la pieza seleccionada: ")
				assert(casillaNueva[0] == 'a' or casillaNueva[0] == 'b' or casillaNueva[0] == 'c' or casillaNueva[0] == 'd' and len(casillaNueva) == 2 and 0 <= int(casillaNueva[1]) <= 4)
				break

			except:
				print("Ha introducido una casilla incorrecta para mover la ficha. please come again") 


		coordenadaNueva = [0, 0]
		
		if casillaNueva[0] == 'a':
			coordenadaNueva[1] = 0

		elif casillaNueva[0] == 'b':
			coordenadaNueva[1] = 1

		elif casillaNueva[0] == 'c':
			coordenadaNueva[1] = 2

		elif casillaNueva[0] == 'd':
			coordenadaNueva[1] = 3

		if casillaNueva[1] == str(1):
			coordenadaNueva[0] = 3

		elif casillaNueva[1] == str(2):
			coordenadaNueva[0] = 2

		elif casillaNueva[1] == str(3):
			coordenadaNueva[0] = 1

		elif casillaNueva[1] == str(4):
			coordenadaNueva[0] = 0

		print(coordenadaNueva)
		print(coordenadaB)
		print(coordenadaA)

		puedeContinuar = False


		if figura == 'Peon':
			if coordenadaNueva[0] == int(coordenadaB - 1) and coordenadaNueva[1] == int(coordenadaA + 1) \
				or coordenadaNueva[1] == int(coordenadaA - 1):

				if TableroBlanco[coordenadaNueva[0]][coordenadaNueva[1]] != 0:
					TableroBlanco[coordenadaB][coordenadaA] = 0
					TableroBlanco[coordenadaNueva[0]][coordenadaNueva[1]] = pieza
					puedeContinuar = True

				else:
					print("No ha sido posible concretar una jugada correcta.")
					print("El peon debe comerse a otra ficha")
			
			else:
				print("Ha introducido una jugada incorrecta. El peon debe comerse a otra ficha")
				print("y no puede salir del tablero.")


		if figura == 'Torre':
			for i in range(0, 16):
				if casillaNueva == M[0][i]:
					n = M[1][i]
					print(n)
					if A == int(n[1]):
						if B < int(n[0]):
							#if int(n[0]) - B <= 3 and TableroBlanco[int(n[0])][int(n[1])] != 0:
							if TableroBlanco[int(n[0])][int(n[1])] != 0:
								TableroBlanco[B][A] = 0
								TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
								puedeContinuar = True
								print('Jugada Valida')
							else:
								pass

						elif int(n[0]) < B:
							#if B - int(n[0]) >= 0 and TableroBlanco[int(n[0])][int(n[1])] != 0:
							if TableroBlanco[int(n[0])][int(n[1])] != 0:
								TableroBlanco[B][A] = 0
								TableroBlanco[int(n[0])][int(n[1])] = pieza[0]

								puedeContinuar = True
								print('Jugada Valida')
							else:
								pass

					if B == int(n[0]):
						if A < int(n[1]):
							#if int(n[1]) - A <= 3 and TableroBlanco[int(n[0])][int(n[1])] != 0:
							if TableroBlanco[int(n[0])][int(n[1])] != 0:
								TableroBlanco[B][A] = 0
								TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
								puedeContinuar = True
								print('Jugada Valida')
							else:
								pass
								
						elif int(n[1]) < A:
							#if A - int(n[1]) >= 0 and TableroBlanco[int(n[0])][int(n[1])] != 0:
							if TableroBlanco[int(n[0])][int(n[1])] != 0:
								TableroBlanco[B][A] = 0
								TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
								puedeContinuar = True
								print('Jugada Valida')
							else:
								pass


		if figura == 'Caballo':
			for i in range(0, 16):
				if casillaNueva == M[0][i]:
					n = M[1][i]
					print(n)
					if B == int(n[0]) + 1:

						if A == int(n[1]) + 2 or A == int(n[1]) - 2 and 0 <= int(n[0]) < 5 and 0 <= int(n[1]) < 5:
							if TableroBlanco[int(n[0])][int(n[1])] != 0:
								TableroBlanco[B][A] = 0
								TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
								puedeContinuar = True
								print('Jugada Valida')
							else:
								pass


					if B == int(n[0]) + 2:

						if A == int(n[1]) + 1 or A == int(n[1]) - 1 and 0 <= int(n[0]) < 5 and 0 <= int(n[1]) < 5:
							if TableroBlanco[int(n[0])][int(n[1])] != 0:
								TableroBlanco[B][A] = 0
								TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
								puedeContinuar = True
								print('Jugada Valida')
							else:
								pass


					if B + 1 == int(n[0]):

						if A == int(n[1]) + 2 or A == int(n[1]) - 2 and 0 <= int(n[0]) < 5 and 0 <= int(n[1]) < 5:
							if TableroBlanco[int(n[0])][int(n[1])] != 0:
								TableroBlanco[B][A] = 0
								TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
								puedeContinuar = True
								print('Jugada Valida')
							else:
								pass

					if B + 2 == int(n[0]):

						if A == int(n[1]) + 1 or A == int(n[1]) - 1 and 0 <= int(n[0]) < 5 and 0 <= int(n[1]) < 5:
							if TableroBlanco[int(n[0])][int(n[1])] != 0:
								TableroBlanco[B][A] = 0
								TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
								puedeContinuar = True
								print('Jugada Valida')
							else:
								pass

			


		if figura == 'Alfil':
			for i in range(0, 16):
				if casillaNueva == M[0][i]:
					n = M[1][i]
					print(n)
					if B > int(n[0]):
						if abs(B - int(n[0])) == abs(A - int(n[1])) and TableroBlanco[int(n[0])][int(n[1])] != 0:
							TableroBlanco[B][A] = 0
							TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
							puedeContinuar = True
							print('Jugada Valida')
						else:
								pass


					if B < int(n[0]):
						if abs(int(n[0]) - B) == abs(int(n[1]) - A) and TableroBlanco[int(n[0])][int(n[1])] != 0:
							TableroBlanco[B][A] = 0
							TableroBlanco[int(n[0])][int(n[1])] = pieza[0]
							puedeContinuar = True
							print('Jugada Valida')
						else:
								pass





		if puedeContinuar == False:
			print("Ha realizado una jugada invalida, intente de nuevo")


		assert(len(TableroBlanco) > 0 and len(pieza) > 0 and len(B) >= 0 and len(A) >= 0)


	except:
		print("Ha elegido posiciones incorrectas para inicializar las piezas. Intente de nuevo")

	return TableroBlanco


#FUNCION QUE DADO TableroBlanco, DIBUJA LAS PIEZAS EN LA INTERFAZ
def escribir_tablero(ventana,TableroBlanco):

	assert(len(TableroBlanco) > 0)

	# Esta funcion permite colocar las piezas del arreglo en la interfaz
	peon = pygame.image.load("Imagenes/PIEZAS/peon.png")
	torre = pygame.image.load("Imagenes/PIEZAS/torre.png")
	caballo = pygame.image.load("Imagenes/PIEZAS/caballo.png")
	alfil = pygame.image.load("Imagenes/PIEZAS/alfil.png")
	rey = pygame.image.load("Imagenes/PIEZAS/rey.png")
	dama = pygame.image.load("Imagenes/PIEZAS/reina.png")


	posTop = [328,454,580,706] 		# posTop y posLeft seran las posiciones de arriba y de la izquierda que 
	posLeft = [22,144,267,386]		# tendran los rectangulos

	cantidadDePiezas = [] 			
	piezasRestantes = len(cantidadDePiezas) 	# Variable que almacena la cantidad de piezas que estan en el tablero


	for i in range(4):
		for j in range(4):
			if TableroBlanco[j][i] != 0 and len(TableroBlanco[j][i]) ==  2 or TableroBlanco[j][i] == "p":
				a = i
				b = j
				ventana.blit(peon,(posTop[a], posLeft[b]))

			if TableroBlanco[j][i] != 0 and (len(TableroBlanco[j][i]) ==  3 or len(TableroBlanco[j][i]) ==  1) and TableroBlanco[j][i] != "p" :
				a = i
				b = j
				if TableroBlanco[j][i][0] == 'T':
					ventana.blit(torre,(posTop[a], posLeft[b]))
				if TableroBlanco[j][i][0] == 'C':
					ventana.blit(caballo,(posTop[a], posLeft[b]))
				if TableroBlanco[j][i][0] == 'A':
					ventana.blit(alfil,(posTop[a], posLeft[b]))
				if TableroBlanco[j][i][0] == 'R':
					ventana.blit(rey,(posTop[a], posLeft[b]))
				if TableroBlanco[j][i][0] == 'D':
					ventana.blit(dama,(posTop[a], posLeft[b]))

	print(TableroBlanco)
	pygame.display.update()

	assert(len(posTop) > 0 and len(posLeft) > 0)


#FUNCION QUE DADO TableroBlanco NOS DICE CUANTAS PIEZAS HAY
def Cantidad_de_piezas(TableroBlanco):

	try:
		for x in range(4):
			for y in range(4):
				if TableroBlanco[x][y] != 0:
					cantidadDePiezas.append(1)

		cantidad = len(cantidadDePiezas)
		assert(TableroBlanco > 0)

	except:
		print("La cantidad de piezas se calculo de forma incorrecta. Reinicie el programa e intente mas tarde")

	return cantidad


#FUNCION PRINCIPAL QUE CARGA E INICIA TODOS LOS COMPONENTES PRINCIPALES DEL PROGRAMA
def Iniciar():
	pygame.init()
	AbrirArchivo("cartaDeDesafio2.txt")
	LlenarTableroBlanco(posiciones)
	

	#VENTANA
	ventana = pygame.display.set_mode((800,700))
	pygame.display.set_caption("Solitaire Chess")


	#IMAGENES
	fondoMadera = pygame.image.load("Imagenes/Background-Wood-HD-Wallpaper.jpg")
	fondo_inicial = pygame.image.load("Imagenes/FONDO1.jpg")
	tablero = pygame.image.load("Imagenes/tablero5.jpg")
	rey_negro = pygame.image.load("Imagenes/rey_negro.png") 
	menu = pygame.image.load("Imagenes/menu.jpg")
	menu2 = pygame.image.load("Imagenes/menu2.jpg")

	#ICONOS DE LAS PIEZAS:
	caballo = pygame.image.load("Imagenes/caballo.jpg")
	alfil = pygame.image.load("Imagenes/PIEZAS/alfil.png")

	#COLORES
	color = (255, 245, 238)	

	#COORDENADAS
	posX = 150
	posY = 50

	#VARIABLE QUE GUARDA EL NOMBRE DEL JUGADOR
	nombre = ""
	nombre2 = ""

	#FUENTES DE TEXTO
	fuente = pygame.font.Font(None,30)
	
	#VARIABLE AUXILIAR
	booleano = False
	booleano2 = False
	booleano3 = False
	booleano4 = False
	


	while True:
		
		
		#FONDO NUMERO 0 (INICIAL)
		
		ventana.blit(fondo_inicial,(0,0))
		texto = fuente.render(nombre,0,(0,0,0),(255,255,255))
		ventana.blit(texto,(400,425))

		#TODOS LOS EVENTOS
		
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			if evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_a:
					
					nombre = nombre + "a"

				if evento.key == pygame.K_b:
					
					nombre = nombre + "b"

				
				if evento.key == pygame.K_c:
						
					nombre = nombre + "c"

				if evento.key == pygame.K_d:
							
					nombre = nombre + "d"
				if evento.key == pygame.K_e:
							
					nombre = nombre + "e"
				if evento.key == pygame.K_f:
							
					nombre = nombre + "f"

				if evento.key == pygame.K_g:
							
					nombre = nombre + "g"
				if evento.key == pygame.K_h:
							
					nombre = nombre + "h"

				if evento.key == pygame.K_i:
							
					nombre = nombre + "i"

				if evento.key == pygame.K_j:
							
					nombre = nombre + "j"

				if evento.key == pygame.K_k:
							
					nombre = nombre + "k"

				if evento.key == pygame.K_l:
							
					nombre = nombre + "l"

				if evento.key == pygame.K_m:
							
					nombre = nombre + "m"

				if evento.key == pygame.K_n:
							
					nombre = nombre + "n"

				if evento.key == pygame.K_o:
							
					nombre = nombre + "o"

				if evento.key == pygame.K_p:
							
					nombre = nombre + "p"

				if evento.key == pygame.K_q:
							
					nombre = nombre + "q"

				if evento.key == pygame.K_r:
							
					nombre = nombre + "r"

				if evento.key == pygame.K_s:
							
					nombre = nombre + "s"

				if evento.key == pygame.K_t:
							
						nombre = nombre + "t"

				if evento.key == pygame.K_u:
							
					nombre = nombre + "u"

				if evento.key == pygame.K_v:
							
					nombre = nombre + "v"

				if evento.key == pygame.K_w:
							
					nombre = nombre + "w"

				if evento.key == pygame.K_x:
							
					nombre = nombre + "x"

				if evento.key == pygame.K_y:
							
					nombre = nombre + "y"

				if evento.key == pygame.K_z:
							
					nombre = nombre + "z"

				if evento.key == pygame.K_SPACE:

					nombre = nombre + " "

				if evento.key == pygame.K_BACKSPACE:

					auxiliar = nombre
					longitud = len(nombre) - 1
					nombre = ""

					for i in range(longitud):
			
						nombre = nombre + auxiliar[i]
				



					

				if evento.key == pygame.K_RETURN:

					booleano = True


				if evento.key == pygame.K_1:
					if booleano3:
						booleano4 = True
					if booleano2:
						booleano3 = True

					booleano2 = True

				if evento.key == pygame.K_4:
					pygame.quit()
					sys.exit()
		
		
		
		# FONDO NUMERO 1 (CUANDO EL USUARIO PRESIONA ENTER DESPUES DE INGRESAR SU NOMBRE)
		if booleano:
			
			ventana.blit(menu,(0,0))
			texto2 = fuente.render("Bienvenido " + nombre,0,(255,255,255),(0,0,0))
			ventana.blit(texto2,(300,10))



		#FONDO NUMERO 2 (CUANDO EL USUARIO PRESIONA EL NUMERO DE LA OPCION QUE DESEA)
		if booleano2:
			ventana.fill(color)
			ventana.blit(menu2,(0,0))
			
			
		#FONDO NUMERO 3 (CUANDO EL USUARIO PRESIONA EL NUMERO DE LA OPCION QUE DESEA)
		if booleano3:
			#ventana.fill(color)
			ventana.blit(fondoMadera,(0,0))
			ventana.blit(tablero,(200,0))
			#ventana.blit(rey_negro,(25,25))
			if booleano4:
				#DIBUJO INICIAL
				escribir_tablero(ventana,TableroBlanco)

				
				lugaresDondeHayPiezas(TableroBlanco)
				evaluacionDeJugadas(coordenadasDeLasFichas,listaDeFichas)
				jugando = Perder(listaDeJugadas,coordenadasDeLasFichas,EnJuego,ventana)
				if jugando:
					seleccionDePieza(TableroBlanco,EnJuego)
					Tablero = validarJugada(TableroBlanco, pieza, coordenadaB, coordenadaA)

					escribir_tablero(ventana,Tablero)


			
			
			
			
		

		#ACTUALIZACION DE LA PANTALLA
		pygame.display.update()

#ESTA FUNCION NO FUE UTILIZADA PARA ESTA PRIMERA ENTREGA
def Teclado(nombre):

	try:	
		while True:
			for evento in pygame.event.get():
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
				if evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_a:
							
						nombre = nombre + "a"

					if evento.key == pygame.K_b:
							
						nombre = nombre + "b"

						
					if evento.key == pygame.K_c:
								
						nombre = nombre + "c"

					if evento.key == pygame.K_d:
									
						nombre = nombre + "d"
					if evento.key == pygame.K_e:
									
						nombre = nombre + "e"
					if evento.key == pygame.K_f:
									
						nombre = nombre + "f"

					if evento.key == pygame.K_g:
									
						nombre = nombre + "g"
					if evento.key == pygame.K_h:
									
						nombre = nombre + "h"

					if evento.key == pygame.K_i:
									
						nombre = nombre + "i"

					if evento.key == pygame.K_j:
									
						nombre = nombre + "j"

					if evento.key == pygame.K_k:
									
						nombre = nombre + "k"

					if evento.key == pygame.K_l:
									
						nombre = nombre + "l"

					if evento.key == pygame.K_m:
									
						nombre = nombre + "m"

					if evento.key == pygame.K_n:
									
						nombre = nombre + "n"

					if evento.key == pygame.K_o:
									
						nombre = nombre + "o"

					if evento.key == pygame.K_p:
									
						nombre = nombre + "p"

					if evento.key == pygame.K_q:
									
						nombre = nombre + "q"

					if evento.key == pygame.K_r:
									
						nombre = nombre + "r"

					if evento.key == pygame.K_s:
									
						nombre = nombre + "s"

					if evento.key == pygame.K_t:
									
							nombre = nombre + "t"

					if evento.key == pygame.K_u:
									
						nombre = nombre + "u"

					if evento.key == pygame.K_v:
									
						nombre = nombre + "v"

					if evento.key == pygame.K_w:
									
						nombre = nombre + "w"

					if evento.key == pygame.K_x:
									
						nombre = nombre + "x"

					if evento.key == pygame.K_y:
									
						nombre = nombre + "y"

					if evento.key == pygame.K_z:
									
						nombre = nombre + "z"

					if evento.key == pygame.K_SPACE:

						nombre = nombre + " "

					if evento.key == pygame.K_BACKSPACE:

						auxiliar = nombre
						longitud = len(nombre) - 1
						nombre = ""

						for i in range(longitud):
					
							nombre = nombre + auxiliar[i]
		assert(len(nombre) != -10)

	except:
		print("Los datos del nombre fueron procesados de forma incorrecta. Intente de nuevo")

		
	return nombre		

#FUNCION QUE DADO TableroBlanco NOS REGRESA DOS LISTAS, QUE PIEZAS HAY Y EN QUE COORDENADAS ESTAN
def lugaresDondeHayPiezas(TableroBlanco):

	assert(len(TableroBlanco))
	global coordenadasDeLasFichas
	global listaDeFichas


	ficha = ''
	coordenadasDeLasFichas = []
	listaDeFichas = []

	for fil in range(0,4):
		for col in range(0,4):
			if TableroBlanco[fil][col] != 0:
				pieza = TableroBlanco[fil][col]

				if len(pieza) == 2 or pieza == 'p':
					pieza = 'p'
					ficha = 'Peon'
					coordenadasDeLasFichas.append((fil, col))
					listaDeFichas.append(ficha)


				if len(pieza) == 3 or len(pieza) == 1 and pieza != 'p':
					if pieza[0] == 'C':
						ficha = 'Caballo'
						coordenadasDeLasFichas.append((fil, col))
						listaDeFichas.append(ficha)

					elif pieza[0] == 'T':
						ficha = 'Torre'
						coordenadasDeLasFichas.append((fil, col))
						listaDeFichas.append(ficha)

					elif pieza[0] == 'A':
						ficha = 'Alfil'
						coordenadasDeLasFichas.append((fil, col))
						listaDeFichas.append(ficha)

					elif pieza[0] == 'R':
						ficha = 'Rey'
						coordenadasDeLasFichas.append((fil, col))
						listaDeFichas.append(ficha)

					elif pieza[0] == 'D':
						ficha = 'Dama'
						coordenadasDeLasFichas.append((fil, col))
						listaDeFichas.append(ficha)


	return coordenadasDeLasFichas

	return listaDeFichas
				

#FUNCION QUE DADAS LAS PIEZAS Y SUS COORDENADAS, CALCULA TODAS LAS POSIBLES JUGADAS
def evaluacionDeJugadas(coordenadasDeLasFichas, listaDeFichas):
	assert(len(coordenadasDeLasFichas) > 0 and len(listaDeFichas) > 0)
	global listaDeJugadas

	listaDeJugadas = []

	for i in range(0, len(listaDeFichas)):

		if listaDeFichas[i] == 'Peon':
			
			peonJugadas(coordenadasDeLasFichas[i][0], coordenadasDeLasFichas[i][1], listaDeJugadas)

		if listaDeFichas[i] == 'Caballo':

			caballoJugadas(coordenadasDeLasFichas[i][0], coordenadasDeLasFichas[i][1], listaDeJugadas)

		if listaDeFichas[i] == 'Alfil':

			alfilJugadas(coordenadasDeLasFichas[i][0], coordenadasDeLasFichas[i][1], listaDeJugadas)

		if listaDeFichas[i] == 'Torre':

			torreJugadas(coordenadasDeLasFichas[i][0], coordenadasDeLasFichas[i][1], listaDeJugadas)

	return listaDeJugadas
	

#FUNCION QUE CALCULA LAS POSIBLES JUGADAS DE UN PEON SEGUN SUS COORDENADAS
def peonJugadas(x,y,listaDeJugadas):
	assert(x>= 0 and y >=0)

	if 0 <= x-1 <=3:
		if 0 <= y-1 <= 3:
			listaDeJugadas.append((x-1,y-1))
		if 0 <= y+1 <= 3:
			listaDeJugadas.append((x-1,y+1))


#FUNCION QUE CALCULA LAS POSIBLES JUGADAS DE UN CABALLO SEGUN SUS COORDENADAS
def caballoJugadas(x,y,listaDeJugadas):
	assert(x>= 0 and y >=0)
	if 0 <= x-2 <=3:
		if 0 <= y-1 <= 3:
			listaDeJugadas.append((x-2,y-1))
		if 0 <= y+1 <= 3:
			listaDeJugadas.append((x-2,y+1))

	if 0 <= x-1 <=3:
		if 0 <= y-2 <= 3:
			listaDeJugadas.append((x-1,y-2))
		if 0 <= y+2 <= 3:
			listaDeJugadas.append((x-1,y+2))

	if 0 <= x+1 <=3:
		if 0 <= y-2 <= 3:
			listaDeJugadas.append((x+1,y-2))
		if 0 <= y+2 <= 3:
			listaDeJugadas.append((x+1,y+2))

	if 0 <= x+2 <=3:
		if 0 <= y-1 <= 3:
			listaDeJugadas.append((x+2,y-1))
		if 0 <= y+1 <= 3:
			listaDeJugadas.append((x+2,y+1))


#FUNCION QUE CALCULA LAS POSIBLES JUGADAS DE UN ALFIL SEGUN SUS COORDENADAS
def alfilJugadas(x,y,listaDeJugadas): 
	assert(x>= 0 and y >=0)
	if 0 <= x-1 <=3:
		if 0 <= y-1 <= 3:
			listaDeJugadas.append((x-1,y-1))
		if 0 <= y+1 <= 3:
			listaDeJugadas.append((x-1,y+1))

	if 0 <= x-2 <=3:
		if 0 <= y-2 <= 3:
			listaDeJugadas.append((x-2,y-2))
		if 0 <= y+2 <= 3:
			listaDeJugadas.append((x-2,y+2))

	if 0 <= x-3 <=3:
		if 0 <= y-3 <= 3:
			listaDeJugadas.append((x-3,y-3))
		if 0 <= y+3 <= 3:
			listaDeJugadas.append((x-3,y+3))

	if 0 <= x+1 <=3:
		if 0 <= y-1 <= 3:
			listaDeJugadas.append((x+1,y-1))
		if 0 <= y+1 <= 3:
			listaDeJugadas.append((x+1,y+1))

	if 0 <= x+2 <=3:
		if 0 <= y-2 <= 3:
			listaDeJugadas.append((x+2,y-2))
		if 0 <= y+2 <= 3:
			listaDeJugadas.append((x+2,y+2))

	if 0 <= x+3 <=3:
		if 0 <= y-3 <= 3:
			listaDeJugadas.append((x+3,y-3))
		if 0 <= y+3 <= 3:
			listaDeJugadas.append((x+3,y+3))


#FUNCION QUE CALCULA LAS POSIBLES JUGADAS DE UNA TORRE SEGUN SUS COORDENADAS
def torreJugadas(x,y,listaDeJugadas): 
	if 0 <= y <=3:
		if 0 <= x + 1 <= 3:
			listaDeJugadas.append((x+1,y))
		if 0 <= x - 1 <= 3:
			listaDeJugadas.append((x-1,y))
		
		if 0 <= x + 2 <= 3:

			listaDeJugadas.append((x+2,y))
		if 0 <= x - 2 <= 3:
			listaDeJugadas.append((x-2,y))

		if 0 <= x + 3 <= 3:
			listaDeJugadas.append((x+3,y))
		if 0 <= x - 3 <= 3:
			listaDeJugadas.append((x-3,y))

	if 0 <= x <=3:
		if 0 <= y + 1 <= 3:
			listaDeJugadas.append((x,y+1))
		if 0 <= y - 1 <= 3:
			listaDeJugadas.append((x,y-1))
		
		if 0 <= y + 2 <= 3:

			listaDeJugadas.append((x,y+2))
		if 0 <= y - 2 <= 3:
			listaDeJugadas.append((x,y-2))

		if 0 <= y + 3 <= 3:
			listaDeJugadas.append((x,y+3))
		if 0 <= y - 3 <= 3:
			listaDeJugadas.append((x,y-3))

#FUNCION QUE DETERMINA CUANDO NO QUEDAN JUGADAS DISPONIBLES
def Perder(listaDeJugadas,coordenadasDeLasFichas,EnJuego,ventana):
	solucion = []
	fondo_perder = pygame.image.load("Imagenes/gameover.png")
	fondo_ganar = pygame.image.load("Imagenes/ganador.png")
	fuente = pygame.font.Font(None,30)
	texto = fuente.render("Ganaste",0,(0,0,0),(255,255,255))
	texto2 = fuente.render("Perdiste",0,(0,0,0),(255,255,255))
	
	print(listaDeJugadas)
	print(' \n')
	print(coordenadasDeLasFichas)

	for i in range(0, len(listaDeJugadas)):
		for j in range(0, len(coordenadasDeLasFichas)):
			if coordenadasDeLasFichas[j] == listaDeJugadas[i]:
				solucion.append(coordenadasDeLasFichas[j])

	if len(solucion) == 0:
		if len(coordenadasDeLasFichas) > 1:
			EnJuego = False
			print("perdiste")
			ventana.blit(texto2,(400,100))
			#ventana.blit(fondo_perder,(0,0))
			#sys.exit()
		elif len(coordenadasDeLasFichas) == 1:
			EnJuego = False
			print("ganaste")
			ventana.blit(texto,(400,100))
			#ventana.blit(fondo_ganar,(0,0))
			#sys.exit()
		
	return EnJuego
	


				







TableroBlanco = [ [0 for i in range(4)] for j in range(4) ]
posiciones =  []
  

Iniciar()