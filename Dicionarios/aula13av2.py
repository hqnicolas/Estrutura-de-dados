##############################################################################################
#Crie um dicionário com os nomes dos estados do Brasil e sua respectiva capital, seguindo o exemplo:
#estados = {“Acre” : “Capital Rio Branco”,  “Alagoas” :  “Capital Maceió”, 
#                    “Amazonas”: “Capital Manaus”,  “Bahia” : “Capital Salvador”, 
#                    “Distrito Federal” : “Capital Brasília”,  “Santa Catarina” : “Capital Florianópolis”, 
#                    “Rio Grande do Sul” : “Capital Porto Alegre”,
#                    “Paraná” : “Capital Curitiba”, “São Paulo” : “Capital São Paulo”,
#                    “Minas Gerais” : “Cuiabá”, “Rio de Janeiro” : “Rio de Janeiro”,
#                    “Tocantins”: “Capital Palmas”}
#Agora, inclua um novo estado e sua capital no final da lista.
#Mostre em qual posição está “Distrito Federal”. 
#Altere a capital do estado “Minas Gerais” para “Belo Horizonte”
#Ao final, mostre a lista completa de séries. 
##############################################################################################

import sys, os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_estado(estados):
    nome_estado = input("\nDigite o nome do estado que deseja cadastrar: ")
    if nome_estado not in estados:
        if not estados:
            max_posicao = 1
        else:
            max_posicao = len(estados) + 1
        capital_estado = input("Digite a capital do estado: ")
        estados[nome_estado] = capital_estado
        print(f"\nEstado {nome_estado} cadastrado com sucesso na posição {max_posicao}!")
    else:
        print("\nO estado já está cadastrado. Tente novamente.")
    input()
    return estados


def excluir_estado(estados):
    nome_estado = input("\nDigite o nome do estado que deseja excluir: ")
    if nome_estado in estados:
        del estados[nome_estado]
        print(f"\nInfelizmente o estado {nome_estado} não faz mais parte da lista e foi removido.\n")
    else:
        print("\nO estado que você tentou excluir não está na sua lista.\n")
    input()
    return estados

def pesquisar_estado(estados):
    nome_estado = input("\nDigite o nome do estado que deseja pesquisar: ")
    if nome_estado in estados:
        posicao = list(estados.keys()).index(nome_estado) + 1
        print(f"\nO estado {nome_estado} está na posição {posicao} e sua capital é {estados[nome_estado]}\n")
    else:
        print("\nO estado que você pesquisou não está na sua lista.\n")
    input()

def alterar_estado(estados):
    nome_estado = input("\nDigite o nome do estado cuja capital deseja alterar: ")
    if nome_estado in estados:
        nova_capital = input("Digite a nova capital do estado: ")
        estados[nome_estado] = nova_capital
        print(f"\nA capital do estado {nome_estado} foi alterada para {nova_capital}.\n")
    else:
        print("\nO estado que você tentou alterar não está na sua lista.\n")
    input()

def exibir_dicionario(estados):
    if len(estados) > 0:
        print('\n** Dicionário de Estados **')
        for estado, capital in estados.items():
            print(f"{estado} - {capital}")
    else:
        print("\nAinda não há estados cadastrados.\n")
    input()

def menu_principal():
    estados = {}
    while True:
        clear_console()
        print("\n** Menu Principal **")
        print("1. Cadastrar Estado")
        print("2. Excluir Estado")
        print("3. Pesquisar por Nome")
        print("4. Alterar Capital")
        print("5. Exibir Dicionário Completo")
        print("6. Sair\n")

        opcao = int(input('Digite a sua escolha: '))

        if opcao == 1:
            clear_console()
            estados = cadastrar_estado(estados)

        elif opcao == 2:
            clear_console()
            estados = excluir_estado(estados)

        elif opcao == 3:
            clear_console()
            pesquisar_estado(estados)

        elif opcao == 4:
            clear_console()
            alterar_estado(estados)

        elif opcao == 5:
            clear_console()
            exibir_dicionario(estados)

        elif opcao == 6:
            clear_console()
            break

        else:
            print('\nOpção inválida. Tente novamente.\n')

menu_principal()