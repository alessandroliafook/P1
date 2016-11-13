# coding: utf-8
# Nova Palavra
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

palavra = raw_input()
digitos = raw_input()

nova_palavra = ""

for letra in range(len(palavra)):
	nova_palavra += palavra[letra] * (int(digitos[len(digitos) -1 -letra]) + 1)

print nova_palavra
