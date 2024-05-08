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
