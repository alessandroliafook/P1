# coding: utf-8
# Soma e Diminui Vizinhos! | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)
# commit 2

def soma_diminui_vizinhos(lista):
	soma = 0
	if lista != []:
		soma = lista[0]
		for index in range(1, len(lista)):
			if index % 2 == 1:
				soma += lista[index]
			else:
				soma -= lista[index]
	return soma

lista = [1,2,3]
assert soma_diminui_vizinhos(lista) == 0
