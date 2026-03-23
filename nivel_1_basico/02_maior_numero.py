numero1 = int(input("Informe o primeiro número inteiro: "))
numero2 = int(input("Informe o segundo número inteiro: "))

if numero1 > numero2:
    print(f"Número {numero1} é maior que {numero2}.")
elif numero2 > numero1:
    print(f"Número {numero2} é maior que {numero1}.")
else:
    print(f"Os números {numero1} e {numero2} são iguais.")
