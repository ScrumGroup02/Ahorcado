
import PedirLetra
import Limpiar
import DarIncongnita

def imprimir(listapala):
	# print("")
	# print("╔═══════Palabras Acertadas═══════╗")
	# print("║",listapala,"                ║")
	# print("╚════════════════════════════════╝")
	print("")
	print("═══════Palabras Acertadas══════════════════════════════════════════")
	print(listapala)
	print("═══════════════════════════════════════════════════════════════════")
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



def MenuPartida(palalist):

	imprimir(palalist)

	
	opcion=input("")

	while (opcion !='1' and opcion != '2'):
		imprimir(palalist)
		opcion=input("")
	
	print()

	if (opcion=='1'):
		letra = PedirLetra.PedirLetra()
		return[True, letra]


	elif (opcion=='2'):
		humillar()
		return[False]


	print("...")
