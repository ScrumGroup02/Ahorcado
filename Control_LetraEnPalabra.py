# La funcion devuelve una lista con las posiciones en que se 
# encuentra la letra en una palabra.

# como en python las listas vacias tienen valor booleano false
# y las listas con elementos valor true. 
# Se puede usar la lista que devuelve la funcion para saber
# si no se encuentra la letra en la palabra.

def Control_LetraEnPalabra(letra, palabra):

	listaPosiciones=[]
	
	a = 0; 

	for i in palabra:
		
		if i==letra:
			listaPosiciones.append(a) #se agrega la posicion de la letra a la lista
		a = a+1

	return listaPosiciones