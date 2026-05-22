#Exercicio - 09
def criptografar_texto(palavra):
    nova_palavra = ""
    vogais = "aeiouAEIOU"

    for letra in palavra:
        if letra in vogais:
            nova_palavra += "*"
        else:
            nova_palavra += letra
    return nova_palavra

texto_usuario = input("Digite uma palavra ou frase para criptografar:")
resultado = criptografar_texto(texto_usuario)
print(f"\nTexto original: {texto_usuario}")
print(f"\nTexto protegido: {resultado}")