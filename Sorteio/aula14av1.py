######################################################
# davi Sartor
# Nicolas Pereira
# Engenharia de Computação - SATC
# Estrutura de dados
######################################################

import sys, os


def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

class listarNumeros:

    def __init__(self):
        self.numeros = []

    def adicionar_numeros(self) -> None:
        while True:
            qtd = int(input("Quantos itens você quer adicionar? Mínimo 10\n"))
            if qtd >= 10:
                break
            else:
                print("Quantidade de itens incorreta!!")
        for i in range(qtd):
            while True:
                try:
                    number = int(input(f"Digite o {i+1}º número da lista: "))
                    if not any(number == x for x in self.numeros):
                        self.numeros.append(number)
                        break
                    else:
                        print("Número já presente na lista. Por favor, digite outro.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro.")

    def mostrar_numeros(self) -> None:
        print("\nLista de números não ordenada:")
        for i, number in enumerate(self.numeros):
            print(f"{i+1}. {number}")
        n = len(self.numeros)
        for i in range(1, n):
            chave = self.numeros[i]
            j = i - 1
            while j >= 0 and self.numeros[j] > chave:
                self.numeros[j + 1] = self.numeros[j]
                j -= 1
            self.numeros[j + 1] = chave

        print("\nLista de números ordenada:")
        for i, number in enumerate(self.numeros):
            print(f"{i+1}. {number}")
        input("Pressione ENTER para continuar")
        

def main() -> None:
    lista_numeros = listarNumeros()

    while True:
        limpa()
        print("\nEscolha uma opção:")
        print("[1] - Adicionar até 10 elementos à lista")
        print("[2] - Visualizar elementos da lista")
        print("[3] - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            lista_numeros.adicionar_numeros()
        elif opcao == 2:
            lista_numeros.mostrar_numeros()
        elif opcao == 3:
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções disponíveis.")


if __name__ == "__main__":
    main()