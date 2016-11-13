#coding: utf-8
# Porta Eletrônica | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

porta_eletronica = []
entradas = []

while True:
	funcionario = raw_input()
	if funcionario in "S":
		break
	elif funcionario[0] == "P":
		registros = 0			
		for registro in porta_eletronica:
			if registro[2] == funcionario[2]:
				registros += 1
		entradas.append(registros)
	elif funcionario[0] == "R":			
		porta_eletronica.append(funcionario)
	
for i in entradas:
	print i

