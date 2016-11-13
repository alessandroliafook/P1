# coding: utf - 8
# Zera não-nulos!
# (C) 2015, Alessandro Santos, Programação 1

def zera_nao_nulos(m, lin, col):

	# alterar linha para esquerda
	for i in range(col, -1, -1):
		if m[lin][i] == 0:
			break
		else:
			m[lin][i] = 0

	# alterar linha para direita
	for j in range(col + 1, len(m[lin])):
		if m[lin][j] == 0:
			break
		else:
			m[lin][j] = 0


	# alterar coluna para cima
	for k in range(lin -1, -1, -1):
		if m[k][col] == 0:
			break
		else:
			m[k][col] = 0

	# altera coluna para baixo

	for l in range(lin + 1, len(m)):
		if m[l][col] == 0:
			break
		else:
			m[l][col] = 0


if __name__ == "__main__":
	jogo = [
	    [1, 1, 1, 1, 1, 1],
	    [1, 0, 0, 0, 1, 1],
	    [1, 1, 1, 1, 1, 1],
	    [1, 1, 1, 1, 1, 1],
	    [1, 1, 1, 1, 1, 1],
	    [1, 1, 1, 1, 1, 1],
	]    

	zera_nao_nulos(jogo, 3, 2)
	assert jogo == [
	    [1, 1, 1, 1, 1, 1],
	    [1, 0, 0, 0, 1, 1],
	    [1, 1, 0, 1, 1, 1],
	    [0, 0, 0, 0, 0, 0],
	    [1, 1, 0, 1, 1, 1],
	    [1, 1, 0, 1, 1, 1],
	] 
