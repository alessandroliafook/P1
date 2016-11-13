# coding: utf-8
# Remove Palavras com Mais Vogais
# 2015, (C), Alessandro Santos, Programação 1

def remove_palavras_com_mais_vogais(lista):
	m_vogal = 0
	n_vogais = []

	for palavra in lista:
		vogal = 0
		for letra in palavra:
			if letra in "aeiouAEIOU":
				vogal += 1

		if vogal > m_vogal:
			m_vogal = vogal

		n_vogais.append(vogal)
	
	for i_palavra in range(len(lista) -1, -1, -1):
		if n_vogais[i_palavra] == m_vogal:
			lista.pop(i_palavra)

if __name__ == "__main__":
	lista1 = ['arara', 'tv',   'bacia']
	assert remove_palavras_com_mais_vogais(lista1) == None
	assert lista1 == ['tv']
