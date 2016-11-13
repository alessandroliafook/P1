# coding: utf-8
# Ano Bissexto
# (C) / 2015, Alessandro Santos / UFCG - PROGARMAÇÃO I

ano = int(raw_input())

if ano % 400 == 0 or (ano % 4 == 0 and  ano % 100 !=0):
    print "%d é bissexto"

else:
    print " não é bissexto"
