# coding: utf-8
# Conta Divisíveis
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

k = int(raw_input())
n = int(raw_input())

sequencia = []
quantidade_divisiveis_por_k = 0

for entrada in range(n):
    numero = int(raw_input())
    sequencia.append(numero)

for divisiveis in sequencia:
    if divisiveis % k == 0:
        quantidade_divisiveis_por_k = quantidade_divisiveis_por_k + 1

percentual = (100.0 * int(quantidade_divisiveis_por_k)) / n

print "%d (%.1f%%)" % (quantidade_divisiveis_por_k, percentual)

    
