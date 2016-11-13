# coding: utf-8
# Complemento Excesso Original
# (C) / 2015, Alessandro Santos / UFCG - PROGARMAÇÃO I

def excesso_127(numero):
	return "{0:b}".format(numero+127)

def complemento1(numero):
	return	

binarios = []

while True:
	entrada = raw_input()
	if "*" in entrada:
		break
	representacao, valor = entrada.split()
	numero = int(valor)
	if representacao == "C1" and numero >= -127 and numero <= 128:
		binarios.append(complement1(numero))
	elif representacao == "E127" and numero >= -127 and numero <= 128:
		binarios.append(excesso_127(numero))

for binario in binarios:
	print "{:0>8}".format(binario)
