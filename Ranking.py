import os #para borrar archivo
#___________________________________________________________________

#Formato del archivo del Ranking:
	##################
	# Nombre1$puntos1
	# Nombre2$puntos2
	# Nombre3$puntos3
	# Nombre4$puntos4
	# Nombre5$puntos5
	##################

#Al cargar un archivo, se lo hace como una lista que contiene la cantidad
#de tuplas como de puestos/lineas se quiera tener. //no hay limites de puesto por ahora
#cada tupla va contener -> (nombre,puntuacion)


#Al guardar una nueva puntuacion:
	#primero se carga el ranking del archivo en una lista.
	#se verifica que la nueva puntuación pueda entrar en el ranking // no aplica, no lim de puestos
	#se inserta el elemento en orden.
	#se guarda la lista en un archivo reemplazando el anterior.

#Al verificar Nombre
	#que no contenga signo $   
	#maxima longitud 9 caracteres, minima 4

#___________________________________________________________________




################################################################
#Variables para las funciones
#
#
#
#


#directorio del ranking
Directorio_Rankink_File = './DATA/RANKING'



###############################################################







#____________________________________________________-

#funcion que pedirá el ingreso de un nombre.
def pedir_ingreso_nombre():
	#pedir ingresar el nombre por teclado.

	nombreCorrecto = False

	
	while not nombreCorrecto:
		#pedir nombre y eso.
		nombre = input("Ingrese Nombre: ")
		nombreCorrecto = verificar_nombre(nombre)

		pass



	return nombre
#__________________________________________________


#__________________________________________________

#funcion para verificar que el nombre cumple los requisitos
def verificar_nombre(nombre):
	verificado = False


	nomLongitud = len(nombre)

	if nomLongitud > 4:
		
		if nomLongitud < 10:
			
			if nombre.isalnum():
				
				verificado = True


	#asegurarse que no tenga el simbolo $
	#max long 9

	return verificado#bool
#__________________________________________________



#__________________________________________________
#!!!!!!!!!!!!! hecho por el gato, revisar...
#crea una tupla con nombre y puntuacion
def crear_tupla_nombre_puntos(nombre,puntos):



	tupla_nueva_puntuacion = (nombre,puntos)

	return tupla_nueva_puntuacion
#__________________________________________________




#__________________________________________________
#pasa de una str de la forma "nombre$puntos" a una tupla
# donde tupla = (nombre,puntos)
def line_a_tupla(linea):

	dividido = linea.split("$")

	nombre = dividido[0]
	puntos = int(dividido[1])

	tupla = (nombre,puntos)

	return tupla
#__________________________________________________



#__________________________________________________
#levanta el ranking de un archivo, y lo hace en forma de lista
# que contiene tuplas.
#en caso de fallar, ejecuta CargarRankingFalso()
def CargarRanking():

	#cargararchivo
	#leer lineas
	#dividir cada linea por donde se encuentra el simbolo $
		#lo de la izquiera del $ primer elemento de la tupla
		#lo de la derecha del $ segundo elemento de la tupla
	#cada linea le corresponde una tupla
	#crear una lista con las tuplas.
	
	lista_ranking_con_tuplas = []
	try:
		
		#abriendo archivo para cargar ranking
		archivo = open(Directorio_Rankink_File,'r')

		lineas= archivo.readlines()

		
		for i in lineas:
					
			lista_ranking_con_tuplas.append(line_a_tupla(i))


		archivo.close()



	except:
		print("entrando except")
		lista_ranking_con_tuplas = CargarRankingFalso()

	return lista_ranking_con_tuplas


#una lista de  ranking falso para pruebas, 
# o controlar errores en el verdader0..
#__________________________________________________

#__________________________________________________
def CargarRankingFalso():

	
	tupla1 = ("Ayelén92",20)
	tupla2 = ("Ramona",10)
	tupla3 = ("Laria",9)
	tupla4 = ("Shirn",7)
	tupla5 = ("Sarah",5)

	lista_ranking_con_tuplas = [tupla1,tupla2,tupla3,tupla4,tupla5]

	return lista_ranking_con_tuplas






#ingresa una tupla nombre-puntos a la lista del ranking. (no se guarda en archivo)
#__________________________________________________


#__________________________________________________

#para agragar una nueva tupla nombre puntos a una lista, y que se acomode en el orden q corresponde
def meter_nueva_puntuacion_a_lista(tupla,lista_en_donde_ingresar):

	
	
	a=0
	entro_al_ranking = False
	for elem in lista_en_donde_ingresar:
		if elem[1]<tupla[1]:
			#si se quiere que
			#tenga que pasar la puntuacion
			#del ultimo en el ranking
			#ingresar en esta parte la tupla
			lista_en_donde_ingresar.insert(a,tupla)	
			entro_al_ranking = True
			break
		a=a+1

	#lista_en_donde_ingresar.insert(a,tupla)
	if entro_al_ranking:
		print("ingreso al ranking")
		input("presione enter...")
	else:
		print("no ingreso al ranking")


	return lista_en_donde_ingresar

#__________________________________________________




#__________________________________________________
#guarda la lista del ranking en un archivo.
#cada tupla sera una linea de la forma
	# tupla[0]$tupla[1]\n
def GuardarRanking(lista_a_guardar):

	try:		
		#se borra antiguo ranking
		os.remove(Directorio_Rankink_File)
		#se crea el reemplazo
		archivo = open(Directorio_Rankink_File,'w')
		

		#se guarda las tuplas de las listas
		#como esta especificado en el formato de archivo
		for x in lista_a_guardar:
			
			nombre = x[0]
			punto = str(x[1])
			
			archivo.write(nombre)
			archivo.write("$")
			archivo.write(punto)
			archivo.write("\n")
		

		archivo.close()
		

		todoCorrecto = True #todo correcto, no hubo problemas.
		
	except:
		todoCorrecto = False#no todo correcto, todo mal.
		
	
		


	return todoCorrecto #bool
#__________________________________________________




#__________________________________________________
#Imprime el ranking.
def ImprimirRanking():
	listaRanking = CargarRanking()
	a=1
	print("______________________________")
	print("RANKING DE LOS QUE SABEN JUGAR")
	print("______________________________")
	print()

	for x in listaRanking:
		
		if len(x[0])>=6:
			print(a,"\t",x[0],"\t\t",x[1])
		else:
			print(a,"\t",x[0],"\t\t\t",x[1])


		a = a+1

	print("______________________________")
	pass
#__________________________________________________

