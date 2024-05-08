def contar_vogais_consoantes(frase):
   vogais = 0
   consoantes = 0
   
   vogais_consoantes = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
   
   for letra in frase:
       if letra in vogais_consoantes:
           if letra in 'aeiouAEIOU':  # Verificando se é uma vogal
               vogais += 1
           else:  # É uma consoante
               consoantes += 1
   
   print(f"Frase: {frase}")
   print(f"Número vogais: {vogais}")
   print(f"Número consoantes: {consoantes}")

def main():
   frase = input("Digite uma frase: ")
   contar_vogais_consoantes(frase)

if __name__ == "__main__":
   main()
