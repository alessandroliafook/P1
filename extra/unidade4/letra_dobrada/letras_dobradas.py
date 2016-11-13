# coding: utf-8
# Palavras com Letras Dobradas
# (C) 2015, Alessandro Fook / UFCG, Programação I

num_palavras = int(raw_input())

pal_dobradas = []
pal_n_dobradas = []

for i in range(num_palavras):
	palavra = raw_input()
	dobradas = False	
	for letra in range(len(palavra)):
		if letra + 1 < len(palavra) and palavra[letra] == palavra[letra + 1]:
			dobradas = True
	if dobradas == True:
		pal_dobradas.append(palavra)
	else:
		pal_n_dobradas.append(palavra)


print "%d palavra(s) com letras dobradas:" % (len(pal_dobradas))
for elemento in pal_dobradas:
	print "%s" % elemento
print "---"
print "%d palavra(s) sem letras dobradas:" % (len(pal_n_dobradas))
for elemento2 in pal_n_dobradas:
	print "%s" % elemento2


