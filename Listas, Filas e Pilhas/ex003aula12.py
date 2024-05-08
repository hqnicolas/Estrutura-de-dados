import sys, os 

class Patio:
    def __init__(self):
        self.veiculos = []
        self.ano = []

    def adicionar_veiculo(self):
        nome = input("Digite o nome do veiculo: ")
        self.veiculos.append(nome)

    def adicionar_ano(self):
        saldo = float(input("Digite o Ano: "))
        if isinstance(saldo, (int, float)):
            self.ano.append(float(saldo))
        else:
            print("O valor deve ser numérico.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar(patio):
    print(f"Nome Veiculo        Ano")
    # Percorrendo a lista de veiculos e seus ano
    for i in range(len(patio.veiculos)):
        maior_ano = max(patio.ano)
        menor_ano = min(patio.ano)
        indice_maior_ano = patio.ano.index(maior_ano)
        indice_menor_ano = patio.ano.index(menor_ano)
        veiculo_com_maior_ano  = patio.veiculos[indice_maior_ano]
        veiculo_com_menor_ano = patio.veiculos[indice_menor_ano]
        print(f"{patio.veiculos[i]}               {patio.ano[i]}")

    print(f"Carro mais novo: {veiculo_com_maior_ano}, Ano: {maior_ano}")
    print(f"Carro mais velho: {veiculo_com_menor_ano}, Ano: {menor_ano}")
    
def menu_principal():
    patio = Patio()

    while True:
        clear_console()
        print("Escolha uma opção:")
        print("[1] - Exibir Lista")
        print("[2] - Adicionar um Veiculo")
        print("[0] - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            mostrar(patio)
            input()

        elif opcao == 2:
            clear_console()
            patio.adicionar_veiculo()
            patio.adicionar_ano()
            print("Veiculo Cadastrado")
            input()

        elif opcao == 0:
            break

        else:
            print("Opção inválida! Por favor, escolha uma das opções disponíveis.")
            input()

menu_principal()
