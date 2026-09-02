from random import randint
jogador = vitorias = computador = resultado = 0
escolha = ''
print('-=-' * 10)
print('Jogo do par ou impar')
print('-=-' * 10)
while True:
    computador = randint(0,10)
    escolha = str(input('Par ou Impar? ')).upper().strip()[0]
    jogador = int(input('Digite um número: '))
    resultado = jogador + computador
    if escolha == 'P':
        if resultado % 2 ==0:
            print('Parabéns! Você ganhou!!')
            print('Vamos jogar novamente...')
        else:
            print('Não foi dessa vez...')
            break
    if escolha == 'I':
        if resultado % 2 != 0:
            print('Parabéns! Você ganhou!!')
            print('Vamos jogar novamente...')
        else:
            print('Não foi dessa vez...')
            break
    vitorias += 1
if vitorias > 1:
    print(f'Parabéns!!! Você ganhou {vitorias} consecutivas')
else:
    print(f'Não foi dessa vez. Tente novamente.')