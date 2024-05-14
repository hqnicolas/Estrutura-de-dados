##############################################################################################
#Crie um dicionário com os nomes de times de futebol de SC, seguindo exemplo:
#times = {1: “Criciuma”,  2: “Avai”,  3: “Marcilio Dias”, 4: “Joinville”, 
#                5: “Figueirense”,  6: “Chapecoense”,  7: “Brusque”, 8: “Metropolitano”
#                9: “Hercílio Luz”, 10: “Inter de Lages” }
#Agora, inclua um novo time no final da lista 
#Mostre em qual posição está o time  “Joinville”. 
#Infelizmente o time “Avaí” não fazem mais parte da lista e deve ser removida.
#Ao final, mostre a lista completa de times.
##############################################################################################

import sys, os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_time(times):
    nome_time = input("\nDigite o nome do time que deseja cadastrar: ")
    if nome_time not in times:
        if not times:
            max_posicao = 1
        else:
            max_posicao = len(times) + 1
        posicao_time = max_posicao
        times[posicao_time] = nome_time
        print(f"\nTime {nome_time} cadastrado com sucesso na posição {max_posicao}!")
    else:
        print("\nO time já está cadastrado. Tente novamente.")
    input()
    return times

def excluir_time(times):
    excluir_time = input("\nDigite o nome do time que deseja excluir: ")
    for posicao_time, nome_time in times.items():
        if nome_time == excluir_time:
            del times[posicao_time]
            print(f"\nInfelizmente o time {excluir_time} não faz mais parte da lista e foi removido.\n")
            break
    else:
        print("\nO time que você tentou excluir não está na sua lista.\n")
    input()
    return times

def pesquisar_time(times):
    i = False
    qual_time = input("\nDigite o nome do time que deseja pesquisar: ")
    for posicao_time, nome_time in times.items():
        if nome_time == qual_time:
            i = True
            print(f"\nO time {qual_time} está na posição {posicao_time}\n")    
    if i == False:        
        print("\nO time que você pesquisou não está na sua lista.\n")
    input()

def exibir_dicionario(times):
    if len(times) > 0:
        print('\n** Dicionário de Times **')
        for nome_time, posicao_time in times.items():
            print(f"{nome_time} - {posicao_time}")
    else:
        print("\nAinda não há times cadastrados.\n")
    input()

def menu_principal():
    times = {}
    while True:
        clear_console()
        print("\n** Menu Principal **")
        print("1. Cadastrar Time")
        print("2. Excluir Time")
        print("3. Pesquisar por Nome")
        print("4. Exibir Dicionário Completo")
        print("0. Sair\n")

        opcao = int(input('Digite a sua escolha: '))

        if opcao == 1:
            clear_console()
            times = cadastrar_time(times)

        elif opcao == 2:
            clear_console()
            times = excluir_time(times)

        elif opcao == 3:
            clear_console()
            pesquisar_time(times)


        elif opcao == 4:
            clear_console()
            exibir_dicionario(times)

        elif opcao == 0:
            clear_console()
            break

        else:
            print('\nOpção inválida. Tente novamente.\n')
            input()

menu_principal()
