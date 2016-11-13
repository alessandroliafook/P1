# coding: utf-8
# Converte Senha
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

palavra = raw_input()
senha = palavra[0]
troca = 0

for letra in range(1, len(palavra)):
	if palavra[letra] in "aA":
		senha += "4"
		troca += 1	
	elif palavra[letra] in "eE":
		senha += "3"
		troca += 1
	elif palavra[letra] in "iI":
		senha += "1"
		troca += 1
	elif palavra[letra] in "oO":
		senha += "0"
		troca += 1
	else:
		senha += palavra[letra]

print "%s (%d troca(s))" % (senha, troca)
