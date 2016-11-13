#coding: utf-8
# Aprovados no ENEM | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

nomes = []
notas = []

while True:
	candidatos = raw_input().split()
	if candidatos == ["fim"]:
		break
	nomes.append(candidatos[0])
	notas.append(int(candidatos[1]))

nota_corte = int(raw_input())

aprovados = False

for indice in range(len(notas)):
	if notas[indice] >= nota_corte:
		print "%s, %d" % (nomes[indice], notas[indice])
		aprovados = True

if aprovados == False:
	print  "Nenhum candidato aprovado."
