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
    def __init__(self, numero, cliente, limite, numero_saques):
        self.numero = numero
        self.saldo = 0
        self.agencia = "0001"
        self.cliente = cliente
        self.limite = (limite,)
        self.numero_saques = (numero_saques,)
        self.extrato = Extrato()

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
    def extrato(self):
        return self.extrato

    def saque(self, valor):
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

    def deposito(self, valor):
        if valor > 0:
            saldo += valor
            print(f"O valor de R${valor:.2f} depositado com sucesso.")

        else:
            print("Deposito Invalido!")
            return False
        
        return True


def extrato(saldo, /, *, extrato):
    """
    A função extrato deve receber ambos tipos de argumenos: Posição e Nominal
    Args:
        Posicionais: Saldo
        Nominais: Extrato
    Return: String
    """

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
