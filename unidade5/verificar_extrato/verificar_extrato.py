# coding: utf-8
# Verifica Operações Extrato | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

limite_saques = int(raw_input())
saldo = float(raw_input())
saques = 0

while True:
	operacao = raw_input().split()
	if (operacao[0] == "saque" and saques + 1 > limite_saques) \
        or (operacao[0] == "depósito" and float(operacao[1]) > 1000.00) \
        or (operacao[0] == "saque" and saldo - float(operacao[1]) < 0):
		print "Operação inválida: %s %s." % (operacao[0], operacao[1])
		print "Seu saldo é R$ %.2f." % (saldo)
		break	
	elif operacao[0] == "saque":
		saques += 1
		saldo -= float(operacao[1])
	elif operacao[0] == "depósito":
		saldo += float(operacao[1])
	

