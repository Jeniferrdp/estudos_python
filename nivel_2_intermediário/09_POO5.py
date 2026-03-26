#abstração

class Impressora:
    def imprimir(self, texto):
        print(f"Imprimindo: {texto}")

imp = Impressora()
imp.imprimir("Olá Mundo!")