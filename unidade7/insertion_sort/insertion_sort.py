# coding: utf-8
# Insertion Sort
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1


def insertion_sort(numeros):
	for i_numeros in range(1, len(numeros)):
		for i_2_numeros in range(i_numeros):
			if numeros[i_numeros] <= numeros[i_2_numeros]:
				numeros.insert(i_2_numeros, numeros.pop(i_numeros))
				break

numeros = [6, 3, 7, 9, 1, 0]
insertion_sort(numeros)
print numeros
assert numeros == [0, 1, 3, 6, 7, 9]
