##############################################################################################
# As listas são uma parte fundamental da linguagem Python e são amplamente
# utilizadas em muitos contextos diferentes, desde manipulação de dados simples até
# implementação de algoritmos mais complexos.
##############################################################################################
#Criando uma lista vazia para armazenar os dicionários

lista_pessoas = []  # Crie uma lista de dicionários vazia para armazenar os dados das pessoas

while True:
    nome = input("Informe o nome da pessoa (ou digite 'O' para encerrar): ")

    if nome.upper() == 'O':  # Use a expressão regular ou converter a entrada para maiúsculas
        break
    
    idade = int(input("Informe a idade da pessoa: "))  # Convertendo a entrada para inteiro
    
    cidade = input("Informe a cidade da pessoa: ")

    # Criando um dicionário com os dados informados e adicionando-o à lista
    lista_pessoas.append({"nome": nome, "idade": idade, "cidade": cidade})

    print("Lista de pessoas:{}". format(lista_pessoas)) 
for i, pessoa in enumerate(lista_pessoas, start=1):
   print(f"{i}. Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")