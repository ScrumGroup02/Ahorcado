import MenuPrincipal
import Limpiar


def portada():

	print("    _    _   _  ___  ____   ____    _    ____   ___  ")
	print("   / \  | | | |/ _ \|  _ \ / ___|  / \  |  _ \ / _ \ ")
	print("  / _ \ | |_| | | | | |_) | |     / _ \ | | | | | | |")
	print(" / ___ \|  _  | |_| |  _ <| |___ / ___ \| |_| | |_| |")
	print("/_/   \_\_| |_|\___/|_| \_\____/_/   \__\____/ \___/ ")



jugando = True

while jugando:
	Limpiar.Limpiar()


	portada()


	jugando = MenuPrincipal.MenuPrincipal()




                                                      

 