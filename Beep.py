import os

def Beep():
	
	sistema = os.name

	if(sistema=="nt"):
		import winsound
		winsound.Beep(500, 100)
	