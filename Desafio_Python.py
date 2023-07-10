import textwrap

def menu():
    menu = """\n

    1\tDEPOSITAR

    2\tSACAR

    3\tEXTRATO

    4\tLISTAR CONTA

    5\tNOVO USUARIO

    0\tSAIR

    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Despósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("@@@&&& Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeroSaque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeroSaque > limite_saques

    if excedeu_saldo:
        print("\n@@@ Opeação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Opeação falhou! O valor de saque excede o limitie. @@@")

    elif excedeu_saques:
        print("\n@@@ Opeação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com Sucesso! ===")

    else:
        print("\n@@@ Opeação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("##ESTRATO##")
    print("Não há movimentação." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("################################################")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nasicmento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("===Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numeroSaque = 0
    usuarios = []
    contas = []
    
    while True:
        opcao  = menu()

        if opcao == "1":
            valor = float(input("Quanto deseja Depositar?: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Quanto deseja sacar?: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeroSaque=numeroSaque,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "0":
            break

        else:
            print("Opção inválida, favor selecionar opção válida.")

main()