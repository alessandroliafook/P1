# coding: utf-8
# Zera Diagonal
# (C) 2015, Alessandro Santos, Programação 1

def zera_diagonal(M):
	for i in range(len(M)):
		M[i][0+i] = 0

if __name__ == "__main__":

	m = [[8, 20, -7],
	     [ 5, 1,  3],
	     [ 6,  7, 9]]

	zera_diagonal(m)
	assert  m == [[0, 20, -7], [5, 0, 3], [6, 7, 0]]


