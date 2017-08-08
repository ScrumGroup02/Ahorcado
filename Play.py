
import DarIncongnita
import PedirLetra
import MeterGuiones
import ImprimirEspaciado
import MeterLetra
import Control_LetraEnPalabra
import Hangman



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


	#print(incognitaSolucion)


	Gano = False
	Perdio = False
	Intentos = Intentos




	while not(Gano) and not(Perdio):

		print("")
		print("")
		ImprimirEspaciado.ImprimirEspaciado(incognitaGuion)
		print("")
		Hangman.hangman(Intentos)
		print("Intentos restantes: ", Intentos)
		print("")

		if Intentos == 0:
				Perdio= True

		if not Perdio:

			letra = PedirLetra.PedirLetra()
			print("")
			print("")

			


			

			print("")
			print("")

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
				pass



	if Gano:
		print("Ganaste")
		return [True,Intentos]
	elif Perdio:
		print("Perdiste")
		print(incognitaSolucion)
		return [False,0]
		



