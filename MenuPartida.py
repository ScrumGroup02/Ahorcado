
import PedirLetra
import Limpiar
import DarIncongnita
import pista_letra

def imprimir(listapala):
	# print("")
	# print("╔═══════Palabras Acertadas═══════╗")
	# print("║",listapala,"                ║")
	# print("╚════════════════════════════════╝")
	print("")
	print("═══════Palabras Acertadas══════════════════════════════════════════")
	# print(listapala)
	print(listapala[0:5])
	print(listapala[5:10])
	print(listapala[10:15])
	print(listapala[15:20])
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


def MenuPartida(palaacer,incognitaSolucion,incognitaGuion):

	imprimir(palaacer)
	
	opcion=input("")

	while (opcion !='1' and opcion != '2' and opcion != '3'):
		imprimir()
		opcion=input("")
	
	Limpiar.Limpiar()

	if (opcion=='1'):
		letra = PedirLetra.PedirLetra()
		return[True, letra]

	elif (opcion=='2'):
		humillar()
		return[False]
	
	elif (opcion=='3'):
		letra = pista_letra.pista_letra(incognitaSolucion,incognitaGuion)
		return [True,letra]
	
	print("...")
