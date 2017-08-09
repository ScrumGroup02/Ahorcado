# Que se impriman las opciones de:

# Jugar

# Salir

# Y que el jugador pueda ingresar una opción.

# Luego que:
# Si se eligió uno, que avance a una función Play() //Por ahora no haga nada la funcion esa o solo imprima "jugando"..
# Si se eligió salir, que se termine la ejecución del programa.
import Play


def MenuPrincipal():

	print("--------------------------------")
	print("-          1-Jugar             -")
	print("-          2-Salir             -")
	print("--------------------------------")
	
	opcion=int(input(""))

	while (opcion !=1 and opcion != 2):
		print("Por Favor eliga opción 1 o 2")
		
		opcion=int(input(""))
	pass
	
	if (opcion==1):
		Play.play()

	elif (opcion==2):
		print("Hasta luego. . .")

	print("...")


