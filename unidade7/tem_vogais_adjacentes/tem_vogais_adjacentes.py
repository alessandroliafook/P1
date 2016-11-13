# coding: utf-8
# Tem Vogais Adjacentes | UFCG - PROGRAMAÇÃO 1
# (C) | Alessandro Santos, 2015

def tem_vogais_adjacentes(palavra):
	for i_palavra in range(len(palavra) - 1):
		if palavra[i_palavra].lower() in "aeiou" \
		and palavra[i_palavra + 1].lower() in "aeiou":
			return "sim"
	return "nao"


palavra = raw_input()
print tem_vogais_adjacentes(palavra)

if __name__ == "__main__":
	assert tem_vogais_adjacentes("orfeu") == "sim"
	assert tem_vogais_adjacentes("brasil") == "nao"
	assert tem_vogais_adjacentes("voo") == "sim"

