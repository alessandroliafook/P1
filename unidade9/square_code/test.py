def nova_string(m):
	nova_string = ""

	for i in m:
		if i.isalpha() == True:
			nova_string += i
	import math
	matriz_base = []
	num_linhas = int(math.sqrt(len(nova_string)))
	for j in range(num_linhas): 
		matriz_base.append([])

	num_colunas = int(math.ceil(len(nova_string) / float(num_linhas)))
	a = 0
	for l in matriz_base:
		for m in range(num_colunas):
			if a < len(nova_string):
				l.append(nova_string[a])
				a += 1
		

	print matriz_base

	codigo = ""
	for i_letra in range(len(matriz_base)):
		for j_letra in range(len(matriz_base[i_letra])):
			codigo += matriz_base[i_letra][j_letra]
		if i_letra < len(matriz_base) - 2:
			codigo += " "
	print codigo

if __name__ == "__main__":
	nova_string("O tatu virou uma bola!!!")
	nova_string("12 ab")
	nova_string("ab!!! ")
	nova_string("a b")
	nova_string("a 123 b")
