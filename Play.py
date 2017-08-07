
import DarIncongnita
import PedirLetra
import MeterGuiones
import ImprimirEspaciado
import MeterLetra
import Control_LetraEnPalabra



def play():

	incognitaSolucion = DarIncongnita.DarIncognitaDesdeArchivo()
	incognitaGuion = ""
	incognitaGuion = MeterGuiones.MeterGuiones(incognitaSolucion)


	print(incognitaSolucion)


	Gano = False
	Perdio = False
	Intentos = 5




	while not(Gano) and not(Perdio):

		print("")
		print("")
		ImprimirEspaciado.ImprimirEspaciado(incognitaGuion)
		print("")
		print("")
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


		if Intentos == 0:
			Perdio= True
		if incognitaGuion.count("_")==0:
			Gano = True
			pass


	if Gano:
		print("Ganaste")
		return True
	elif Perdio:
		print("Perdiste")
		return False



