class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome, idade):
        super(). __init__(nome, idade)
        self.__notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida")

    def __calcular_media(self):
        if self.__notas:
            return sum(self.__notas ) / len(self.__notas)
        return 0

    def mostrar_situacao(self):
        media = self.__calcular_media()
        if media >= 7:
            print(f"Aluno: {self.nome}\nMédia: {media:.2f}\nSituação: Aprovado")
        elif media >= 5:
            print(f"Aluno: {self.nome}\nMédia: {media:.2f}\nSituação: Recuperação")
        else:
            print(f"Aluno: {self.nome}\nMédia: {media:.2f}\nSituação: Reprovado")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super(). __init__(nome, idade)
        self.disciplina = disciplina

    def ensinar(self):
        print(f"O professor(a) {self.nome} está ensinando a disciplina de: {self.disciplina}")

aluno1 = Aluno("Jenifer", 27)
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7.5)

aluno2 = Aluno("Lina", 22)
aluno2.adicionar_nota(6)
aluno2.adicionar_nota(4.5)

professor1 = Professor("Helena", 40, "Matemática")


pessoas = [aluno1, aluno2, professor1]

for i in pessoas:
    i.apresentar()

    if isinstance(i, Aluno):
        i.mostrar_situacao()

    if isinstance(i, Professor):
        i.ensinar()