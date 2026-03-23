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

alunos = []

quantidade_alunos = int(input("Quantos alunos você quer cadastrar? "))

for i in range(quantidade_alunos):
    nome = input(f"\nDigite o nome do aluno{i+1}: ")
    notas = []
    quantidade_de_notas = int(input(f"Quantas notas o aluno {nome} possui? "))

    for j in range(quantidade_de_notas):
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas.append(nota)
    alunos.append([nome, notas])

for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]
    media = media_notas(*notas)
    print(f"\nAluno: {nome}")
    situacao_do_aluno(media)