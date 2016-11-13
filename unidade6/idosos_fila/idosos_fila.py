# coding: utf-8
# Idosos Fila | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

def idosos_inicio(fila):
	contador = 0
	for indice in range(len(fila)):
		if fila[indice] >= 60:
			fila[contador], fila[indice] = fila[indice], fila[contador]
			contador += 1

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)


