##################################################################################
# Aluno: Nicolas Pereira 
# Disciplina: 1402044 - ESTRUTURA DE DADOS
##################################################################################
# Programa em Python Verificação de Expressões Matemáticas
##################################################################################

from collections import deque
import sys, os 

pilha = deque() 
verificar = False

def verificadora(expressao):
    pilha = []  # iniciando a pilha vazia
    for char in expressao:
        if char == '(':
            pilha.append('(')  # adicionando ( à pilha
        elif char == ')':
            try:
                if not pilha.pop() == '(':
                    return False  # erro, não está balanceado
            except IndexError:
                    print("Esta expressão não está balanceada! Pressione para repetir:")
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    verificar = True
                    main()
        else:
            continue   # ignorar caracteres que não são parênteses
    return not pilha  # retornar True se a expressão estiver balanceada

def main():
    expressao = input("Por favor, escreva uma expressão matemática: ") 
    if verificadora(expressao) == True and verificar == False:
        print("Esta expressão está balanceada, Parabéns!:")
        print("{}".format(expressao))
    else:
        print("Esta expressão não está balanceada! Pressione para repetir:")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
   
if __name__ == "__main__":
    main()










