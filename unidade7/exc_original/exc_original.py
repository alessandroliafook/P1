# coding: utf-8
# Filtrando Elementos em uma Lista
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1


def complemento1(numero):
	return numero

def excesso_127(numero):
	return numero

binarios = []

while True:
	entrada = raw_input()
	if "*" in entrada:
		break
	notacao, numero = entrada.split()	
	if int(numero) <= 127 or int(numero) >= -128:
		if notacao == "E127":
			binarios.append(excesso_127(numero))
		elif notacao == "C1":
			binarios.append(complemento1(numero))

for binario in binarios:
	print binario 
