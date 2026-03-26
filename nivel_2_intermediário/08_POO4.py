#exemplo de polimorfismo

class Animal:
    def falar(self):
        print("O animal emite algum som")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late: Au Au!")

class Gato(Animal):
    def falar(self):
        print("O gato mia: Miau!")

animais = [Cachorro(), Gato(), Animal()]

for i in animais:
    i.falar()