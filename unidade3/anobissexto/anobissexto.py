# coding: utf-8
# Ano Bissexto
# (C) 2015, Alessandro Fook / UFCG, Programação I

ano = int(raw_input())

if ano % 400 == 0:
	print "%d é bissexto" % ano
elif ano % 4 == 0 and ano % 100 != 0:
	print "%d é bissexto" % ano
else:
	print "%d não é bissexto" % ano
