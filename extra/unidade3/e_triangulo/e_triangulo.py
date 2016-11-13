# coding: utf-8
# É Triângulo
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

lado_1 = int(raw_input())
lado_2 = int(raw_input())
lado_3 = int(raw_input())

if abs(lado_2 - lado_3) < lado_1 < lado_2 + lado_3 \
   and abs(lado_1 - lado_3) < lado_2 < lado_1 + lado_3 \
   and abs(lado_1 - lado_2) < lado_3 < lado_1 + lado_2:
    perimetro = lado_1 + lado_2 + lado_3
    print  "triangulo valido. %d" % perimetro

else:
    print "triangulo invalido."
