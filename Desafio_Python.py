menu = """

1 DEPOSITAR

2 SACAR

3 EXTRATO

0 SAIR

"""

saldo = 0
limite = 500
extrato = ""
numeroSaque = 0
LIMIE_SAQUES = 3

while True:
    opcao  = input(menu)

    if opcao == "1":
        valor = float(input("Quanto deseja Depositar?: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Opção inválida, informe valor positivo")
    
    elif opcao == "2":
        valor = float(input("Quanto deseja sacar?: "))

        excedeuSaldo = valor > saldo

        excedeuLimite = valor > limite

        excedeuSaques = numeroSaque >= LIMIE_SAQUES

        if excedeuSaldo:
            print("Você não tem saldo suficiente!")

        elif excedeuLimite:
            print("Você não tem saldo suficiente para este saque!")

        elif excedeuSaques:
            print("Você não tem saldo de saques suficiente! LIMITE = 3/dia")

        else:
            print("VALOR INVALIDO!")

    
    elif opcao == "3":
        print("##ESTRATO##")
        print("Não há movimentação." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida, favor selecionar opção válida.")