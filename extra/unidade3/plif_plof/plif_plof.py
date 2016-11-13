# coding: utf-8
# Plif Plof
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

numero_1 = int(raw_input())
numero_2 = int(raw_input())
numero_3 = int(raw_input())

soma = numero_1 + numero_2 + numero_3

if soma % 3 == 0 and soma % 5 == 0:
    print "plifplof"

elif soma % 3 == 0:
    print "plif"

elif soma % 5 == 0:
    print "plof"

else:
    print soma

