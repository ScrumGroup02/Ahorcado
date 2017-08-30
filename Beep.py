import os

def Beep():
	
	sistema = os.name
	if(sistema=="posix"):
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( a, b))
		print("Tenes linux sin funcion de sonido gil")
	elif(sistema=="nt"):
		import winsound
		winsound.Beep(500, 100)
		



