class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

aluno1 = Aluno("Jenifer", [8, 7, 9])

print(aluno1.calcular_media())
print(aluno1.situacao())