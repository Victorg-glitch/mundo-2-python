<<<<<<< HEAD
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
=======
sistema = 1

print('=-='*4)
print('Calculadora')
print('=-='*4)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while sistema == 1:
    print(('-=-'*3), ('MENU') ,('-=-'*3))
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    menu = int(input('Qual opção voce deseja usar? (use somente os numeros.): '))

    if menu == 1: #Soma dos produtos
        soma = n1 + n2
        print(f'A soma deu {soma}')
        

    if menu == 2: #Multiplicação dos produtos
        mult = n1 * n2
        print(f'A Multiplicação deu {mult}')
        
    if menu == 3: 
        if n1 > n2:
            print(f'{n1} é o maior')
    if menu == 5:
        sistema = 0
>>>>>>> 523ff6ddd18b79c540f5f781a7db0379be1c8992
