# coding: utf-8
# Subtração de Polinomios
# 2015, (C), Alessandro Santos, Programação 1

def subtrai_polinomios(p1, p2):
	subtracao = []

	if len(p1) >= len(p2):
		indice = len(p1)
	else:
		indice = len(p2)

	for coef in range(indice):
		if coef >= len(p2):
			subtracao.append(int(p1[coef]))
		elif coef >= len(p1):
			subtracao.append(- int(p2[coef]))		
		else:
			subtracao.append(int(p1[coef]) - int(p2[coef]))

	while len(subtracao) > 0 and subtracao[-1] == 0:
		subtracao.pop(-1)
	
	return subtracao

if __name__ == "__main__":

	p1 = [-5, 4, 3]
	p2 = [-1, 0, 2, 0, 0, 0, 5]
	assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]
	
	p1 = [-5, 4, 3]  # 3x2 + 4x - 5
	p2 = [-4, 2, 3]  # 3x2 + 2x - 4
	assert subtrai_polinomios(p1, p2) == [-1, 2]  # 2x - 1
