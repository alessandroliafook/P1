#coding: utf-8
# Fila de Atendimento de Pacientes
# 2015, (C), Alessandro Santos, Programação 1

def filas_de_atendimento(fila_unica, n):
	fila_organizada = []
	medico = 0

	for medicos in range(n):
		fila_organizada.append([])


	for paciente in fila_unica:
		if medico < n:
			fila_organizada[medico].append(paciente)
			medico += 1
		elif medico >= n:
			fila_organizada[0].append(paciente)
			medico = 1
		
	return fila_organizada

if __name__ == "__main__":

	fila_1 = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
	assert filas_de_atendimento(fila_1, 3) == [['Andre','Carlos'],['Antonio', 'Claudia'], ['Bianca']]

	fila_2 = ['Andre', 'Antonio', 'Bianca', 'Carlos']
	assert filas_de_atendimento(fila_2, 2) == [['Andre','Bianca'],['Antonio', 'Carlos']]



