#coding: utf-8
# Esteira em uma Linha de Produção de uma Fábrica
# 2015, (C), Alessandro Santos, Programação 1

def verifica_esteira(l1,l2):
	coincidencias = 0
	indice = 0
	for i_componente in range(len(l2)):
		for i_busca in range(indice, len(l1)):
			if l1[i_busca] == l2[i_componente]:
				coincidencias += 1
				indice = i_busca
				break
	if coincidencias == len(l2):
		return True
	else:
		return False

if __name__ == "__main__":
	l1 = [2,1,3,4]
	l2 = [2]
	assert verifica_esteira(l1,l2)
	assert l1 == [2,1,3,4]
	assert l2 == [2]

	l1 = [1,3,4]
	l2 = [4,1]
	assert not verifica_esteira(l1,l2)
	assert l1 == [1,3,4]


