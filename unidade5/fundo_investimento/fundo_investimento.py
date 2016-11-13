#coding: utf-8
# Fundo de Investimento | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

valor_investido = 0
investimentos = 0
media = 0

while True:
	quantia = float(raw_input())
	if quantia < media and quantia > 0:
		break
	valor_investido += quantia
	investimentos += 1
	media = valor_investido / investimentos

print "Saldo total do FIS: R$%.2f." % valor_investido
print "Média das contribuições: R$%.2f." % media




