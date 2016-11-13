# coding: utf-8
# Maior Diferença Absoluta
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

n = int(raw_input())
numeros = []

for i in range(n):
	numero = float(raw_input())
	numeros.append(numero)

maior_diferenca = -1
numeros_maior_abs = []

for k in range(n):
	if k + 1 == n:
		break
	elif abs(numeros[k] - numeros[k + 1]) > maior_diferenca:
		maior_diferenca = abs(numeros[k] - numeros[k + 1])
		numeros_maior_abs = [numeros[k], numeros[k + 1]]

print "%.1f e %.1f" % (numeros_maior_abs[0], numeros_maior_abs[1])
