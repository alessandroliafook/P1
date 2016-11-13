#coding: utf-8
# Junção Ordenada de Duas Listas Ordenadas
# 2015, (C), Alessandro Santos, Programação 1

def juncao_ordenada(lista1, lista2):
	n_lista = []
	i_lista1 = 0
	i_lista2 = 0
	while i_lista1 < len(lista1) or i_lista2 < len(lista2):
		if i_lista1 == len(lista1):
			n_lista.append(lista2[i_lista2])
			i_lista2 += 1
		
		elif i_lista2 == len(lista2):
			n_lista.append(lista1[i_lista1])
			i_lista1 += 1	

		elif lista1[i_lista1] <= lista2[i_lista2]:	
			n_lista.append(lista1[i_lista1])
			i_lista1 += 1	

		elif lista2[i_lista2] < lista1[i_lista1]:	
			n_lista.append(lista2[i_lista2])
			i_lista2 += 1	
	return n_lista

if __name__ == "__main__":
	
	l1 = [8, 11, 78, 79, 511]
	l2 = [7, 8, 121, 302]
	assert juncao_ordenada(l1, l2) == [7, 8, 8, 11, 78, 79, 121, 302, 511]
	assert l1 == [8, 11, 78, 79, 511]
	assert l2 == [7, 8, 121, 302]

