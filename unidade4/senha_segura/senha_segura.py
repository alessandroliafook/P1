# coding: utf-8
# Senha Segura
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

senha = raw_input()
status = "senha insegura"
nova_senha = ""
tamanho = 0

for letra in senha:
	if letra != " " and letra not in "1234567890":
		nova_senha += letra * 2
	else:
		nova_senha += " "

if len(nova_senha) >= 13:
	status = "senha segura"

print nova_senha
print status

