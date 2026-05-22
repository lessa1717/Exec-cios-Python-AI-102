#Exercício 01
numero = int(input("Digite um número inteiro para ver a tabuada: "))

print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")