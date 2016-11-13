# coding: utf-8
# Percentual de Alunos Aprovados
# (C) 2015, Alessandro Fook / UFCG, Programação I

n = int(raw_input())

notas = []

for numero_alunos in range(n):
	notas.append(raw_input())

aprovados = []
reprovados = []

for resultado in notas:
	if resultado == "F":
		reprovados.append(resultado)
	elif float(resultado) < 5.0:
		reprovados.append(resultado)
	else:	
		aprovados.append(resultado)

percentual_aprovados = 100 * int(len(aprovados)) / n

print "%d%% (%d/%d) de aprovados" % (percentual_aprovados, len(aprovados), n)
