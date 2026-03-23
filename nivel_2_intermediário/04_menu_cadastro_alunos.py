def media_notas(*notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    notas= []
    quantidade = int(input("Quantas notas? "))

    for i in range(quantidade):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    return [nome, notas]

def listar_alunos(alunos):
    for aluno in alunos:
        nome = aluno[0]
        notas = aluno[1]

        print(f"\nAluno: {nome}")
        print(f"Notas: {notas}")

def gerar_ranking(alunos):
    ranking = []

    for aluno in alunos:
        nome = aluno [0]
        notas = aluno [1]
        media = media_notas(*notas)

        ranking.append([nome,media])

    return sorted(ranking, key=lambda x: x[1], reverse = True)

def exibir_ranking(ranking):
    for posicao, aluno in enumerate(ranking, start = 1):
        print(f"{posicao}° lugar: {aluno[0]} - {aluno[1]:.2f}")

alunos = []

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Ver ranking")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        aluno = cadastrar_aluno()
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso! ")
    elif opcao == "2":
        listar_alunos(alunos)
    elif opcao == "3":
        ranking = gerar_ranking(alunos)
        exibir_ranking(ranking)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! ")

