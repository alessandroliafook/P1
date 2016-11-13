#coding: utf-8
# Sequência | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

limite = int(raw_input())
contador = 1
soma = 1

while soma < limite:
	print contador
	contador *= 2
	soma += contador
