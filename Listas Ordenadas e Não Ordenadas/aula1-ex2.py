####################################################################
# Criar um novo programa.
# 1- Inserir elementos em uma lista
# 2- Pesquisar um elemento na lista
# 3- Excluir um elemento da lista
# 4 – Imprimir a lista
#####################################################################

import os

def insert_element(list, element):
    list.append(element)

def search_element(list, element):
    if element in list:
        os.system('cls')
        print("Elemento encontrado.")
        i = (input("Anotou? "))
    else:
        os.system('cls')
        print("Elemento não encontrado.")
        i = (input("Anotou? "))
        
def delete_element(list, element):
    if element in list:
        os.system('cls')
        list.remove(element)
    else:
        os.system('cls')
        print("Elemento não encontrado na lista para exclusão.")

def print_list(list):
    os.system('cls')
    for i in list:
        print(i, end=" ")
    print() # Para pular uma linha após a impressão da lista.
    
# Teste das funções:
myList = []
while True:
    print("\nMenu:\n1- Inserir elementos\n2- Pesquisar um elemento\n3- Excluir um elemento\n4 – Imprimir a lista\n5 - Sair")
    choice = int(input("Escolha uma opção: "))
    
    if choice == 1:
        os.system('cls')
        element = input("Digite o elemento para inserir: ")
        insert_element(myList, element)
        
    elif choice == 2:
        os.system('cls')
        element = input("Digite o elemento para pesquisar: ")
        search_element(myList, element)
    
    elif choice == 3:
        os.system('cls')
        element = input("Digite o elemento para excluir: ")
        delete_element(myList, element)
        
    elif choice == 4:
        os.system('cls')
        print_list(myList)
        i = (input("Anotou? "))

      
    elif choice == 5:
        break;
    
    else:
        os.system('cls') 
        print ("Opção inválida.")