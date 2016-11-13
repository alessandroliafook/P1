#coding: utf-8
# Eh Palíndromo | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

frase = raw_input()
frase_c = ""
frase_i = ""

for indice in range(len(frase) -1, -1, -1):
	if frase[indice] != " ":
		frase_i += frase[indice]	

for letra in frase:
	if letra != " ":
		frase_c += letra

if frase_c.lower() == frase_i.lower():
	print "%s é palíndromo" % frase

else:
	print "%s não é palíndromo" % frase

