# coding: utf-8
# Primeira Vogal
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

palavra = raw_input()
flag = False
for letra in palavra:
    if letra in "aeiouAEIOU":
        print letra
        flag = True
        break
if flag == False:
	print "-"
    
