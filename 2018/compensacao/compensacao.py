cheques_emitido, quantidade_habitantes = map(int, input().split())

carteiras = [0] * (quantidade_habitantes + 1)

dinheiro_transitado = 0

for i in range(cheques_emitido):
	x, v, y = map(int, input().split())
	# x deu v dinheiros para y
	carteiras[x] -= v
	carteiras[y] += v
	dinheiro_transitado += v

menor_dinheiro_transitado_possivel = 0

for i in carteiras:
	if i > 0:
		menor_dinheiro_transitado_possivel += i

if (dinheiro_transitado == menor_dinheiro_transitado_possivel):
	print('N')
else:
	print('S')
print(menor_dinheiro_transitado_possivel)