# open(nombre,modo)
#----------------------------------------------------
import os
import ipdb
#recordar hacer en la consola de CMD "pip install ipdb"
def crea_archivo():
# Crear un archivo
	archivo = open("palabras.txt","w")
	archivo.close()
#----------------------------------
def escribir_archivo(palabra):
# Escribir en un archivo
	archivo = open("palabras.txt","a")
	archivo.write(palabra+"\n")
#----------------------------------
def largo():
	#print(len(palabra))
	archivo = open("palabras.txt","r")
	lineas = archivo.readlines()
	for i in lineas:
		print(len(i)-1)
#----------------------------------
def leer_archivo():
# Leer desde un archivo
	archivo = open("palabras.txt","r")
	lineas = archivo.readlines()
	print()
	for i in lineas:
		print(i)
#----------------------------------
def eliminar_archivo():
	os.remove("palabras.txt")

#ipdb.set_trace()   DEBUGGER
os.system("cls")
#----------------------------------#----------------------------------
crea_archivo()

print("Ingrese cantidad de palabras a ingresar:  ")
for i in range(3):
	print("__________________________________________")
	print("Ingrese la ",i+1 , " palabra:")
	palabra = input("Palabra: ")
	escribir_archivo(palabra)
print("______________________________________________________________","\n")

print("Las palabras cargadas son: ")	
leer_archivo()
print("-------------------")
print("La longitud de las palabras es: ")
largo()
#print("La longitud de la palabra es: ")
#largo(palabra)

input(" ")
