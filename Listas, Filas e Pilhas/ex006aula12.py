##############################################################################################
# Faça um Programa Python que leia a idade das pessoas, armazene a informação
#  na sua respectiva lista. Mostre ao final a lista das idades na ordem menor para maior.
##############################################################################################
idades = []

while True:
    idade = input("digite a idade idade (ou digite 'x' para sair): ")
    if idade == "x":
        break
    try:
        idade = int(idade)
        idades.append(idade)
    except ValueError:
        print("Digite um número")

idades.sort()

print("idades em ordem ascendente: ", idades)
