# coding: utf-8
# Meta
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1


meta_mensal = float(raw_input())
vendas = []
venda_total = 0
bonus_funcionario = []
meta = "meta não foi atingida"
meta_ind = True

for valor in range(6):
	venda_funcionario = float(raw_input())
	vendas.append(venda_funcionario)
	venda_total += venda_funcionario	

for valor in vendas:
	if valor < (meta_mensal / 6):
		meta_ind = False

if venda_total >= meta_mensal and meta_ind == True:
	for valor in vendas:
		bonus = valor / 100
		bonus_funcionario.append(bonus)
	meta = "meta atingida"

print "Total de vendas: R$ %.2f (%s)" % (venda_total, meta)
print "----"
if meta == "meta atingida":
	print "Bonificação:"
	print "Funcionário 1: R$ %.2f" % bonus_funcionario[0]
	print "Funcionário 2: R$ %.2f" % bonus_funcionario[1]
	print "Funcionário 3: R$ %.2f" % bonus_funcionario[2]
	print "Funcionário 4: R$ %.2f" % bonus_funcionario[3]
	print "Funcionário 5: R$ %.2f" % bonus_funcionario[4]
	print "Funcionário 6: R$ %.2f" % bonus_funcionario[5]



