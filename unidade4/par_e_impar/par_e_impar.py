# coding: utf-8
# Par e Ìmpar
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

quantidade_numeros = int(raw_input())

pares = []
impares = []

soma_pares = 0
soma_impares = 0

for i in range(quantidade_numeros):
    numero = int(raw_input())
    if numero % 2 == 0:
        pares.append(numero)
        soma_pares = soma_pares + numero
    else:
        impares.append(numero)
        soma_impares = soma_impares + numero

media_pares = soma_pares / float(len(pares))
media_impares = soma_impares / float(len(impares))

print "pares: %d" % (int(len(pares)))
print "ímpares: %d" % (int(len(impares)))
print "média pares: %.1f" % media_pares
print "média ímpares: %.1f" % media_impares
