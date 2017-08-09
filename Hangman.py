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
		print("____________________")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 4:
		print("______ ")
		print("|  |")
		print("|  ")
		print("|  ")
		print("| ")
		print("|")
		print("|") 
		print("____________________")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 3:
		print("______ ")
		print("|  |")
		print("|  0")
		print("|  ")
		print("| ")
		print("|")
		print("|") 
		print("____________________")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 2:
		print("______ ")
		print("|  |")
		print("|  0")
		print("|  | ")
		print("| ")
		print("|")
		print("|") 
		print("____________________")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 1:
		print("______ ")
		print("|  |")
		print("|  0")
		print("| /|\ ")
		print("| ")
		print("|")
		print("|") 
		print("____________________")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 0:
		print("______ ")
		print("|  |")
		print("|  0")
		print("| /|\ ")
		print("| / \     YOU DIE!!!")
		print("|")
		print("|") 
		print("____________________")
		print("Intentos restantes: ", Intentos)

