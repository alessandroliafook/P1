# coding: utf-8
# Bolsa do CNPQ
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1
#

mes = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", \
	"nov", "dez"]
indice_mes = 0

gastos = []
saldo_acumulado = 0
saldo_maior = 0

for entrada in range(12):
	consumo = int(raw_input())
	gastos.append(consumo)

for indice_gastos in range(len(gastos)):
	saldo_acumulado += 500 - gastos[indice_gastos]
	if saldo_acumulado >= saldo_maior:
		saldo_maior = saldo_acumulado
		indice_mes = indice_gastos

print mes[indice_mes]

