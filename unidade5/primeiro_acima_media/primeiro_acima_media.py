#coding: utf-8
# Primeiro Acima da Média | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

valores = []
soma = 0
quantidade = 0

while True:
	num = raw_input()
	if num == "fim":
		break
	soma += float(num)
	quantidade += 1
	valores.append(float(num))

media = soma / quantidade

for indice in range(len(valores)):
	if valores[indice] > media:
		print "%d, %.2f > %.2f" % (indice, valores[indice], media)
		break
