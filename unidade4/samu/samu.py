# coding: utf-8
# Atendimentos no SAMU
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

total_atendimentos = 0
atendimentos_mes = []

for i in range(12):
	atendimentos = int(raw_input())
	total_atendimentos += atendimentos
	atendimentos_mes.append(atendimentos)

media_atendimentos = total_atendimentos / 12.0

print "Média mensal de atendimentos: %.2f" % media_atendimentos
print "----"

for mes in range(len(atendimentos_mes)):
	if atendimentos_mes[mes] > media_atendimentos:
		print "Mês %d: %d" % (mes + 1, atendimentos_mes[mes])




