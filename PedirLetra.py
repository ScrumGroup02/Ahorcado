

#
#Imprime mensaje pidiendo al usuario una letra.
#Luego devuelve la letra q el usuario ingreso.
#
#no deja: no poner ninguna letra o mas una.

def PedirLetra():

	a = "aa"
	while len(a) != 1:
		print("")
		print("")
		a = input("Ingrese Una Letra: ")
		
	return a.upper()