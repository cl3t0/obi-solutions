quantidade_de_pesos = int(input())

pesos = list(map(int, input().split()))
pesos.sort()

if pesos[0] <= 8:
	dando_certo = True
else:
	dando_certo = False

for i in range(quantidade_de_pesos - 1):
	if pesos[i+1] - pesos[i] > 8:
		dando_certo = False
		break
		
if dando_certo == True:
	print('S')
else:
	print('N')