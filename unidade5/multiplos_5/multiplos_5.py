#coding: utf-8
# Múltiplos de 5 | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

lim = int(raw_input())
mult = 0

while mult < lim:
	if mult % 2 == 0 and mult != 0:
		print mult
	mult += 5
	
