# coding: utf-8
# Filtrando Elementos em uma Lista
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

def filtra_lista(num, lista):
	nova_lista = [lista[0]]
	for i_lista in range(1,len(lista)):
		if i_lista % num == 0:
			nova_lista.append(lista[i_lista])
	return nova_lista

if __name__ == "__main__":
	lista1 = [0,1,2,3,4,5,6]
	lista2 = [2,3,5,7,11,13,17]
	assert filtra_lista(2, lista1) == [0,2,4,6]
	assert filtra_lista(3, lista1) == [0,3,6]
	assert filtra_lista(4, lista2) == [2,11]
	assert filtra_lista(40, lista2) == [2]

