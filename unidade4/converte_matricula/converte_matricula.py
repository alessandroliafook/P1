# coding: utf-8
# Conversão de Matrículas na UFCG
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

mat_antiga = raw_input()

mat_nova = ""

for numero in range(len(mat_antiga)):
	if numero == 0:
		mat_nova += "1"

	elif numero == 5:
		mat_nova += "0" + mat_antiga [numero]	

	else:
		mat_nova += mat_antiga [numero]

print mat_nova
