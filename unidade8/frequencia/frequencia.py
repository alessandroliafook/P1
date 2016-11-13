#coding: utf-8
# Frequencia
# 2015, (C), Alessandro Santos, Programação 1

def get_frequencia(lista):
	lista_t = lista[:]
	lista_frequencia = []
	frequencia = 0
	for elem in lista:
		for c_elem in range(len(lista_t) -1, -1, -1):
			if elem == lista_t[c_elem]:
				frequencia += 1
				lista_t.pop(c_elem)
		if frequencia > 0:		
			lista_frequencia.append(frequencia)
			frequencia = 0
	
	return lista_frequencia		

if __name__ == "__main__":
	assert get_frequencia(['b','b','c','b', 'a']) == [3,1,1]
