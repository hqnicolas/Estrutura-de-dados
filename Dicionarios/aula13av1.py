##############################################################################################
#Crie um Dicionário com os nomes de séries de TV seguindo o exemplo:
#series = ("Black Mirror", "Breaking Bad", "Friends", "Game of Thrones", 
#                "The Big Bang Theory”, “House”,  “The Last of Us”, “One Piece”,
#                “Grey's Anatomy”, “Stranger Things” )
#Agora, inclua uma nova série no final da lista 
#Mostre em qual posição está a série  “One Piece”. 
#Infelizmente a série “House” não fazem mais parte da lista e deve ser removida.
#Ao final, mostre a lista completa de séries.
##############################################################################################

import sys, os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_serie(series):
    nome_serie = input("\nDigite o nome da série que deseja cadastrar: ")
    if nome_serie not in series:
        if not series:
            max_posicao = 1
        else:
            max_posicao = len(series) + 1
        series[nome_serie] = max_posicao
        print(f"\nSérie {nome_serie} cadastrada com sucesso na posição {max_posicao}!")
    else:
        print("\nA série já está cadastrada. Tente novamente.")
    input()
    return series

def excluir_serie(series):
        nome_serie = input("\nDigite o nome da série que deseja excluir: ")  
        if nome_serie in series:
            del series[nome_serie]
            print(f"\nInfelizmente a série {nome_serie} não faz mais parte da lista e foi removida.\n")
        else:
            print("\nA série que você tentou excluir não está na sua lista.\n")
        input()
        return series

def exibir_serie(series):
        nome_serie = input("\nDigite o nome da série que deseja pesquisar: ")   
        if nome_serie in series:
            print(f"\nA série {nome_serie} está na posição #{series[nome_serie]} da sua lista.\n")
        else:
            print("\nA série que você pesquisou não está na sua lista.\n")
        input()

def listar_serie(series):
        if len(series) > 0:
                print('\n** Séries Cadastradas **')
                for serie, posicao in series.items():
                    print(f"{serie} está na posição {posicao}")
        else:
                print("\nAinda não há séries cadastradas.\n")
        input()

def menu_principal():
    series = {}
    while True:
        clear_console()
        print("\n** Menu Principal **")
        print("1. Cadastrar Série")
        print("2. Excluir Série")
        print("3. Pesquisar por Nome")
        print("4. Exibir Dicionário Completo")
        print("5. Sair\n")
        
        opcao = int(input('Digite a sua escolha: '))
        
        if opcao == 1:
            series = cadastrar_serie(series)
        
        elif opcao == 2:
            series = excluir_serie(series)
        
        elif opcao == 3:
             exibir_serie(series)
        
        elif opcao == 4:
            listar_serie(series)
        
        elif opcao == 5:
            break
            
        else:
            print('\nOpção inválida. Tente novamente.\n')
            input()

menu_principal()