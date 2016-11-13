# coding: utf - 8
# Square Code
# (C) 2015, Alessandro Santos, Programação 1

def transposta(M):
	matriz_transposta = []
	for i in range(len(M[0])):
		matriz_transposta.append([])
	for j in range(len(M)):
		for k in range(len(M[j])):
			matriz_transposta[k].append(M[j][k])
	return matriz_transposta

def square_code(m):
	nova_string = ""
	# remover o que não for letra
	for i in m:
		if i.isalpha() == True:
			nova_string += i
			
	# criar a matrix base
	import math
	matriz_base = []
	num_linhas = int(math.sqrt(len(nova_string)))
	for j in range(num_linhas): 
		matriz_base.append([])

	# preencher a matriz
	a = 0
	num_colunas = int(math.ceil(len(nova_string) / float(num_linhas)))
	for l in matriz_base:
		for m in range(num_colunas):
			if a < len(nova_string):
				l.append(nova_string[a])
				a += 1

	# gerar a string codificada
	matriz_transposta = transposta(matriz_base)
	codigo = ""
	for i_letra in range(len(matriz_transposta)):
		for j_letra in range(len(matriz_transposta[i_letra])):
			codigo += matriz_transposta[i_letra][j_letra]
		if i_letra < len(matriz_transposta) - 1:
			codigo += " "
	return codigo
	

if __name__ == "__main__":

	m = "O tatu virou uma bola!!!"
	assert square_code(m) == "Ovul tima ara tob uuo"

