####################################################################################
# Este script cria uma matriz de acordo com as dimensões informadas pelo usuário,
# e cada elemento na matriz é inserido manualmente pelo usuário.
# A saída do programa será a matriz que você digitou.
####################################################################################
import os

# Solicitar ao usuário o tamanho da matriz
tam_linha = int(input("Digite o número de colunas na matriz: "))
tam_coluna = int(input("Digite o número de linhas na matriz: "))

# Criar a matriz com base no tamanho informado pelo usuário
matriz = []
for i in range(tam_linha):
    linha = []
    for j in range(tam_coluna):
        valor = input("Digite um elemento para [{}][{}]: ".format(i, j))
        linha.append(valor)
    matriz.append(linha)

# Imprimir a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=' ')
    print()  # Pular para a próxima linha após cada linha da matriz.
