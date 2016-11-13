# coding: utf-8
# Análise de Variação do Salário Mínimo
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

ano_ini = int(raw_input())
ano_fin = int(raw_input())
total_anos = ano_fin + 1 - ano_ini
anos_maiores = 0
anos_menores = 0
soma_maiores = 0
soma_menores = 0

for i in range(total_anos):
	salario = float(raw_input())
	if salario <= 100.00:
		anos_menores += 1
		soma_menores += salario
	elif salario > 100:
		anos_maiores += 1
		soma_maiores += salario

if anos_menores == 0:
	perc_menores = 0
	print "%d ano(s) abaixo (%d%% dos anos)" % (anos_menores, \
	perc_menores)

else:
	media_menor = soma_menores / anos_menores	
	perc_menores = (anos_menores * 100) / total_anos
	print "%d ano(s) abaixo (%d%% dos anos)" % (anos_menores, \
	perc_menores)	
	print "média dos anos abaixo: U$ %.2f" % (media_menor)

if anos_maiores == 0:
	print "%d ano(s) acima (0.00%% dos anos)" % (anos_maiores)

else:
	media_maior = soma_maiores / anos_maiores	
	perc_maiores = 100 - perc_menores
	print "%d ano(s) acima (%d%% dos anos)" % (anos_maiores, \
	perc_maiores)	
	print "média dos anos acima: U$ %.2f" % (media_maior)



















