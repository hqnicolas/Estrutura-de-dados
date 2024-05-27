# Desenvolver um programa Python para criar uma Árvore Binária com a sequência, de pai para filho:
# Arvore = {43,11,62,9,41,48,95}
# Após, um menu com as opções:
# Incluir: adicionar um novo nó na árvore criada (informado pelo usuário).
# Excluir: remover um nó que já exista na arvore (se não existir, exibir mensagem).
# Pesquisar: mostrar os nós existente na arvore.

import sys, os

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

class Node:
    def __init__(self, value):
        self.value = value
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def inserir(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._inserir(value, self.root)

    def _inserir(self, value, node):
        if value < node.value:
            if node.esquerda:
                self._inserir(value, node.esquerda)
            else:
                node.esquerda = Node(value)
        elif value > node.value:
            if node.direita:
                self._inserir(value, node.direita)
            else:
                node.direita = Node(value)

    def pesquisa(self, value):
        return self._pesquisa(value, self.root)

    def _pesquisa(self, value, node):
        if not node:
            return None
        elif value == node.value:
            return node
        elif value < node.value:
            return self._pesquisa(value, node.esquerda)
        else:
            return self._pesquisa(value, node.direita)

    def delete(self, value):
        self.root = self._delete(value, self.root)
    
    def print_arvores(self, node, level=0):
        if node is not None:
            self.print_arvores(node.direita, level + 2)
            print(' ' * 8 * level + '->', node.value)
            self.print_arvores(node.esquerda, level + 2)

    def display_arvores(self):
        print("Árvore Binária:")
        self.print_arvores(self.root)

    def _delete(self, value, node):
        if not node:
            return None
        elif value == node.value:
            if not node.esquerda and not node.direita:
                return None
            elif not node.esquerda:
                return node.direita
            elif not node.direita:
                return node.esquerda
            else:
                min_value = self._find_min(node.direita)
                node.value = min_value
                node.direita = self._delete(min_value, node.direita)
        elif value < node.value:
            node.esquerda = self._delete(value, node.esquerda)
        else:
            node.direita = self._delete(value, node.direita)
        return node

    def _find_min(self, node):
        while node.esquerda:
            node = node.esquerda
        return node.value

def main():
    arvores = ArvoreBinaria()
    arvores.inserir(43)
    arvores.inserir(11)
    arvores.inserir(62)
    arvores.inserir(9)
    arvores.inserir(41)
    arvores.inserir(48)
    arvores.inserir(95)

    while True:
        limpa()
        print("\nEscolha uma opção:")
        print("[1] - Incluir um novo nó")
        print("[2] - Excluir um nó")
        print("[3] - Pesquisar um valor")
        print("[4] - Exibir árvore")
        print("[5] - Sair")

        option = int(input("Escolha uma opção: "))

        if option == 1:
            limpa()
            value = int(input("Digite o valor a ser incluido: "))
            arvores.inserir(value)
        
        elif option == 2:
            limpa()
            value = int(input("Digite o valor a ser excluido: "))
            node = arvores.pesquisa(value)
            if node:
                arvores.delete(value)
                print(f"Valor {value} excluído com sucesso!")
            else:
                print(f"Valor {value} não encontrado na árvore.")
        
        elif option == 3:
            limpa()
            value = int(input("Digite o valor a ser pesquisado: "))
            node = arvores.pesquisa(value)
            if node:
                print(f"Valor {value} encontrado na árvore!")
            else:
                print(f"Valor {value} não encontrado na árvore.")
        
        elif option == 4:
            limpa()
            arvores.display_arvores()
            input()
        
        elif option == 5:
            limpa()
            break
        
        else:
            limpa()
            print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

if __name__ == "__main__":
    main()
