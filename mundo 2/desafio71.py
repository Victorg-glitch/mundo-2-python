valor_saque = valor_notas = nota50 = nota20 = nota10 = nota1 = 0
escolha = ''
print('=' * 30)
print(' ' * 5 ,'CAIXA ELETRÔNICO')
print('=' * 30)
while True:
    valor_saque = int(input('Qual valor você deseja sacar? '))
    valor_notas = valor_saque
    nota50 = valor_notas // 50
    if nota50 > 0:
        valor_notas -= nota50 * 50
        print(f'Será um total de {nota50} de R$50')
    nota20 = valor_notas // 20
    if nota20 > 0:
        valor_notas -= nota20 * 20
        print(f'Será um total de {nota20} de R$20')
    nota10 = valor_notas // 10
    if nota10 > 0:
        valor_notas -= nota10 * 10
        print(f'Será um total de {nota10} de R$10')
    nota1 = valor_notas
    if nota1 > 1:
        valor_notas -= nota1 * 1
        print(f'Será um total de {nota1} de R$1')
    totalNota = nota1 + nota10 + nota20 + nota50
    print(f'Vai ficar em um total de {totalNota} celulas.')    
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break