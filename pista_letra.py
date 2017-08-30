
def pista_letra(palabra,incognitaGuion):

	
	au = 0; 
	print(palabra)
	print(incognitaGuion)
	pista="XZXX"
	while au==0 :
		for i in palabra:
			if not i in incognitaGuion:
				print(i)
				pista= i
				au=1
		#	for j in incognitaGuion:
				
				
		#		if palabra.find(j)>-1:
		#			pista= j
		#			print(pista)
		#			input(" ")
		#			au=1
	return pista

