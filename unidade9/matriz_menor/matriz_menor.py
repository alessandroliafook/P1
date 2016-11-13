# coding: utf-8
# Matriz Menor
# (C) 2015, Alessandro Santos, Programação 1

def matriz_menor(m1, m2):
	nova_matriz = []
	for i in range(len(m1)):
		nova_matriz.append([])
		for j in range(len(m1[i])):
			if m1[i][j] >= m2[i][j]:
				nova_matriz[i].append(m2[i][j])
			else: 
				nova_matriz[i].append(m1[i][j])
	return nova_matriz

if __name__ == "__main__":

	M1 = [[1,2,3], [13,14,15], [7,8,9]]

	M2= [[10,11,12], [4,5,6], [7,8,9]]

	M3= [[1,2,3], [0,0,0], [7,8,9]]

	assert matriz_menor(M1, M2) == [[1,2,3],[4,5,6],[7,8,9]]
	assert matriz_menor(M1, M3) == [[1,2,3],[0,0,0],[7,8,9]]
