# coding: utf - 8
# Quem bebeu mais menos
# (C) 2015, Alessandro Santos, Programação 1

def consumo(dia, amigo):
	consumo = 0
	for j in range(len(dia)):
		consumo += dia[j][amigo]
	return consumo


def quem_bebeu_mais_menos(dia1, dia2):
	maior_consumo = consumo(dia1, 0) + consumo(dia2, 0)
	maior_consumidor = 1
	menor_consumo = consumo(dia1, 0) + consumo(dia2, 0)
	menor_consumidor = 1

	for i in range(len(dia1[0])):
		if consumo(dia1, i) + consumo(dia2, i) > maior_consumo:
			maior_consumo = consumo(dia1, i) + consumo(dia2, i)
			maior_consumidor = i + 1
		if consumo(dia1, i) + consumo(dia2, i) < menor_consumo:
			menor_consumo = consumo(dia1, i) + consumo(dia2, i)
			menor_consumidor = i + 1
	return maior_consumidor, menor_consumidor

if __name__ == "__main__":
	sabado = [[1,2,3], [0,1,0], [3,1,2]]
	domingo = [[2,1,3], [0,2,1], [1,1,2]]
	assert quem_bebeu_mais_menos(sabado, domingo) == (3,1)
	sabado = [[1,2,3,4,5], [0,1,2,3,1], [2,1,0,1,2], [3,1,2,1,3], [4,1,3,0,0]]
	domingo = [[0,1,1,0,1], [1,2,2,0,2], [2,3,1,1,1], [3,4,2,0,0], [4,3,3,0,0]]
	assert quem_bebeu_mais_menos(sabado, domingo) == (1,4)

