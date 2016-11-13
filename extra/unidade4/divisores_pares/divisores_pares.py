# coding: utf-8
# Divisores Pares
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1
# nova tentativa, o servidor está bloqueando o envio..


numero = int(raw_input())

for divisor in range(2, numero, 2):
    if numero % divisor == 0:
        print divisor
