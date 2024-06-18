##############################################################
# CASSIO MACHADO CARDOSO                                     #
# DAVI SARTOR                                                #
# NICOLAS BORBA PEREIRA                                      #
##############################################################
# Algoritmos de Busca e aplicação de grafos ás rotas         #
# de transporte no sudeste do estado de Santa Catarina       #
##############################################################
# Importação de módulos necessários
import heapq
import sys, os

# Função para limpar a tela do console
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

# Representação gráfica das estradas entre cidades
graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11), (8, 7)],
    2: [(1, 8), (3, 7), (5, 4), (8, 2)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(2, 4), (3, 14), (4, 10), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(1, 7), (2, 2), (6, 6), (7, 7)]
}

# Função para otimizar o caminho usando o algoritmo de Dijkstra
def otimizador(graph, start, end):
    fila = [(0, start)]
    distancias = {node: float('infinity') for node in graph}
    distancias[start] = 0
    anteriores = {node: None for node in graph}
    while fila:
        # Reconstruir o caminho desde o início até o fim
        distancia_atual, atual = heapq.heappop(fila)
        if atual == end:
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = anteriores[atual]
            return caminho[::-1]
        for vizinho, peso in graph[atual]:
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                anteriores[vizinho] = atual
                heapq.heappush(fila, (distancia, vizinho))
    return None

# Função para encontrar o caminho mais curto entre dois nós
def buscar_caminho(start, end):
    return otimizador(graph, start, end)

# Laço principal do programa
while True:
    limpa()
    print("\nTransportadora Sudeste")
    print("\nEscolha uma opção:")
    print("[1] - Otimização da Rota de Transporte")
    print("[2] - Sair do programa")
    option = int(input("Escolha uma opção: "))
    if option == 1:
        limpa()
        print("Sumário:\n0 - São Joaquim || 1 - Lages         || 2 - Campos Novos \
              \n3 - Curitibanos || 4 - Monte Castelo || 5 - Rio do Sul \
              \n6 - Ibirama     || 7 - Blumenau      || 8 - Brusque")
        nodo_inicial = int(input("Digite sua localização: "))
        nodo_final = int(input("Digite a cidade destino: "))

        #Encontrar o caminho mais curto usando o algoritmo de Dijkstra
        caminho = buscar_caminho(nodo_inicial, nodo_final)
        limpa()
        print(f"Caminho de {nodo_inicial} para {nodo_final}")
        print(caminho)
        print("Saindo de:")
        for i in caminho:
            match i:
                case 0:
                    print("    São Joaquim ")
                case 1:
                    print("    Lages ")
                case 2:
                    print("    Campos Novos ")
                case 3:
                    print("    Curitibanos ")
                case 4:
                    print("    Monte Castelo ")
                case 5:
                    print("    Rio do Sul ")
                case 6:
                    print("    Ibirama ")
                case 7:
                    print("    Blumenau ")
                case 8:
                    print("    Brusque ")
            print("Vá até:")
        print("     O Local da entrega.")
        input()

    elif option == 2:
        limpa()
        break

    else:
        limpa()
        print("Opção inválida. Por favor, escolha uma das opções disponíveis.")