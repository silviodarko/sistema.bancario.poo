# Projeto de Sistema Bancário

Este projeto implementa um sistema bancário simples em Python, utilizando classes para representar clientes e contas bancárias.

## Funcionalidades

- `Cliente`: Classe abstrata que representa um cliente genérico, com atributos comuns como nome e endereço.
- `Conta`: Classe abstrata que representa uma conta bancária genérica, com métodos abstratos para saque e depósito.
- `PessoaFisica`: Subclasse de `Cliente` que representa um cliente pessoa física, com atributos adicionais como CPF.
- `PessoaJuridica`: Subclasse de `Cliente` que representa um cliente pessoa jurídica, com atributos adicionais como CNPJ.
- `ContaCorrente`: Subclasse de `Conta` que representa uma conta corrente, com atributos adicionais como limite de crédito.
- `ContaPoupanca`: Subclasse de `Conta` que representa uma conta poupança.

## Como utilizar

1. Crie instâncias de clientes utilizando as subclasses `PessoaFisica` e `PessoaJuridica`, informando os dados necessários.
2. Crie instâncias de contas utilizando as subclasses `ContaCorrente` e `ContaPoupanca`, informando o número da conta, o cliente associado e os atributos adicionais.
3. Utilize os métodos `depositar` e `sacar` nas instâncias de contas para realizar operações de depósito e saque, respectivamente.
4. Acesse o atributo `saldo` das instâncias de contas para verificar o saldo atual.

Exemplo de uso:

```python
from projeto_sistema_bancario import PessoaFisica, PessoaJuridica, ContaCorrente, ContaPoupanca

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

Notas adicionais
Este projeto é apenas uma implementação simples para fins didáticos e pode ser adaptado e expandido conforme necessário.
Sempre teste o código antes de utilizá-lo em um ambiente de produção.
Caso tenha dúvidas ou precise de mais informações, consulte a documentação do Python ou entre em contato com a equipe responsável pelo projeto.
