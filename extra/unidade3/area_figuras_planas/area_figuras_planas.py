# coding: utf-8
# Área das Figuras Planas
# (C) 2015, Alessandro Fook / UFCG, Programação I
import math

# vai receber o tipo de figura e dois valores que variam de acordo com a figura

figura = raw_input()

# calcular as áreas

area_da_figura = -1

if figura == "triângulo" or figura == "triangulo":
	valor_1 = float(raw_input())
	valor_2 = float(raw_input())
	area_da_figura = (valor_1 * valor_2) / 2

elif figura == "quadrado":
	valor_1 = float(raw_input())
	area_da_figura = valor_1 ** 2

elif figura == "círculo" or figura == "circulo":
	valor_1 = float(raw_input())
	area_da_figura = math.pi * (valor_1 ** 2)  

elif figura == "retângulo" or figura == "retangulo":
	valor_1 = float(raw_input())
	valor_2 = float(raw_input())
	area_da_figura = valor_1 * valor_2

print "Área do %s: %.2f (cm2)" % (figura, area_da_figura)

