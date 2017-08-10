# Imprimir menu:
# 1.Decir Letra
# 2. Rendirse

# si se elige decir letra, que ejecute una función DecirLetra() 
# //por ahora esa funcion solo imprima "diciendo letra" Después se la va reemplazar por la función correspondiente.
# Si se elige Rendirse, que ejecute otra funcion Rendirse() 
# //por ahora esa funcion solo imprima "rindiendose" Después se la va reemplazar por la función correspondiente.
import PedirLetra

def imprimir():
	print("")
	print("")
	print("Elegir opción")
	print("1-Decir Letra")
	print("2-Rendirse")

def humillar():
	print("------------------------------------------")
	print("-      SOS un FRACASADO-----Niño RATA    -")
	print("------------------------------------------")


def MenuPartida():

	imprimir()

	
	opcion=input("")

	while (opcion !='1' and opcion != '2'):
		imprimir()
		opcion=input("")
	

	if (opcion=='1'):
		letra = PedirLetra.PedirLetra()
		return[True, letra]


	elif (opcion=='2'):
		humillar()
		return[False]


	print("...")
