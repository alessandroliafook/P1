# coding: utf-8
# Lanche mais Pedido
# (C) / Alessandro Santos, 2015 / UFCG - PROGRAMAÇÃO 1

def lanchemaispedido(pedidos):
	mais_pedido = 0
	lanche = ""
	for i_pedidos in range(len(pedidos)):
		num_pedidos = 0	
		for i_2_pedidos in range(i_pedidos, len(pedidos)):
			if pedidos[i_pedidos] == pedidos[i_2_pedidos]:
				num_pedidos += 1
		if num_pedidos > mais_pedido and num_pedidos > len(pedidos) / 2:
			mais_pedido = num_pedidos
			lanche = pedidos[i_pedidos]
	if lanche != "":	
		return lanche	

ines = ['tapioca','tapioca','salada','bolo','misto','tapioca', 'tapioca'] 

marcos = ['suco','coxinha','suco','misto','folhado']

assert lanchemaispedido(ines) == 'tapioca' 

assert lanchemaispedido(marcos) == None
