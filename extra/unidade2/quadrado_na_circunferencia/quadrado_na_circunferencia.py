# coding: utf-8

import math

raio = float(raw_input())

area_da_circunferencia = math.pi * raio ** 2

area_do_quadrado = ((2 * raio) ** 2) / 2

area = area_da_circunferencia - area_do_quadrado

print "Área não comum: %.5f" % area
