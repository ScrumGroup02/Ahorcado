# open(nombre,modo)
#----------------------------------------------------

#recordar hacer en la consola de CMD "pip install ipdb"
#----------------------------------
def hangman(Intentos):
	
	if Intentos == 5:
		print("______ ")
		print("|  ")
		print("|  ")
		print("|  ")
		print("| ")
		print("|")
		print("|") 
		print("____________________'esto.es.un.piso'")
	elif Intentos == 4:
		print("______ ")
		print("|  |")
		print("|  ")
		print("|  ")
		print("| ")
		print("|")
		print("|") 
		print("____________________'esto.es.un.piso'")
	elif Intentos == 3:
		print("______ ")
		print("|  |")
		print("|  0")
		print("|  ")
		print("| ")
		print("|")
		print("|") 
		print("____________________'esto.es.un.piso'")
	elif Intentos == 2:
		print("______ ")
		print("|  |")
		print("|  0")
		print("|  | ")
		print("| ")
		print("|")
		print("|") 
		print("____________________'esto.es.un.piso'")
	elif Intentos == 1:
		print("______ ")
		print("|  |")
		print("|  0")
		print("| /|\ ")
		print("| ")
		print("|")
		print("|") 
		print("____________________'esto.es.un.piso'")
	elif Intentos == 0:
		print("______ ")
		print("|  |")
		print("|  0")
		print("| /|\ ")
		print("| / \     YOU DIE!!!")
		print("|")
		print("|") 
		print("____________________'esto.es.un.piso'")

