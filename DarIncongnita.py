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

	return palabras


def SeleccionPalabra(palabras):

	palabra=random.choice(palabras)
	palabras.remove(palabra)
	return palabra,palabras
