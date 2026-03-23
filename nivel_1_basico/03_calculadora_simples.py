#solicitar dois números de entrada para realizar as operações

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
operacao = input("Informe a operação matemática entre +, -, *, /: ")

# Verifica qual operação foi escolhida

if operacao == "+":
    print(f"A soma de {numero1} e {numero2} é: {numero1 + numero2}")
elif operacao == "-":
    print(f"A subtração de {numero1} e {numero2} é: {numero1 - numero2}")
elif operacao == "*":
    print(f"A multiplicação de {numero1} e {numero2} é: {numero1 * numero2}")
elif operacao == "/":
    if numero2 != 0:
        print(f"A divisão de {numero1} e {numero2} é: {numero1 / numero2}")
    else:
        print("Erro: divisão por zero não é permitida")

else:
    print("Não foi possível realizar sua operação matemática")