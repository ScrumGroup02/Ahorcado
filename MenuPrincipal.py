# Que se impriman las opciones de:

# Jugar

# Salir

# Y que el jugador pueda ingresar una opción.

# Luego que:
# Si se eligió uno, que avance a una función Play() //Por ahora no haga nada la funcion esa o solo imprima "jugando"..
# Si se eligió salir, que se termine la ejecución del programa.
import Play
import Limpiar
import time 
import os
import Ranking
import Beep


def imprimir_menu():

	print("╔══════════════════════════════╗")
	print("║          1-Jugar             ║")
	print("║          2-Ranking           ║")
	print("║          3-Salir             ║")
	print("╚══════════════════════════════╝")
	if(os.name=="nt"):
		os.system('color 3')

def despedir():
	print("╔══════════════════╗")
	print("║  Hasta luego. . .║")
	print("╚══════════════════╝")
 

	print("  ╔ ╗")
	print("  ║║║")
	print("ooooo")
	print("ooooo")
	print("ooooo")
	time.sleep(0.8)
	Limpiar.Limpiar()

	for i in range(5):
		print(" ( ¨ ¨ )┐")
		print("└(  O  ) ")
		time.sleep(0.3)
		Limpiar.Limpiar()
		print(" ( ¨ ¨ )┘")
		print("┌( \=/ ) ")
		time.sleep(0.3)
		Limpiar.Limpiar()





def MenuPrincipal():

	imprimir_menu()

	opcion=input("")

	Beep.Beep()

	while (opcion !='1' and opcion != '2' and opcion != '3'):
		print("==>Por Favor eliga opción 1 o 2<==")
		
		opcion=input("")
		Beep.Beep()
	

	Limpiar.Limpiar()
	
	
	if (opcion=='1'):
		Play.play()
		time.sleep(3)
		return True

	elif (opcion=='2'):
		Limpiar.Limpiar()
		Ranking.ImprimirRanking()
		input("presione enter para volver...")
		return True

	elif (opcion=='3'):
		despedir()
		return False
		




