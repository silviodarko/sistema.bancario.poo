from abc import ABC, abstractmethod


class Cliente(ABC):
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


class Conta(ABC):
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass


class PessoaFisica(Cliente):
    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self.cpf = cpf


class PessoaJuridica(Cliente):
    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self.cnpj = cnpj


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite):
        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente")
            return False

    def depositar(self, valor):
        self.saldo += valor
        return True


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente")
            return False

    def depositar(self, valor):
        self.saldo += valor
        return True


def main():
    cliente1 = PessoaFisica("João", "Rua A, 123", "123.456.789-00")
    cliente2 = PessoaJuridica("Empresa X", "Rua B, 456", "12.345.678/0001-00")

    conta1 = ContaCorrente("001", cliente1, 1000)
    conta2 = ContaPoupanca("002", cliente2)

    conta1.depositar(500)
    conta1.sacar(200)

    conta2.depositar(1000)
    conta2.sacar(500)

    print(f"Saldo conta1: {conta1.saldo}")
    print(f"Saldo conta2: {conta2.saldo}")


if __name__ == "__main__":
    main()

