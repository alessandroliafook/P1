# coding: utf-8
# Fila por altura | Programação 1 - UFCG
# Alessandro Lia Fook Santos, 2015, (C)

# list.insert(index, obj)

# nome é string
# altura é float

def insere_na_fila(fila, nome, altura):
	for i_tupla in range(len(fila)):
		if fila[i_tupla][1] > altura:
			aluno = (nome, altura)
			fila.insert(i_tupla, aluno)
			break
		elif i_tupla == len(fila) -1:
			aluno = (nome, altura)
			fila.append(aluno)
	
fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]

