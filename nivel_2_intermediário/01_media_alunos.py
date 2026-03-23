def media_notas (*notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma/quantidade

def situacao_do_aluno(media):
    if media >= 7:
        print(f"A média do aluno é: {media:.2f}\nAprovado")
    elif media >= 5:
        print(f"A média do aluno é: {media:.2f}\nRecuperação")
    else:
        print(f"A média do aluno é: {media:.2f}\nReprovado")

quantidade = int(input("Quantas notas irá informar? "))

notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = media_notas(*notas)
situacao_do_aluno(media)

