class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, me chamo {self.nome} e tenho {self.idade} anos")

#Aluno herda a classe Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)  # chama o __init__ da classe Pai
        self.matricula = matricula

    def estudar(self):
        print(f"O aluno (a) {self.nome}\nMatrícula: {self.matricula}\nEstá estudando")

aluno1 = Aluno("Jenifer", 22, "123456")
aluno1.apresentar()  #classe Pai
aluno1.estudar()     #classe filha