menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        vlr = float(input("Informe o valor a ser depositado:"))
        if vlr > 0:
            saldo += vlr
            print(f"O valor de R${vlr:.2f} depositado com sucesso.")
            extrato += f"Depósito: R$ {vlr:.2f}"
        else:
            print("Deposito Invalido!")
    elif opcao == "s":
        vlr = float(input("Informe o valor a ser sacado:"))
        if vlr > saldo:
            print("Voce não possui este valor em conta.")
        elif vlr > limite:
            print("Voce não possui este limite de saque.")
        elif numero_saques > 3:
            print("Você alcançou o numero maximo de saques.")
        elif vlr >= 0:
            saldo -= vlr
            print(f"Saque: R$ {vlr:.2f}")
            extrato += f"Saque: R$ {vlr:.2f}"
            numero_saques += 1
    elif opcao == "e":
       print("\n================ EXTRATO ================")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
