# coding: utf - 8
# Transposta
# (C) 2015, Alessandro Santos, Programação 1

def transposta(M):
	matriz_transposta = []
	for i in range(len(M[0])):
		matriz_transposta.append([])
	for j in range(len(M)):
		for k in range(len(M[j])):
			matriz_transposta[k].append(M[j][k])
	return matriz_transposta
			

if __name__ == "__main__":

	M = [[1,1,1,1], [2,2,2,2], [3,3,3,3]]
	assert transposta(M) == [[1,2,3], [1,2,3], [1,2,3], [1,2,3]]
	assert M == [[1,1,1,1], [2,2,2,2], [3,3,3,3]]
