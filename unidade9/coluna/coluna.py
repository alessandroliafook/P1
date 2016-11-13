# coding: utf - 8
# Coluna
# (C) 2015, Alessandro Santos, Programação 1

def coluna(matriz, i):
	valores = []
	for j in range(len(matriz)):
		valores.append(matriz[j][i])
	return valores


if __name__ == "__main__":
	M = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
	assert coluna(M,0) == [1,2,3]
	assert coluna(M,1) == [1,2,3]
	assert coluna(M,2) == [1,2,3]
	assert coluna(M,3) == [1,2,3]
	
