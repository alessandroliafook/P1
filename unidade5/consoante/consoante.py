#coding: utf-8
# Palavras que Começam com Consoantes | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)


consoantes = 0

while True:
	palavra = raw_input()
	if palavra[0].isalpha() and palavra[0] not in "AaEeIiOoUu":
		consoantes += 1	
	if palavra == "***":
		break

print "Palavras: %d" % consoantes
