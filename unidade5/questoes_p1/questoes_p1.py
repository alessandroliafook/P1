# coding: utf-8
# Questões para P1 | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

colaboradores = []
total_questoes = []
total = 0

while True:
	colaborador = raw_input()
	if colaborador == "**":
		break
	colaboradores.append(colaborador)
	soma = 0
	while True:
		questoes = raw_input()
		if questoes == "*":
			break
		soma += int(questoes)
	total_questoes.append(soma)

print "Relatório de novas questões:"
print ""
for indice in range(len(colaboradores)):
	print "%s: %d" % (colaboradores[indice], total_questoes[indice])
	total += total_questoes[indice]
print "---"
print "Total de novas questões: %d" % total
