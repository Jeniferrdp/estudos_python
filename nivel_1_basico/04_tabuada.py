#solicitar número de entrada
numero = float(input("informe um numero: "))

# Mostra a tabuada do número informado
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
