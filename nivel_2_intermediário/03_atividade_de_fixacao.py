def media_notas(*notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

def situacao_do_aluno(media):
    if media >= 7:
        print(f"A média do aluno é: {media:.2f}\nAprovado")
    elif media >= 5:
        print(f"A média do aluno é: {media:.2f}\nRecuperação")
    else:
        print(f"A média do aluno é: {media:.2f}\nReprovado")


def analisar_alunos(alunos):
    maior_media = float('-inf')
    menor_media = float('inf')

    aluno_maior = ""
    aluno_menor = ""

    ranking = []

    for aluno in alunos:
        nome = aluno[0]
        notas = aluno[1]

        media = media_notas(*notas)

        print(f"\nAluno: {nome}")
        situacao_do_aluno(media)

        ranking.append([nome, media])

        if media > maior_media:
            maior_media = media
            aluno_maior = nome

        if media < menor_media:
            menor_media = media
            aluno_menor = nome

    print("\n--- RESULTADO FINAL ---")
    print(f"Maior média: {maior_media:.2f} - {aluno_maior}")
    print(f"Menor média: {menor_media:.2f} - {aluno_menor}")

    ordem_ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
    print("\n--- RANKING DOS ALUNOS ---")
    for posicao, aluno in enumerate(ordem_ranking, start=1):
        print(f"{posicao}° lugar: {aluno[0]} - Média: {aluno[1]:.2f}")


alunos = []

quantidade_alunos = int(input("Quantos alunos você quer cadastrar? "))

for i in range(quantidade_alunos):
    nome = input(f"Informe o nome do {i+1 }° aluno(a): ")
    notas = []
    quantidade_de_notas = int(input(f"Quantas notas o aluno {nome} possui? "))

    for j in range(quantidade_de_notas):
        nota = float(input(f"Digite a {j+1} nota do aluno (a) {nome}: "))
        notas.append(nota)
    alunos.append([nome, notas])

analisar_alunos(alunos)





