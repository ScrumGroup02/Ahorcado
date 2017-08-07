import random


def DarIncognita():




	return "INFORMATORIO"
	
	



def DarIncognitaDesdeArchivo():


	archivo = open('./DATA/PALABRAS/PALABRAS', 'r')

	palabras = []

	for x in archivo:
		palabra = ""
		for y in x:
			if y!='\n':
				palabra = palabra + y
		palabras.append(palabra)



	

	return palabras[random.randint(0,len(palabras)-1)]


