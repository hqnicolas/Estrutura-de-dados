##############################################################################################
# Faça um Programa Python que leia uma frase (caracteres), e diga quantas vogais e consoantes 
# foram lidas. Mostre a lista ao final.
##############################################################################################
def contar_vogais_consoantes(frase):
   vogais = 0
   consoantes = 0
      
   for letra in frase:
        if letra in 'aeiouAEIOU':
            vogais += 1
        else:
            consoantes += 1
        
   
   print(f"Frase: {frase}")
   print(f"Número vogais: {vogais}")
   print(f"Número consoantes: {consoantes}")

def main():
   frase = input("Digite uma frase: ")
   contar_vogais_consoantes(frase)

if __name__ == "__main__":
   main()
