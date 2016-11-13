# coding: utf-8
# Classificação de Elementos Utilizando a Média dos Extremos
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

n = int(raw_input())

primeiro_numero = int(raw_input())

numeros = [primeiro_numero]

maior = primeiro_numero
menor = primeiro_numero

for i in range(n - 1):
	numero = int(raw_input())
	numeros.append(numero)
	if numero > maior:
		maior = numero
	if numero < menor:
		menor = numero

media = (maior + menor) / 2.0
qnt_maior = 0
qnt_menor = 0

for valor in numeros:
	if valor > media:
		qnt_maior += 1
	if valor < media:
		qnt_menor += 1

print "Menor número: %d" % menor
print "Maior número: %d" % maior
print "Média dos extremos: %.2f" % media
print "%d número(s) abaixo da média" % qnt_menor
print "%d número(s) acima da média" % qnt_maior



