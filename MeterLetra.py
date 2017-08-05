def MeterLetra(palabraConGuion, letra, listaPosiciones):



	guionesreemplazados = ""

	for i in range(len(palabraConGuion)):

	
		if listaPosiciones.count(i)==1:
			guionesreemplazados = guionesreemplazados + letra
		else:
			guionesreemplazados = guionesreemplazados + palabraConGuion[i]




	return guionesreemplazados
