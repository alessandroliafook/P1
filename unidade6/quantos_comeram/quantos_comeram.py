# coding: utf-8
# Quantos Comeram? | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

def quantos_comeram(n, fila):
	servidas = 0
	for pedido in fila:
		if n - pedido >= 0:
			n = n - pedido
			servidas += pedido
		else:
			break
	return servidas



