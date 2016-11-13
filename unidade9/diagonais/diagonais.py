# coding: utf - 8
# Diagonais
# (C) 2015, Alessandro Santos, Programação 1


def diagonais(M):
	diagonais = [[], []]
	for i in range(len(M)):
		diagonais[0].append(M[i][0 + i])
		diagonais[1].append(M[i][-1 - i])
	return diagonais


if __name__ == "__main__":

	M = [[1,2,3],
	     [4,5,6],
	     [7,8,9]]
	assert diagonais(M) == [[1,5,9],[3,5,7]]
