# coding: utf - 8
# Labir Move Direita
# (C) 2015, Alessandro Santos, Programação 1


def move_direita(lab):
	for i in range(len(lab)):
		for j in range(len(lab[i])):
			if j+1 < len(lab[i]) and lab[i][j] == "*" and \
			   lab[i][j + 1] == " ":
				lab[i][j], lab[i][j+1] = lab[i][j+1], lab[i][j]
				return i, j+1
			elif lab[i][j] == "*":
				return i, j
				
			

if __name__ == "__main__":

	labirinto1 = [
	  ['P', '*', ' ', ' '],
	  ['P', ' ', 'P', ' '],
	  ['P', 'P', 'P', ' '],
	]
	assert move_direita(labirinto1) == (0, 2)

	assert labirinto1 ==  [
	  ['P', ' ', '*', ' '],
	  ['P', ' ', 'P', ' '],
	  ['P', 'P', 'P', ' '],
	]

	labirinto2 = [
	  ['P', 'P', ' ', ' '],
	  ['P', '*', 'P', ' '],
	  ['P', 'P', 'P', ' '],
	]
	assert move_direita(labirinto2) == (1, 1)
