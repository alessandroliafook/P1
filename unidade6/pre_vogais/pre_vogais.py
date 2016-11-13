# coding: utf-8
# Pré-vogais | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

def pre_vogais(palavra):
	lista = []	
	for letra in range(len(palavra)):
		if palavra[letra].lower() in "aeiou" and letra - 1 >= 0 \
		and palavra[letra -1].lower() not in lista:
			lista.append(palavra[letra -1].lower())
	return lista


