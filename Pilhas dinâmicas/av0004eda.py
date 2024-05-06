##################################################################################
# Aluno: Nicolas Borba Pereira 
# Disciplina: 1402044 - ESTRUTURA DE DADOS
##################################################################################
# Programa em Python Gerenciamento de uma lanchonete 
##################################################################################

from collections import deque
import sys, os 

class Lanchonete:
    def __init__(self):
        self.pedidos = deque()
        
    def fazer_pedido(self):
        pedido = input("Digite seu pedido: ")
        self.pedidos.append(pedido)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def processar_pedido(self):
        print('Pedidos em fila para serem processados:')
        for i, pedido in enumerate(lanchonete.pedidos, 1):
            print(f'{i}. {pedido}')
        if not self.pedidos:
            print('Não há pedidos pendentes')
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            elemento_removido = self.pedidos.popleft()
            print("Pressione para Processar e remover o pedido: {}".format(elemento_removido))
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
    
    def remover_pedido(self):
        try:
            while True:
                numero = int(input("\nDigite o número do pedido que deseja remover (ou 0 para cancelar): "))
                if numero == 0 or len(self.pedidos) <= numero - 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    self.pedidos.popleft()
                    print(f"Pedido {numero} removido com sucesso.")
                    input()
                    break
        except ValueError:
            print("Por favor, digite um número válido.")

    def primeiro_pedido(self):
        if not self.pedidos:
            print('Não há pedidos pendentes')
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Proximo pedido da fila: {}".format(self.pedidos[0]))
            input()
            os.system('cls' if os.name == 'nt' else 'clear')        
    
    def mostrar_pedidos(self):
        if not self.pedidos:
            print('Não há pedidos pendentes')
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            for i, pedido in enumerate(self.pedidos, 1):
                print(f'{i}. {pedido}')
            input()
            os.system('cls' if os.name == 'nt' else 'clear')

lanchonete = Lanchonete()
while True:
    print("\n**** Lanchonete ****\n")
    print("1. Fazer Pedido")
    print("2. Atender Pedido")
    print("3. Consultar todos os Pedidos")
    print("4. Consultar próximo da fila")
    print("5. Remover um elemento da fila")
    print("6. Sair\n")
    
    opcao = int(input("Digite sua opção: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if opcao == 1:
        lanchonete.fazer_pedido()
    elif opcao == 2:
        lanchonete.processar_pedido()
    elif opcao == 3:
        lanchonete.mostrar_pedidos()
    elif opcao == 4:
        lanchonete.primeiro_pedido()
    elif opcao == 5:
        lanchonete.remover_pedido()    
    elif opcao == 6:    
        break
    else:
        print("Opção inválida")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')