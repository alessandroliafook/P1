# coding: utf-8
# Ano Bissexto
# (C) / 2015, Alessandro Santos / UFCG - PROGARMAÇÃO I

figura = raw_input()

import math

if figura == "círculo" or figura == "circulo":
    raio = float(raw_input())
    area = math.pi * (raio ** 2)

elif figura == "quadrado":
    lado = float(raw_input())
    area = lado ** 2

elif figura == "retângulo" or figura == "retangulo":
    base = float(raw_input())
    altura = float(raw_input())
    area = base * altura

elif figura == "triângulo" or figura == "triangulo":
    base = float(raw_input())
    altura = float(raw_input())
    area = (base * altura) / 2.0

print "Área do %s: %.2f (cm2)" % (figura, area)
