from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetimes


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, nro_conta, transacao):
        transacao.registrar(nro_conta)

    def adicionar_conta(self, nro_conta):
        self.contas.append(nro_conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.saldo = 0
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def criar_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self.saldo

    @property
    def agencia(self):
        return self.agencia

    @property
    def cliente(self):
        return self.cliente

    @property
    def historico(self):
        return self.historico

    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo:
            print("Voce não possui este valor em conta.")
        elif valor >= 0:
            self.saldo -= valor
            print("Saque Realizado")
            return True
        else:
            print("Operacao falhou")

        return False

    def depositar(self, valor):
        if valor > 0:
            saldo += valor
            print(f"O valor de R${valor:.2f} depositado com sucesso.")

        else:
            print("Deposito Invalido!")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )
        if valor > self.limite:
            print("o Valor do saque é maior que seu limite...")
        elif numero_saques >= self.limite_saques:
            print("Conta ja alcançou limites de saques.")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @classmethod    
    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
