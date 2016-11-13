# coding: utf-8
# DNA
# (C) 2015, Alessandro Fook / UFCG, Programação I

# ler as sequências
dna_sequencia_1 = raw_input()
dna_sequencia_2 = raw_input()
dna_sequencia_3 = raw_input()

# identificar os tamanhos

tamanho_da_sequencia_1 = len(dna_sequencia_1)
tamanho_da_sequencia_2 = len(dna_sequencia_2)
tamanho_da_sequencia_3 = len(dna_sequencia_3)

# comparar

if tamanho_da_sequencia_1 <= tamanho_da_sequencia_2 and tamanho_da_sequencia_1 <= tamanho_da_sequencia_3:
	print "%s %d" % (dna_sequencia_1, tamanho_da_sequencia_1)

elif tamanho_da_sequencia_2 < tamanho_da_sequencia_1 and tamanho_da_sequencia_2 <= tamanho_da_sequencia_3:
	print "%s %d" % (dna_sequencia_2, tamanho_da_sequencia_2)

else:
	print "%s %d" % (dna_sequencia_3, tamanho_da_sequencia_3)

