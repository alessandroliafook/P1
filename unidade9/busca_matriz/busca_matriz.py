# coding: utf-8
# Busca em Matriz
# (C) 2015, Alessandro Santos, Programação 1

def busca_matriz(m, e):
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == e:
				return i,j

if __name__ == "__main__":

	matriz = [
	    [2, 3, 5, 3, 1],
	    [3, 2, 1, 5, 6],
	    [1, 2, 3, 2, 1],
	]
	assert busca_matriz(matriz, 4) == None
	assert busca_matriz(matriz, 3) == (0,1)
	assert busca_matriz(matriz, 1) == (0,4)
