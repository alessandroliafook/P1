# coding: utf-8
# Divisores Pares
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1


numero = float(raw_input())

for divisor in range(2, int(numero), 2):
    if numero % divisor == 0:
        print divisor
