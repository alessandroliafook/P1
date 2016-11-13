# coding: utf-8
# Novo Salário
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

# entrada

sal_atual = float(raw_input("Salário atual? "))
aument_proj = float(raw_input("Aumento projetado (em %)? "))
prev = float(raw_input("Nova contribuição Previdenciária (em %)? "))

# calculo

sal_novo = (sal_atual * aument_proj / 100) + sal_atual
cont_prev = sal_novo * prev / 100
sal_liq = sal_novo - cont_prev

# saida

print ""
print "Dados do novo salário"
print "==="
print "Salário: R$ %.2f" % sal_novo
print "Contribuição previdenciária: R$ %.2f (%.1f%%)" % (cont_prev, prev)
print "Salário líquido: R$ %.2f" % sal_liq
