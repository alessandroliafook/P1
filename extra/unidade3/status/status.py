# coding: utf-8
# Status de uma Disciplina
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

nota_1 = float(raw_input())
nota_2 = float(raw_input())
nota_3 = float(raw_input())

numero_de_faltas = int(raw_input())

numero_de_aulas = 30.0

presenca = (numero_de_faltas * 100) / 30

media = (nota_1 + nota_2 + nota_3) / 3

if presenca > 25.0:
    print "reprovado por faltas"

elif media < 4.0:
    print "reprovado por nota"

elif 4.0 <= media < 7.0:
    print "prova final"

else:
    print"aprovado por media"


