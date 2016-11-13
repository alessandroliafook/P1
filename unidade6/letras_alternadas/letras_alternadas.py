# coding: utf-8
# Letras Alternadas | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

def letras_alternadas(string):
	nova_string = ""	
	for letra in range(0, len(string), 2):
		nova_string += string[letra]
	return nova_string


