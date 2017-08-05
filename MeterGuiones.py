def MeterGuiones(palabra):
	
	cantLetras = len(palabra)

	guiones = ""

	for x in range(cantLetras):
		guiones = guiones + "_"

	return guiones
