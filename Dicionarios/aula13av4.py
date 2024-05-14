##############################################################################################
#Crie um dicionário com os nomes de atletas famosos, seguindo exemplo:
#atletas = { “Cristiano Ronaldo” : “Futebol”, “LeBron James” : “Basquete”,
#                    “Lionel Messi” : “Futebol”, “Neymar” : “Futebol”,
#                    “Conor McGregor” : “MMA”, “Roger Federer” : “Tênis”,
#                     “Rafael Nadal” : “Tênis”,  “Stephen Curry” : “Basquete”,
#                     “Tiger Woods” : “Golfe”,  “Kevin Durant” : “Basquete”,
#                      “Lewis Hamilton” : “Fórmula 1”, “Sun Yang” : “Natação” }
#Agora, inclua um novo atleta no final da lista 
#Mostre em qual posição está o atleta  “Roger Federer”. 
#Infelizmente o atleta “Tiger Woods” não faz mais parte da lista e deve ser removido.
#Ao final, mostre a lista completa de atletas.
##############################################################################################

import sys, os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_atleta(atletas):
    nome_atleta = input("\nDigite o nome do atleta que deseja cadastrar: ")
    if nome_atleta not in atletas:
        if not atletas:
            max_posicao = 1
        else:
            max_posicao = len(atletas) + 1
        estado_atleta = input("Digite o esporte do atleta: ")
        atletas[nome_atleta] = estado_atleta
        print(f"\nAtleta {nome_atleta} cadastrado com sucesso na posição {max_posicao}!")
    else:
        print("\nO atleta já está cadastrado. Tente novamente.")
    input()
    return atletas

def excluir_atleta(atletas):
    nome_atleta = input("\nDigite o nome do atleta que deseja excluir: ")
    if nome_atleta in atletas:
        del atletas[nome_atleta]
        print(f"\nInfelizmente o atleta {nome_atleta} não faz mais parte da lista e foi removido.\n")
    else:
        print("\nO atleta que você tentou excluir não está na sua lista.\n")
    input()
    return atletas

def pesquisar_atleta(atletas):
    nome_atleta = input("\nDigite o nome do atleta que deseja pesquisar: ")
    if nome_atleta in atletas:
        posicao = list(atletas.keys()).index(nome_atleta) + 1
        print(f"\nO atleta {nome_atleta} está na posição {posicao} e seu esporte é {atletas[nome_atleta]}\n")
    else:
        print("\nO atleta que você pesquisou não está na sua lista.\n")
    input()

def alterar_atleta(atletas):
    nome_atleta = input("\nDigite o nome do atleta cujo esporte deseja alterar: ")
    if nome_atleta in atletas:
        novo_esporte = input("Digite o novo esporte do atleta:")
        atletas[nome_atleta] = novo_esporte
        print(f"\nO esporte do atleta {nome_atleta} foi alterada para {novo_esporte}.\n")
    else:
        print("\nO atleta que você tentou alterar não está na sua lista.\n")
    input()

def exibir_dicionario(atletas):
    if len(atletas) > 0:
        print('\n** Dicionário de Atletas **')
        for atleta, estado in atletas.items():
            print(f"{atleta} - {estado}")
    else:
        print("\nAinda não há atletas cadastrados.\n")
    input()

def menu_principal():
    atletas = {}
    while True:
        clear_console()
        print("\n** Menu Principal **")
        print("1. Cadastrar Atleta")
        print("2. Excluir Atleta")
        print("3. Pesquisar por Nome")
        print("4. Alterar esporte")
        print("5. Exibir Dicionário Completo")
        print("6. Sair\n")

        opcao = int(input('Digite a sua escolha: '))

        if opcao == 1:
            clear_console()
            atletas = cadastrar_atleta(atletas)

        elif opcao == 2:
            clear_console()
            atletas = excluir_atleta(atletas)

        elif opcao == 3:
            clear_console()
            pesquisar_atleta(atletas)

        elif opcao == 4:
            clear_console()
            alterar_atleta(atletas)

        elif opcao == 5:
            clear_console()
            exibir_dicionario(atletas)

        elif opcao == 6:
            clear_console()
            break

        else:
            print('\nOpção inválida. Tente novamente.\n')
menu_principal()
