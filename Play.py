import DarIncongnita
import MeterGuiones
import ImprimirEspaciado
import MeterLetra
import Control_LetraEnPalabra
import Hangman
import MenuPartida
import time
import Limpiar
import Ranking



def play():

	jugando = True
	Intentos = 7

	jugando= [True,Intentos]

	listapalabras = DarIncongnita.DarIncognitaDesdeArchivo()#Hacer desde otra funcion para no llamar la lista del archivo cada vez que se llame esta funcion
	palaacer=[]#Crea una lista de palabras acertadas

	puntuacion = -1

	while jugando[0]:
		puntuacion = puntuacion+1
		jugando,listapalabras,palaacer = playMatch(jugando[1],listapalabras,palaacer,puntuacion)

	
	#aca va venir el tema de guardar la puntuacion
		
	#pedir nombre y eso.
	

	nombre = Ranking.pedir_ingreso_nombre()

	Puntuacion_a_Guardar = Ranking.crear_tupla_nombre_puntos(nombre,puntuacion)

	listaPuntos_aGuardar = Ranking.meter_nueva_puntuacion_a_lista(Puntuacion_a_Guardar, Ranking.CargarRanking())

	Ranking.GuardarRanking(listaPuntos_aGuardar)

	#
	

	
		


		
	

def playMatch(Intentos,listapalabras,palaacer,puntos):#Cada playmach es una palabra

	incognitaSolucion,listapalabras = DarIncongnita.SeleccionPalabra(listapalabras)
	incognitaGuion = ""
	incognitaGuion = MeterGuiones.MeterGuiones(incognitaSolucion)

	Gano = False
	Perdio = False
	Intentos = Intentos
	lista1 = []
	while not(Gano) and not(Perdio):

		Limpiar.Limpiar()
		
		print("puntos: ", puntos) 
		Hangman.hangman(Intentos, incognitaGuion)
		print("")
		print("═══════Letras Incorrectas══════════════════════════════════════════")
		print(" ", lista1[0:7])
		print("═══════════════════════════════════════════════════════════════════")
		
				

		if Intentos == 0:
				Perdio= True

		if not Perdio:


			letraMenu = MenuPartida.MenuPartida(palaacer,incognitaSolucion,incognitaGuion)
			

			#Si ingreso la letra
			if letraMenu[0]=='1':
				letra = letraMenu[1]	
				
				#si esta bien la letra se agrega
				if Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion):
				
					incognitaGuion = MeterLetra.MeterLetra(incognitaGuion,letra, Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion))
				
				#Si esta mal se resta el intento y agrega en el historial de fallo la letra
				else:
					Intentos = Intentos-1
					lista1.append(letra)

				print("")
				

			
				
			

			#Si pidio pista
			elif letraMenu[0]=='2':
				letra = letraMenu[1]
				incognitaGuion = MeterLetra.MeterLetra(incognitaGuion,letra, Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion))
				Intentos = Intentos-1


			#Si se ridió
			else:
				Perdio=True

		#Si no hay mas guiones es por que gano
		if incognitaGuion.count("_")==0:
					Gano = True

			
			

	







	if Gano:
		Hangman.hangman(Intentos, incognitaGuion)
		time.sleep(1)
		palaacer.append(incognitaSolucion)
		mensaje_gano()
		input()

		return [True,Intentos],listapalabras,palaacer

	elif Perdio:
		mensaje_predio2()

		print("La respuesta FUE: ",incognitaSolucion)
		return [False,0],listapalabras, palaacer
		










def mensaje_gano():
	print("╔══════════════════════════════════════════════════════════╗")
	print("║                                                          ║")
	print("║       ===>Por Fin te salio algo en la vida :P <===       ║")
	print("║                                                          ║")
	print("╚══════════════════════════════════════════════════════════╝")







def mensaje_predio():
	print("-------------------------------------------------------")
	print("-     Perdiste y si no jugas otra vez sos un ...      -")
	print("-------------------------------------------------------")

def mensaje_predio2():
	for i in range(3):
		print("-------------------------------------------------------")
		print("-     Perdiste y si no jugas otra vez sos un ...      -")
		print("-------------------------------------------------------")
		time.sleep(0.9)
		Limpiar.Limpiar()
		print("")
		print("-     Perdiste y si no jugas otra vez sos un ...      -")
		
		time.sleep(0.9)
		Limpiar.Limpiar()
