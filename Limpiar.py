import os


def Limpiar():
	
	sistema = os.name


	if(sistema=="posix"):
		os.system ("clear")
	elif(sistema=="nt"):
		os.system ("cls")