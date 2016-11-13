# coding: utf-8
# Convertendo um Número Octal em um Número Decimal
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

numero_octal = raw_input()

numero_decimal = 0

for i in range(len(numero_octal)):
	conversao = int(numero_octal[i]) * 8 ** (len(numero_octal) - (i + 1))
	numero_decimal += conversao	
	print "%s * 8^%d = %d" % (numero_octal[i], len(numero_octal) - (i+ 1) \
	, conversao)

print "%s(8) = %d(10)" % (numero_octal, numero_decimal)
