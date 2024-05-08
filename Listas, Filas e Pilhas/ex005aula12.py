numeros = []
par = []
impar = []

while True:
   num = int(input("Digite um número (0 para parar): "))
   if num == 0:
       break
   numeros.append(num)

for number in numeros:
   if number % 2 == 0:
       par.append(number)
   else:
       impar.append(number)

print("Números pares:", par)
print("Números ímpares:", impar)
