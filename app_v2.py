def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    A função deve receber apenas argumentos por nome,
    Args: saldo,valor,extrato,limite,numero_saques,limite_saques
    Return: saldo, extrato
    """
    if valor > saldo:
        print("Voce não possui este valor em conta.")
    elif valor > limite:
        print("Voce não possui este limite de saque.")
    elif numero_saques > limite_saques:
        print("Você alcançou o numero maximo de saques.")
    elif valor >= 0:
        saldo -= valor
        print(f"Saque: R$ {valor:.2f}")
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print("Saque Realizado")
    else:
        print("Operacao falhou")

    return saldo, extrato


def deposito(saldo, valor, extrato, /):
    """
    A função deve receber apenas argumentos posicional.
    Args: saldo,valor,extrato
    Return: saldo,extrato
    """
    if valor > 0:
        saldo += valor
        print(f"O valor de R${valor:.2f} depositado com sucesso.")
        extrato += f"Depósito: R$ {valor:.2f}"
    else:
        print("Deposito Invalido!")
    return saldo, extrato


def criar_usuario(usuarios):
    """
    Função deve Armazenar usuarios em uma lista.
    Args: nome, data_nasc, cpf, endereco
    """
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )
    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )
    print("Usuario Criado!")


def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuario Nao cadastrado")


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


def listar_contas(contas):
    # criar_conta("1000","01",usuario={'nome':'Sander','data_nasc':'10/06/1985','endereco':'rua dos caquis'})
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha, sep="\n")


def main():
    menu = """
[c] Criar Conta
[u] Criar Usuario
[l] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado:"))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor a ser sacado:"))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            extrato(saldo, extrato=extrato)
        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


main()
