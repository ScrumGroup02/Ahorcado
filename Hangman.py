# open(nombre,modo)
#----------------------------------------------------

#recordar hacer en la consola de CMD "pip install ipdb"
#----------------------------------
def hangman(Intentos):
	
	if Intentos == 5:
		print("(̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅()")
		print("█         |")
		print("█         |")
		print("█  ")
		print("█   ")
		print("█ ")
		print("█ ")
		print("█  ")
		print("█  ")
		print("█")
		print("█")
		print("█")
		print("█")
		print("█")
		print("██████████████████████████")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 4:
		print("(̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅()")
		print("█        |")
		print("█        |")
		print("█      (̲̅̅●̲̲̅̅̅̅=̲̲̅̅̅̅●̲̅̅)")
		print("█   ")
		print("█ ")
		print("█  ")
		print("█  ")
		print("█  ")
		print("█")
		print("█")
		print("█")
		print("█")
		print("█")
		print("██████████████████████████")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 3:
		print("(̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅()")
		print("█        |")
		print("█        |")
		print("█      (̲̅̅●̲̲̅̅̅̅=̲̲̅̅̅̅●̲̅̅)")
		print("█        ║  ")
		print("█        ║")
		print("█        ║ ")
		print("█ ")
		print("█ ")
		print("█")
		print("█")
		print("█")
		print("█")
		print("█")
		print("██████████████████████████")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 2:
		print("(̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅()")
		print("█        |")
		print("█        |")
		print("█      (̲̅̅●̲̲̅̅̅̅=̲̲̅̅̅̅●̲̅̅)")
		print("█       /║\ ")
		print("█      / ║ \     ")
		print("█        ║ ")
		print("█ ")
		print("█ ")
		print("█")
		print("█")
		print("█")
		print("█")
		print("█")
		print("██████████████████████████")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 1:
		print("(̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅()")
		print("█        |")
		print("█        |")
		print("█     \(̲̅̅●̲̲̅̅̅̅=̲̲̅̅̅̅●̲̅̅)   hi")
		print("█      \/║\ ")
		print("█        ║ \  ")
		print("█        ║ ")
		print("█       / \ ")
		print("█      /   \ ")
		print("█")
		print("█")
		print("█")
		print("█")
		print("█")
		print("██████████████████████████")
		print("Intentos restantes: ", Intentos)
	elif Intentos == 0:
		print("(̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅_̅_̅̅()")
		print("█        |")
		print("█        |")
		print("█       (̲̅xx)  dwaaaughhh")
		print("█       /║\ ")
		print("█      / ║ \       YOU DIE!!!")
		print("█        ║  ")
		print("█       / \ ")
		print("█      /   \ ")
		print("█")
		print("█")
		print("█")
		print("█")
		print("█")
		print("██████████████████████████")
		print("Intentos restantes: ", Intentos)

