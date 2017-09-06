import random


# def DarIncognita():




# 	return "INFORMATORIO"
	
	



def DarIncognitaDesdeArchivo():#No es eficiente, utilizar metodo readlines. 


	archivo = open('./DATA/PALABRAS/PALABRAS', 'r')

	palabras = []
	
	for x in archivo:
		palabra = ""
		for y in x:
			if y!='\n':
				palabra = palabra + y
				
		palabras.append(palabra)

	#palabras=archivo.readlines()

	return palabras#Lista de palabras creada desde archivo de palabras.


def SeleccionPalabra(palabras):#Sortea una palabra y a la vez la saca de la lista de sorteo .

	palabra=random.choice(palabras)#Elige una palabra de la lista creada anteriormente.
	palabras.remove(palabra)
	return palabra,palabras