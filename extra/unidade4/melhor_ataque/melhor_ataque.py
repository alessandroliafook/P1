# coding: utf-8
# Ataque Mais Positivo de um Campeonato
# (C) 2015, Alessandro Fook / UFCG, Programação I


total_times = int(raw_input())
times = []
gols = []
maior_gol = -1
time_maior = []
total_goals = 0

for i in range(total_times):
	time = raw_input()
	times.append(time)	
	gol = int(raw_input())
	gols.append(gol)	
	total_goals += gol
	if gol > maior_gol:
		maior_gol = gol
		
media_gols = total_goals / float(total_times)

print "Time(s) com melhor ataque (%d gol(s)):" % maior_gol
for n in range(total_times):
	if gols[n] == maior_gol:	
		print "%s" % times[n]
print ""
print "Média de gols marcados: %.1f" % media_gols
