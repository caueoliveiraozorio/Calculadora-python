# Calculadora Simples em Python (sem funções)

# Solicita entrada do usuário
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza as operações
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2

    # Trata divisão por zero
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Erro: Divisão por zero!"

    # Exibe os resultados
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")
except ValueError:
    print("Erro: Insira números válidos.")