# coding: utf-8
# Inverte dois a dois | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015 (C)

def inverte2a2(seq):
	for indice in range(1, len(seq), 2):
		seq[indice - 1], seq[indice] = seq[indice], seq[indice - 1]
