largura_da_sala = int(input())
comprimento_da_sala = int(input())

quantidade_tipo1 = largura_da_sala * comprimento_da_sala + (largura_da_sala - 1) * (comprimento_da_sala - 1)
quantidade_tipo2 = 2 * (largura_da_sala - 1) + 2 * (comprimento_da_sala - 1)

print(quantidade_tipo1)
print(quantidade_tipo2)