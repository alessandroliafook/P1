def consumo(dia, amigo):
	consumo = 0
	for j in range(len(dia)):
		consumo += dia[j][amigo]
	return consumo


if __name__ == "__main__":

	sabado = [[1,2,3], [0,1,0], [3,1,2]]
	domingo = [[2,1,3], [0,2,1], [1,1,2]]

	print consumo(sabado, 0)
	print consumo(sabado, 1)
	print consumo(sabado, 2)

	sabado = [[1,2,3,4,5], [0,1,2,3,1], [2,1,0,1,2], [3,1,2,1,3], [4,1,3,0,0]]
	domingo = [[0,1,1,0,1], [1,2,2,0,2], [2,3,1,1,1], [3,4,2,0,0], [4,3,3,0,0]]
	print consumo(sabado, 0)
	print consumo(sabado, 1)
	print consumo(sabado, 2)
	print consumo(sabado, 3)
	print consumo(sabado, 4)


