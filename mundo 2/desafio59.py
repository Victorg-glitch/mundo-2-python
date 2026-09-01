from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5: 
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplicação}')
    elif opção == 3:
        maior = n1
        if n1 < n2:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opção == 4:
        print('informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Saindo do programa...')
        sleep(3)
        opção = 5
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')