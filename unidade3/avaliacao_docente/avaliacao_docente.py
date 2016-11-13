# coding: utf-8
# Status de uma Disciplina
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1


numero_de_semestres = int(raw_input())
pontuacao_ensino = int(raw_input())
pontuacao_producao_intelectual = int(raw_input())
pontuacao_orientacao = int(raw_input())
pontuacao_administrativa = int(raw_input())

media_da_pontuacao = (pontuacao_ensino + pontuacao_producao_intelectual \
                  + pontuacao_orientacao + pontuacao_administrativa) \
                  / numero_de_semestres

if numero_de_semestres < 4:
    print "Promoção indeferida. Número de semestres insuficiente."

elif pontuacao_ensino < 320 or pontuacao_producao_intelectual < 100 \
     or pontuacao_orientacao < 20:
    print "Promoção indeferida. Pontuação mínima não alcançada."

elif media_da_pontuacao < 140:
    print "Promoção indeferida. Média insuficiente."

else:
    print "Promoção deferida. Parabéns!"
