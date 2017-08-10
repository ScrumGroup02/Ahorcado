
import DarIncongnita

import MeterGuiones
import ImprimirEspaciado
import MeterLetra
import Control_LetraEnPalabra
import Hangman
import MenuPartida

import Limpiar


def play():

	jugando = True
	Intentos = 5
	jugando= [True,Intentos]

	while jugando[0]:
		
		jugando = playMatch(jugando[1])
		
	

	pass




def playMatch(Intentos):

	incognitaSolucion = DarIncongnita.DarIncognitaDesdeArchivo()
	incognitaGuion = ""
	incognitaGuion = MeterGuiones.MeterGuiones(incognitaSolucion)



	Gano = False
	Perdio = False
	Intentos = Intentos




	while not(Gano) and not(Perdio):

		Limpiar.Limpiar()
		
		Hangman.hangman(Intentos)
		
		print("")
		ImprimirEspaciado.ImprimirEspaciado(incognitaGuion)
		
		

		if Intentos == 0:
				Perdio= True

		if not Perdio:


			letraMenu = MenuPartida.MenuPartida()
			
			if letraMenu[0]:
				letra = letraMenu[1]

				if Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion):
				
					incognitaGuion = MeterLetra.MeterLetra(incognitaGuion,letra, Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion))
				else:
					Intentos = Intentos-1

				print("")
				print("")
				ImprimirEspaciado.ImprimirEspaciado(incognitaGuion)

				print(Control_LetraEnPalabra.Control_LetraEnPalabra(letra,incognitaSolucion))


			
				if incognitaGuion.count("_")==0:
					Gano = True
					



			else:
				Perdio=True

			
			

			



	if Gano:
		print("╔══════════════════════════════════════════════════════════╗")
		print("║                                                          ║")
		print("║       Ganaste---Por Fin te salio algo en la vida :P      ║")
		print("║                                                          ║")
		print("╚══════════════════════════════════════════════════════════╝")
		input()

		return [True,Intentos]
	elif Perdio:
		print("-------------------------------------------------------")
		print("-     Perdiste y si no jugas otra vez sos una NENA    -")
		print("-------------------------------------------------------")

		print(incognitaSolucion)
		return [False,0]
		



