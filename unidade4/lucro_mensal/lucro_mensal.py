# coding: utf-8
# Lucro Mensal de uma Empresa
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', \
	'ago', 'set', 'out', 'nov', 'dez']

receitas = []
despesas = []

for mes in range(12):
	receita, despesa = raw_input().split()
	receitas.append(float(receita))
	despesas.append(float(despesa))

for i in range(12):
	print "%s %4.1f" % (meses[i], receitas[i] - despesas[i])




