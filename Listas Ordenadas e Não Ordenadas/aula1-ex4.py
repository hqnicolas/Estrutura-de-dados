####################################################################################
# Este programa permite que você insira elementos em uma lista,
# pesquise por elementos na lista e exclua elementos da lista.
# Quando você escolhe a opção "Imprimir o vetor",
# ele imprime todos os elementos da lista atual. 
# A opção "Encerrar o programa" encerra o programa.
####################################################################################

# Criando uma lista vazia
my_list = []

def insert(element):
    my_list.append(element)

def insert_position(element, position):
    if position < len(my_list):
        my_list.insert(position, element)
    else:
        print("Posição inválida")

def search_value(value):
    return my_list.index(value) if value in my_list else "Valor não encontrado"

def search_position(position):
    return my_list[position] if 0 <= position < len(my_list) else "Posição inválida"

def delete_value(value):
    if value in my_list:
        my_list.remove(value)
    else:
        print("Valor não encontrado")

def delete_position(position):
    if 0 <= position < len(my_list):
        del my_list[position]
    else:
        print("Posição inválida")

def print_list():
    print(my_list)

while True:
    print("\n1- Inserir elementos em uma lista\n2- Pesquisar um elemento na lista\n3- Excluir um elemento da lista\n4 - Imprimir o vetor\n0 - Encerrar o programa.")
    option = int(input("Escolha uma opção: "))
    
    if option == 1:
        element = input("Digite o elemento a ser inserido: ")
        position_option = input("Deseja inserir no final da lista ou em uma posição específica? (f/p): ")
        
        if position_option == 'f':
            insert(element)
        elif position_option == 'p':
            position = int(input("Digite a posição: "))
            insert_position(element, position)
            
    elif option == 2:
        value_or_position = input("Você deseja procurar pelo valor ou pela posição? (v/p): ")
        
        if value_or_position == 'v':
            value = input("Digite o valor a ser pesquisado: ")
            print(search_value(value))
            
        elif value_or_position == 'p':
            position = int(input("Digite a posição a ser pesquisada: "))
            print(search_position(position))
    
    elif option == 3:
        value_or_position = input("Você deseja excluir pelo valor ou pela posição? (v/p): ")
        
        if value_or_position == 'v':
            value = input("Digite o valor a ser excluído: ")
            delete_value(value)
            
        elif value_or_position == 'p':
            position = int(input("Digite a posição a ser excluída: "))
            delete_position(position)
    
    elif option == 4:
        print_list()
        
    elif option == 0:
        break
