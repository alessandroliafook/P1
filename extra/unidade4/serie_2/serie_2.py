# coding: utf-8
# Série (Ímpares 2)
# (C) 2015, Alessandro Fook / UFCG, Programação I

for i in range(102):
	if i % 2 == 1:
		if i % 7 == 0:			
			print '*,',
		elif (i - 7) % 10 == 0:	
			print '*,',
		elif i == 101:
			print "%d" % i, 
		else:
			print "%d," % i, 

			
