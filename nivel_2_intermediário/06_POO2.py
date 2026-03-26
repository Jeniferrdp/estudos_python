class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo  #atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido")

    def ver_saldo(self):
        return self.__saldo

conta1 = Conta(1000)
conta1.depositar(500)
print(conta1.ver_saldo())  # 1500

conta1.sacar(200)
print(conta1.ver_saldo())  # 1300

# conta1.__saldo = 99999  # Não funciona! (protegido)