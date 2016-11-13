#coding: utf-8
# Abaixo da Média | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

sequencia = []
qnt_v = 0
soma = 0

while True:
	valor = raw_input()
	if valor == "fim":	
		break
	qnt_v += 1
	soma += int(valor)
	sequencia.append(int(valor))

media = float(soma) / qnt_v
print "%.2f" % media
for num in range(len(sequencia)):
	if sequencia[num] < media:
		print "%d %d" % (num + 1, sequencia[num])


