# coding: utf-8
# Números Iguais
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

numero_1 = int(raw_input())
numero_2 = int(raw_input())
numero_3 = int(raw_input())

iguais = 0

if numero_1 == numero_2 and numero_1 == numero_3:
    iguais = 3

if numero_1 == numero_2 and numero_1 != numero_3:
    iguais = 2

if numero_1 != numero_2 and (numero_2 == numero_3 or numero_1 == numero_3):
    iguais = 2

print iguais
