quantidade_de_retangulos = int(input())

# formato x1, y1, x2, y2
retangulos = []

maior_area = 0

# Recebendo os inputs e colocando as cords dentro da lista de retangulos
for i in range(quantidade_de_retangulos):
	# Recebendo a nova linha
	linha = input()
	# Transformando os valores para inteiros
	cords = list(map(int, linha.split()))

	x1 = min(cords[0], cords[2])
	y1 = min(cords[1], cords[3])
	x2 = max(cords[0], cords[2])
	y2 = max(cords[1], cords[3])

	retangulo = [i, x1, y1, x2, y2]

	# Calculando a area
	base = x2 - x1
	altura = y2 - y1
	area = base * altura

	if (area > maior_area):
		maior_area = int(area)
		maior_retangulo = list(retangulo)

	# Colocando as cords na lista de retangulos
	retangulos.append(retangulo)

def dentro(retangulomaior, retangulomenor):

	# Renomeando as variaveis para facilitar compreensão
	r1_x1 = retangulomaior[1]
	r1_y1 = retangulomaior[2]
	r1_x2 = retangulomaior[3]
	r1_y2 = retangulomaior[4]
	r2_x1 = retangulomenor[1]
	r2_y1 = retangulomenor[2]
	r2_x2 = retangulomenor[3]
	r2_y2 = retangulomenor[4]

	x1_dentro = r1_x1 < r2_x1 and r2_x1 < r1_x2
	x2_dentro = r1_x1 < r2_x2 and r2_x2 < r1_x2
	y1_dentro = r1_y1 < r2_y1 and r2_y1 < r1_y2
	y2_dentro = r1_y1 < r2_y2 and r2_y2 < r1_y2

	# Fazendo a checagem
	if (x1_dentro and x2_dentro and y1_dentro and y2_dentro):
		return True
	else:
		return False

def verificarCamadas(retangulos, retangulomaior, retangulomenor):

	# Checando de o retangulo menor esta dentro do maior
	if (dentro(retangulomaior, retangulomenor)):

		# Renomeando as variaveis para facilitar compreensão
		r1_x1 = retangulomaior[1]
		r1_y1 = retangulomaior[2]
		r1_x2 = retangulomaior[3]
		r1_y2 = retangulomaior[4]
		r2_x1 = retangulomenor[1]
		r2_y1 = retangulomenor[2]
		r2_x2 = retangulomenor[3]
		r2_y2 = retangulomenor[4]

		deu_certo = True

		for retangulo in retangulos:

			# Renomeando as variaveis para facilitar compreensão
			x1 = retangulo[1]
			y1 = retangulo[2]
			x2 = retangulo[3]
			y2 = retangulo[4]

			# Verificações
			y1_dentro = y1 < r2_y1 and r2_y1 < y2
			x2_dentro = r2_x2 < x2 and x2 < r1_x2
			x1_dentro = r2_x2 < x1 and x2 < r1_x2

			if ((y1_dentro and x2_dentro) != (y1_dentro and x1_dentro)):
				deu_certo = False
				break

		if (deu_certo == True):
			return True
		else:
			return False

# Cada retangulo pode possui outros retangulos

global possui
possui = {}

# Verificando quais retangulos possuem quais

for i in range(quantidade_de_retangulos):
	possui[i] = []

for i in retangulos:
	for j in retangulos:
		if verificarCamadas(retangulos, i, j):
			possui[i[0]].append(j[0])

global contador

if len(possui[maior_retangulo[0]]) != 0:
	contador = len(possui[maior_retangulo[0]])
else:
	contador = 1

def somarcontador(i):
	global possui
	global contador
	if len(possui[i]) != 0:
		contador += len(possui[i]) - 1
		for j in possui[i]:
			somarcontador(j)

for i in possui[maior_retangulo[0]]:
	somarcontador(i)

print(contador)
