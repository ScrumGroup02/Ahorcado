
import PedirLetra
import Limpiar

def imprimir():
	print("")
	print("Elegir opción")
	print("1-Decir Letra")
	print("2-Rendirse")

def humillar():
	print("------------------------------------------")
	print("-      SOS un FRACASADO-----Niño RATA    -")
	print("------------------------------------------")
	print("\tooooo")
	print("\tooooo")
	print("\tooooo")
	print("\t║ ║")
	print("\t╚ ╝")



def MenuPartida():

	imprimir()

	
	opcion=input("")

	while (opcion !='1' and opcion != '2'):
		imprimir()
		opcion=input("")
	
	Limpiar.Limpiar()

	if (opcion=='1'):
		letra = PedirLetra.PedirLetra()
		return[True, letra]


	elif (opcion=='2'):
		humillar()
		return[False]


	print("...")
