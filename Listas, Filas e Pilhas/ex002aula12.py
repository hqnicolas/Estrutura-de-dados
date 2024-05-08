##############################################################################################
# Faça um Programa Python que crie 3 listas: uma lista com  nomes de frutas e outra lista com 
# quantidade em estoque correspondente as frutas e uma terceira lista correspondendo
# o preço do quilo da fruta usando estruturas de repetição mostre os  dados da seguinte forma:
# Fruta		Qtde Estoque		Preço Kg
# Laranja		35			4.25
# Banana		20			3.75
# Etc.
# Mostrar também as frutas com maior e menor quantidade em estoque.
# Mostrar a soma total das quantidades das frutas.
##############################################################################################
import sys,os 

class estoque:
    def __init__(self):
            self.frutas = []
            self.qtd_estoque = []
            self.preco = []

    def adicionar_fruta(self):
        self.frutas.append(input("Digite o nome da fruta: "))
        self.qtd_estoque.append(float(input("Informe a quantidade de frutas em estoque: ")))
        self.preco.append(input("Informe o preço do quilo da fruta R$: "))

    def mostrar_frutas(self):
        clear_console()
        print(f"Nome da Fruta     Quantidade")
    # Percorrendo a lista de frutas e seus qtd_estoque
        for i in range(len(estoque.frutas)):
            maior_saldo = max(estoque.qtd_estoque)
            menor_saldo = min(estoque.qtd_estoque)
            soma = soma + estoque.qtd_estoque
            indice_maior_saldo = estoque.qtd_estoque.index(maior_saldo)
            indice_menor_saldo = estoque.qtd_estoque.index(menor_saldo)
            fruta_com_maior_saldo = estoque.frutas[indice_maior_saldo]
            fruta_com_menor_saldo = estoque.frutas[indice_menor_saldo]
            print(f"{estoque.frutas[i]}               {estoque.qtd_estoque[i]}")
        print(f"\nfruta com maior saldo: {fruta_com_maior_saldo}, Quantidade: {maior_saldo}")
        print(f"\nfruta com menor saldo: {fruta_com_menor_saldo}, Quantidade: {menor_saldo}")
        print(f"\nSomatório do saldo: {soma}")
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

estoque = estoque()
while True:
    clear_console()
    print("Escolha uma opção:")
    print("[1] - Exibir Lista de frutas")
    print("[2] - Adicionar uma fruta")
    print("[0] - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        estoque.mostrar_frutas()
        input()

    elif opcao == 2:
        clear_console()
        estoque.adicionar_fruta()
        print("Fruta adicionada")
        input()

    elif opcao == 0:
        break
    else:
        print("Opção inválida! Por favor, escolha uma das opções disponíveis.")
        input()
