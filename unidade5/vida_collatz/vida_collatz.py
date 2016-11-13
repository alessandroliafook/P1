#coding: utf-8
# Vida Collatz | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

num = int(raw_input())
vida = 1

while num > 1:
	if num % 2 == 0:
		num = num / 2
		vida += 1
	elif num % 2 == 1:
		num = 3 * num + 1
		vida += 1

print vida
