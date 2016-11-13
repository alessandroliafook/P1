#coding: utf-8
# Eh Palindromo | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

numero_conta = raw_input()
soma_par = 0
soma_impar = 0

for indice in range(len(numero_conta)):
	if indice == 0 or indice % 2 == 0:
		soma_par += int(numero_conta[indice])
	else:
		soma_impar += int(numero_conta[indice])

digito = (soma_par * soma_impar) % 11

if digito == 10:
	print "%s-X" % numero_conta
else:
	print "%s-%d" % (numero_conta, digito)


