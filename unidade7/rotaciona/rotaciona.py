# coding: utf-8
# Rotaciona
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1



def rotacionaum(sequencia):
	if sequencia == []:
		return	
	sequencia.append(sequencia[0])
	del sequencia[0]

def rotaciona(sequencia, num):
	for repeticoes in range(num):
		rotacionaum(sequencia)

if __name__ == "__main__":
	sequencia = [1, 2, 3, 4, 5, 6, 7, 8]
	rotacionaum(sequencia)
	print sequencia
	
	sequencia = [1, 2, 3, 4, 5, 6, 7, 8]
	rotaciona(sequencia, 2)
	print sequencia
	

	sequencia = [1, 2, 3, 4, 5, 6, 7, 8]
	rotaciona(sequencia, 3)
	print sequencia

	sequencia = [1, 2, 3, 4, 5, 6, 7, 8]
	rotaciona(sequencia, 0)
	print sequencia

	sequencia = [1]
	rotaciona(sequencia, 1)
	print sequencia

	sequencia = []
	rotaciona(sequencia, 2)
	print sequencia

	sequencia = [1, 2, 3, 4, 5, 6, 7, 8]
	rotaciona(sequencia, 0)
	print sequencia

	sequencia = [1, 2, 3, 4, 5, 6, 7, 8]
	rotaciona(sequencia, -1)
	print sequencia


