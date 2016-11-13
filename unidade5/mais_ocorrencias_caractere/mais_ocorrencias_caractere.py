#coding: utf-8
# Mais Ocorrências Caractere | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

lista = []

while True:
	palavra = raw_input()
	if palavra == "fim":
		break
	lista.append(palavra)

caractere = raw_input()
ocorrencia = int(raw_input())
condicao = False

for palavra in lista:
	num_caractere = 0
	for letra in palavra:
		if letra == caractere:
			num_caractere += 1
	if num_caractere > ocorrencia:
		condicao = True
		print palavra

if condicao == False:
	print "Nenhuma palavra encontrada."
