n = mult = 0
cont = 10
print('-=-' * 10)
print('TABUADA DE NÚMEROS')
print('-=-' * 10)
n = int(input('Digite o número de qual tabuada você quer saber: '))
while True:
    print('-' * 30)
    print(f'{n} x ' , end ='')
    print(f'{cont} = {n * cont}')
    cont -= 1
    if cont == 0:
        print('-' * 30)
        n = int(input('Digite qual o novo número você deseja saber: '))
        cont = 10
    if n < 0:
        print('O número digitado é negativo.')
        break
print('FIM.')