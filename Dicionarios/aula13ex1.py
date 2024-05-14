# 1 – Elabore um script em  linguagem Python,
# utilizando Dicionários, que contenha 4 funcionários,
# com o índice numérico e seu nome.
# Em seguida, solicite do usuário demitir um dos funcionários
# conforme o número de cadastro e mostre na tela os funcionários restantes.

import sys, os 

funcionarios = {}

for f in range(1, 5):
    os.system('cls' if os.name == 'nt' else 'clear')
    funcionarios[f] = input("Digite o nome do funcionário {}: ".format(f))

os.system('cls' if os.name == 'nt' else 'clear')
print("Funcionários:")
for i, nome in funcionarios.items():
    print("{} - {}".format(i, nome))

num_funcionario_demissao = int(input("Insira o número do funcionário que deseja demitir: "))

if num_funcionario_demissao in funcionarios:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O funcionário {} {} foi demitido.".format(num_funcionario_demissao, funcionarios[num_funcionario_demissao]))
    del funcionarios[num_funcionario_demissao]
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Funcionário não encontrado!")
os.system('cls' if os.name == 'nt' else 'clear')
print("\nFuncionários restantes:")
for i, nome in funcionarios.items():
    print("{} - {}".format(i, nome))
input()