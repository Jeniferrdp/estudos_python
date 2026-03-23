#solicitar as 3 notas do aluno
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

#calcular a media
media = (nota1 + nota2 + nota3)/3

# Calcula a média e informa se o aluno está aprovado ou reprovado
if media >= 7:
    print(f"Média: {media:.2f}\nAprovado")
else:
    print(f"Média: {media:.2f}\nReprovado")