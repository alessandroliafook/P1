# coding: utf-8
# Corrigindo Equações
# (C) 2015, Alessandro Fook / UFCG, Programação I

elemento_a = float(raw_input())
elemento_b = float(raw_input())
elemento_c = float(raw_input())

delta = (((elemento_b ** 2) - (4 * elemento_a * elemento_c))) 

if delta > 0:
	delta_2 = delta ** 0.5
	raiz_1 = ((-elemento_b) + delta_2) / (2 * elemento_a)
	raiz_2 = ((-elemento_b) - delta_2) / (2 * elemento_a)
	print "x1 = %.2f" % raiz_1
	print "x2 = %.2f" % raiz_2

elif delta == 0:
	raiz = (-elemento_b) / (2 * elemento_a)
	print "x = %.2f" % raiz

else:
	print "sem raizes reais"
