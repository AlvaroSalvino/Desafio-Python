
while True:
    opcao = input(f'''========== Banco DIO ==========
        
        1 - Depositar

        2 - Sacar

        3 - Ver Extrato
                
        INSIRA UMA OPÇÃO: ''')

    if opcao == '1':
        while True:
            deposito = int(input('Quanto quer depositar?: '))
            if deposito <= 0:
                print('Não é possível depositar valores negativos, por favor insira um valor válido!')
            else:
                break
    if opcao == '2':
        saque = int(input('Quanto deseja sacar?: '))
