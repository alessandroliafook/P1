# coding: utf-8
# Média dos Pares
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

n = int(raw_input())

pares = []
numeros = []
soma = 0
numero_abaixo_media = 0

for i in range(n):
    numero_inserido = int(raw_input())
    numeros.append[numero_inserido]
    
    if numero % 2 == 0 and numero != 0:
        pares.append(numero_inserido)
        soma += numero_inserido

media = float(soma) / int(len(pares))

for numero_par in numeros:
    if numero_par < media:
        numero_abaixo_media += 1
    

print "soma: %d" % soma
print "média: %.1f" % media
print "%d número(s) abaixo da média" % numero_abaixo_media


