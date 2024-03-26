import heapq  # Para usar funções de fila e pilha

import time
import sys, os 

class Pilha:
    def __init__(self):
        self.pilha = []

    def adicionar_elemento(self, elemento):
        self.pilha.append(elemento)
        return "Elemento adicionado com sucesso!"
        input()

    def remover_elemento(self):
        if not self.esta_vazia():
            return self.pilha.pop()
        else:
            return "A pilha está vazia. Não há itens para remover."
            input()

    def exibir_ultimo_elemento(self):
        if not self.esta_vazia():
            return f"O último elemento na pilha é: {self.pilha[-1]}"
            input()
        else:
            return "A pilha está vazia. Não há itens para exibir."
            input()

    def esta_cheia(self):
        return len(self.pilha) >= 3  # Suponhamos que a pilha pode conter no máximo 100.000 itens

    def esta_vazia(self):
        return len(self.pilha) == 0

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    pilha = Pilha()

    while True:
        clear_console()
        print("Escolha uma opção:")
        print("[1] - Criar a pilha")
        print("[2] - Adicionar um elemento na pilha")
        print("[3] - Remover um item da pilha")
        print("[4] - Exibir o último elemento na pilha")
        print("[5] - Informa se a pilha está cheia")
        print("[6] - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            resultado = pilha.adicionar_elemento(0)
            print(resultado)
            input()

        elif opcao == 2:
            elemento = str(input("Digite a palavra para adicionar na pilha: "))
            resultado = pilha.adicionar_elemento(elemento)
            print(resultado)
            input()

        elif opcao == 3:
            resultado = pilha.remover_elemento()
            print(resultado)
            input()

        elif opcao == 4:
            resultado = pilha.exibir_ultimo_elemento()
            print(resultado)
            input()

        elif opcao == 5:
            resultado = pilha.esta_cheia()
            print(resultado)
            input()

        elif opcao == 6:
            break

        elif not (1 <= opcao <= 6):
            print("Opção inválida! Por favor, escolha uma das opções disponíveis.")
            input()
menu_principal()

