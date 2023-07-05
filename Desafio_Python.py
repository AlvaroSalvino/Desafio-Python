deposito = {
}
saque = {
}
extrato = {
}


while True:
    opcao = input(f'''========== Banco DIO ==========
        
        1 - Depositar

        2 - Sacar

        3 - Ver Extrato

        0 - Sair
                
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
        if saque > '500':
            print('Limite máximo para saque: R$ 500')
    if opcao == '3':
        print(f'''Seu extrato:''')
