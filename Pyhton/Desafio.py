# ==============================================================================
# Exercício 1: O Clássico "FizzBuzz"
# ==============================================================================
print("--- Exercício 1 ---")
for numero in range(1, 51):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)

# ==============================================================================
# Exercício 2: O Caracol no Poço
# ==============================================================================
print("\n--- Exercício 2 ---")
profundidade = 10
posicao_atual = 0
dias = 0

while posicao_atual < profundidade:
    dias += 1
    posicao_atual += 3  # Sobe durante o dia
    
    if posicao_atual >= profundidade:
        break  # Se já atingiu o topo de dia, não escorrega à noite
        
    posicao_atual -= 2  # Escorrega à noite

print(f"O caracol levou {dias} dias para sair do poço.")

# ==============================================================================
# Exercício 3: A Bolinha de Borracha
# ==============================================================================
print("\n--- Exercício 3 ---")
altura = 20.0
quiques = 0

while altura >= 0.1:
    altura = altura * 0.5
    quiques += 1

print(f"A bolinha quicou {quiques} vezes até o quique ser menor que 0.1 metro.")

# ==============================================================================
# Exercício 4: O Detetive de Números Primos
# ==============================================================================
print("\n--- Exercício 4 ---")
def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(f"O número 7 é primo? {e_primo(7)}")
print(f"O número 11 é primo? {e_primo(11)}")
print(f"O número 4 é primo? {e_primo(4)}")

# ==============================================================================
# Exercício 5: O Caixa Eletrônico Inteligente
# ==============================================================================
print("\n--- Exercício 5 ---")
def calcular_notas(valor_saque):
    print(f"Valor do saque: R$ {valor_saque}")
    
    notas_50 = valor_saque // 50
    valor_saque = valor_saque % 50
    
    notas_20 = valor_saque // 20
    valor_saque = valor_saque % 20
    
    notas_10 = valor_saque // 10
    valor_saque = valor_saque % 10
    
    notas_1 = valor_saque // 1
    
    print(f"Notas de R$ 50: {notas_50}")
    print(f"Notas de R$ 20: {notas_20}")
    print(f"Notas de R$ 10: {notas_10}")
    print(f"Notas de R$ 1: {notas_1}")

calcular_notas(138)

# ==============================================================================
# Exercício 6: Inversor de Senhas (Palíndromo)
# ==============================================================================
print("\n--- Exercício 6 ---")
def verificar_palindromo(palavra):
    palavra_invertida = ""
    for i in range(len(palavra) - 1, -1, -1):
        palavra_invertida += palavra[i]
        
    if palavra == palavra_invertida:
        return True
    else:
        return False

print(f"arara é palíndromo? {verificar_palindromo('arara')}")
print(f"python é palíndromo? {verificar_palindromo('python')}")

# ==============================================================================
# Exercício 7: O Salário Flutuante
# ==============================================================================
print("\n--- Exercício 7 ---")
def calcular_salario(valor_inicial):
    salario_mes1 = valor_inicial * 1.10  # +10%
    salario_final = salario_mes1 * 0.90  # -10% sobre o novo valor
    return salario_final

resultado = calcular_salario(1000.00)
print(f"Salário Final: R$ {resultado:.2f}")

# EXPLICAÇÃO MATEMÁTICA:
# O valor final não voltou para R$ 1.000,00 porque os 10% de desconto no segundo
# mês foram aplicados sobre o salário já reajustado (R$ 1.100,00) e não sobre o
# valor inicial. Tirar 10% de 1100 significa perder R$ 110,00, resultando em R$ 990,00.
# Matematicamente: 1000 * 1.10 * 0.90 = 1000 * 0.99 = 990.

# ==============================================================================
# Exercício 8: O Validador de Anos Bissextos
# ==============================================================================
print("\n--- Exercício 8 ---")
def e_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

for ano in range(1890, 2011):
    if e_bissexto(ano):
        print(f"Ano bissexto: {ano}")

# ==============================================================================
# Exercício 9: A Caminhada Fracionada (O Loop Interminável)
# ==============================================================================
print("\n--- Exercício 9 ---")
x = 0.0
while x != 1.0:
    # O round() limpa as imprecisões de ponto flutuante da norma IEEE 754,
    # que faziam com que o número nunca crava-se exatamente em 1.0.
    x = round(x + 0.1, 1)
    print(x)

# ==============================================================================
# Exercício 10: A Soma dos Dígitos (Modo Hardcore)
# ==============================================================================
print("\n--- Exercício 10 ---")
numero = 451
soma = 0

print(f"Calculando a soma dos dígitos de: {numero}")

while numero > 0:
    digito = numero % 10    # Pega o último algarismo
    soma += digito          # Soma o algarismo extraído
    numero = numero // 10   # Remove o último algarismo usando divisão inteira

print(f"A soma dos dígitos é: {soma}")