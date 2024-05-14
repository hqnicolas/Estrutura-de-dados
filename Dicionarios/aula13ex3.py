# 3 – Desenvolva um script em linguagem Python,
# utilizando Dicionários, que solicite ao usuário inserir
# o nome de 05 livros e seus respectivos autores e os mostre na tela.

import os

livros = {}

for f in range(1, 6):
    os.system('cls' if os.name == 'nt' else 'clear')
    nome_livro = input("Digite o nome do {}° livro: ".format(f))
    livros[nome_livro] = {}
    autor = input("Digite o nome do autor: ")
    livros[nome_livro]["autor"] = autor

print("\nLista de Livros:")
for i, (nome_livro, autor) in enumerate(livros.items()):
    print(f"{i+1} - {nome_livro} ({autor})")
input()
