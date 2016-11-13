# coding: utf-8
# Conta Palavras | UFCG - PROGRAMAÇÃO 1
# (C) | Alessandro Santos, 2015

def conta_palavras(k, palavras):
	maiores_k = 0
	lista_palavras = palavras.split(":")

	for palavra in lista_palavras:
		if len(palavra) >= k:
			maiores_k += 1

	return maiores_k

if __name__ == "__main__":
	assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") == 2
		
