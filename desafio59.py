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
