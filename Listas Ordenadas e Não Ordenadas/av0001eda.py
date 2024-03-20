##################################################################################
# Aluno: Nicolas Pereira
# Disciplina: ESTRUTURA DE DADOS
# christine.vieira@satc.edu.br
##################################################################################
# Programa em Python
##################################################################################
# 1- Inserir elementos em uma lista
#    a) Inserir 
#    b) Inserir em um posição 
# 2- Pesquisar um elemento na lista individualmente
#    a) Pelo valor  
#    b) Pela posição 
# 3- Excluir um elemento da lista
#    a) Pelo valor 
#    b) Pela posição  
# 4 – Imprimir a lista
# 0 – Encerrar o programa.
# X - Encerrar o programa.
##################################################################################

import os

def menu_mostra(): # função responsável por exibir o menu na tela do usuário
    print('1- Inserir elementos em uma lista')
    print('2- Pesquisar um elemento na lista individualmente')
    print('3- Excluir um elemento da lista')
    print('4- Imprimir a lista')
    print('0- Encerrar o programa')


def menu_resolve(lst): # função responsável por tratar o submenu de inserção
    submenu = input("a) Inserir\nb) Inserir em um posição\nEscolha a opção: ")
    if submenu == 'a':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        elem = str(input('Digite o elemento que deseja inserir: '))
        lst.append(elem)
    elif submenu == 'b':
        try:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            pos = int(input('Digite a posição onde deseja inserir: '))
            if pos > len(lst):
                pos = (len(lst) +1)
                print("\nesta posição é maior que o ultimo elemento, será inserida no final")
            elem = str(input('Digite o elemento que deseja inserir: '))
            lst.insert(pos, elem)
        except ValueError:
            print("\nDigite um número inteiro!")
            input()
    else:
        print("\n\nDigite somente a ou b, ok?")
        input()
        menu_resolve(lst)

        
def pesquisa_resolve(lst): # função responsável por tratar o submenu de pesquisa
    submenu = input("a) Pelo valor\nb) Pela posição\nEscolha a opção: ")
    if submenu == 'a':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        elem = str(input('Digite o elemento que deseja buscar: '))
        if elem in lst:
            print("Elemento encontrado na lista e sua posição é: ", lst.index(elem) + 1)
        else:
            print("Elemento não encontrado na lista")
        input()
    elif submenu == 'b':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        pos = int(input('Digite a posição que deseja procurar: '))
        if pos < len(lst):
            print("Na posição", pos, "está o elemento", lst[pos])
            input()
        else:
            print("Posição não encontrada")
            input()
    else:
        print("\n\nDigite somente a ou b, ok?")
        input()
        pesquisa_resolve(lst)
        
def delete_resolve(lst):
    submenu = input("a) Pelo valor\nb) Pela posição\nEscolha a opção: ")
    if submenu == 'a':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        elem = str(input('Digite o elemento que deseja excluir: '))
        index = lst.index(elem) if elem in lst else None
        if index is not None:
            print("Elemento excluído: " + elem)
            lst.remove(elem)
        else:
            print("Elemento não foi encontrado")
        input()
    elif submenu == 'b':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        pos = int(input('Digite a posição que deseja excluir: '))
        if pos < len(lst):
            del lst[pos]
            print('Lista:', lst)
            print('\n\nPressione qualquer tecla para sair.')
            input()
        else:
            print("Posição não encontrada")
            input()
    else:
        print("Opção inválida.")
        input()
        
def main():
    lst = []
    while True:
        if os.name == 'posix':      # eu fiz este programa em Linux
            os.system('clear')      # na minha maquina este aqui funciona
        elif os.name == 'nt':       # provavelmente vai ser testado em Windows
            os.system('cls')        # em uma maquina windows funciona assim
        menu_mostra()
        option = input('\nDigite uma das opções acima: ')
        if option == '1':
            menu_resolve(lst)      # Quando o usuário seleciona 1- inserir elementos em uma lista
        elif option == '2':
            pesquisa_resolve(lst)  # Quando o usuário seleciona 2- Pesquisar um elemento na lista individualmente
        elif option == '3':
            delete_resolve(lst)    # Quando o usuário seleciona 3- Excluir um elemento da lista 
        elif option == '4':
            if os.name == 'nt':    # Quando o usuário seleciona 4– Imprimir a lista
                os.system('cls')
            else:
                os.system('clear') # na minha maquina este aqui funciona
            print('Lista:', lst)
            print('\n\nPressione qualquer tecla para sair.')
            input()
        elif option in ('0', 'X', 'x'):
            break                  # Quando o usuário seleciona 0- Encerrar o programa
        else:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            menu_mostra()
            print("Digite somente um dos numero exibidos acima, ok?")
            input()
            
main()                            # chama a função principal em loop
