# coding: utf-8
# Série: Sequência de floats
# (C) 2015, Alessandro Fook / UFCG, Programação I

elemento_inicial = 15.2
elemento_final = -5.8

tamanho_lista = ((elemento_final - elemento_inicial) / -1.5) + 1

for x in range(int(tamanho_lista)):
	print "%.1f" % elemento_inicial 
	elemento_inicial = elemento_inicial - 1.5
	

		
