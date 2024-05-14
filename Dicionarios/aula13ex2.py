# 2 – Desenvolva um script em linguagem Python, 
# utilizando Dicionários, que solicite ao usuário inserir o nome de 05 produtos
# de papelaria e seus respectivos preços e os mostre na tela.
import sys, os 

produtos = {}

for f in range(1, 6):
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Digite o nome do {}° produto: ".format(f))
    produtos[nome] =  input("Digite o preço do ítem: {}: ".format(nome))

print("\nLista de produtos:")
for i, (nome, preco) in enumerate(produtos.items()):
    print("{} - {} - R$ {}".format(i+1, nome, preco))

input()