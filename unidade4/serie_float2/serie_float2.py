# coding: utf-8
# Série: Uma nova série com floats
# (C) 2015, Alessandro Fook / UFCG, Programação I

elemento_inicial = 4.0
elemento_final = 103.5

for x in range(200):
	print "%.1f" % elemento_inicial ,
	elemento_inicial = elemento_inicial + 0.5
