# coding: utf-8
# Inverte dois a dois condicional | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

def inverte2a2_condicional(seq):
	for indice in range(1, len(seq), 2):
		if seq[indice - 1] > seq[indice]:
			seq[indice - 1], seq[indice] = seq[indice], seq[indice - 1]


if __name__ == "__main__":

	seq = [3,1,2,3,10,5,6]
	print seq
	inverte2a2_condicional(seq)
	print seq
	assert seq == [1,3,2,3,5,10,6]

	seq = [5,4,3,2,1]
	print seq
	inverte2a2_condicional(seq)
	print seq
	assert seq == [4,5,2,3,1]


