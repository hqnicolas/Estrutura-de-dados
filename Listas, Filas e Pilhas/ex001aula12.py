##############################################################################################
# Utilizando a linguagem PYTHON, crie 2 listas: uma lista com  nomes dos clientes 
# de um banco (João, Maria, etc...) e outra lista com saldo da conta em reais(R$)
# correspondentes ao cliente (1350, 3240, etc... ), e usando estruturas de repetição 
# mostre os  dados da seguinte forma:
# Nome Cliente		Saldo Conta R$
# João			1350,00
# Maria			3240,00
# Etc.
# Mostrar também nome dos clientes com maior e menor saldo da conta.
##############################################################################################

import sys, os 

class Banco:
    def __init__(self):
        self.clientes = []
        self.saldos = []

    def adicionar_cliente(self):
        nome = input("Digite o nome: ")
        self.clientes.append(nome)

    def adicionar_saldo(self):
        saldo = float(input("Digite o saldo: "))
        if isinstance(saldo, (int, float)):
            self.saldos.append(float(saldo))
        else:
            print("O valor deve ser numérico.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar(banco):
    print(f"Nome Cliente     Saldo Conta R$")
    # Percorrendo a lista de clientes e seus saldos
    for i in range(len(banco.clientes)):
        maior_saldo = max(banco.saldos)
        menor_saldo = min(banco.saldos)
        indice_maior_saldo = banco.saldos.index(maior_saldo)
        indice_menor_saldo = banco.saldos.index(menor_saldo)
        cliente_com_maior_saldo = banco.clientes[indice_maior_saldo]
        cliente_com_menor_saldo = banco.clientes[indice_menor_saldo]
        print(f"{banco.clientes[i]}               {banco.saldos[i]}")

    print(f"Cliente com maior saldo: {cliente_com_maior_saldo}, Saldo: R${maior_saldo}")
    print(f"Cliente com menor saldo: {cliente_com_menor_saldo}, Saldo: R${menor_saldo}")
    
def menu_principal():
    banco = Banco()

    while True:
        clear_console()
        print("Escolha uma opção:")
        print("[1] - Exibir Lista")
        print("[2] - Adicionar um Cliente")
        print("[0] - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            mostrar(banco)
            input()

        elif opcao == 2:
            clear_console()
            banco.adicionar_cliente()
            banco.adicionar_saldo()
            print("Cliente Cadastrado")
            input()

        elif opcao == 0:
            break

        else:
            print("Opção inválida! Por favor, escolha uma das opções disponíveis.")
            input()

menu_principal()
