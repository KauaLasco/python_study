'''Calculadora com while'''

while True:
    try:
        opcao = input('Você deseja, [1] somar, [2] subtrair, [3] multiplicar, [4] dividir ou [0] sair? Selecione uma das opções: ')
        opcao = int(opcao)

        if opcao == 1:
            soma_1 = input('Selecione o primeiro número: ')
            soma_1 = int(soma_1)
            soma_2 = input('Selecione o segundo número: ')
            soma_2 = int(soma_2)

            print(f'A soma entre os valores {soma_1} e {soma_2} é igual à:', soma_1 + soma_2)
    
        elif opcao == 2:
            sub_1 = input('Selecione o primeiro número: ')
            sub_1 = int(sub_1)
            sub_2 = input('Selecione o segundo número: ')
            sub_2 = int(sub_2)

            print(f'A subtração entre os valores {sub_1} e {sub_2} é igual à:', sub_1 - sub_2)

        elif opcao == 3:
            mult_1 = input('Selecione o primeiro número: ')
            mult_1 = int(mult_1)
            mult_2 = input('Selecione o segundo número: ')
            mult_2 = int(mult_2)

            print(f'A subtração entre os valores {mult_1} e {mult_2} é igual à:', mult_1 * mult_2)
    
        elif opcao == 4:
            div_1 = input('Selecione o primeiro número: ')
            div_1 = int(div_1)
            div_2 = input('Selecione o segundo número: ')
            div_2 = int(div_2)

            print(f'A subtração entre os valores {div_1} e {div_2} é igual à:', div_1 / div_2)

        elif opcao == 0:
            print("Fechando calculadora...")
            break

        else:
            print('Insira uma opcão válida')
    except:
        print('Insira somente números.')