# coding: utf-8
# Número Perfeito
# (C) 2015, Alessandro Fook / UFCG, Programação I

numero = int(raw_input())

soma = 0

for divisor in range(1, numero):
	if numero % divisor == 0:
		soma += divisor

if soma == numero:
	print "%d é um número perfeito." % numero
else:
	print "%d não é um número perfeito." % numero
