#Exemplo com While
print("---Sistema de Cadastro---")

while True:
    resposta = input("Voce aceita os termos de uso? (S/N)").upper()

    if resposta == "S":
        print("Ótimo! Cadastro Liberado!")
        break #Fim do Loop
    elif resposta == "N":
        print("Que pena. Cadastro cancelado!")
        break
    else:
        print("Opçao inválida! por favor digite apenas S ou N")