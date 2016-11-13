# coding: utf-8
# Um Passo do Algoritmo BubbleSort
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

def buble_step(entrada):
	entrada = entrada.split()
	n_entrada = ""
	for i_ent in range(len(entrada) -1):
		if int(entrada[i_ent]) > int(entrada[i_ent + 1]):
			entrada[i_ent], entrada[i_ent + 1] = entrada[i_ent + 1], entrada[i_ent]
	
	n_entrada += " ".join(entrada)
	lista.append(n_entrada)

lista = []

while True:
	entrada = raw_input()
	if entrada == "fim":
		break
	else:
		buble_step(entrada)			

for elem in lista:
	print elem
