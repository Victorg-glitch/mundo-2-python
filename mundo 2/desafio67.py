n = mult = 0
cont = 10
print('-=-' * 10)
print('TABUADA DE NÚMEROS')
print('-=-' * 10)
n = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 30)
while True:
    print(f'{n} x ' , end ='')
    print(f'{cont} = {n * cont}')
    cont -= 1
    if cont == 0:
        print('-' * 30)
        n = int(input('Quer ver a tabuada de qual valor? '))
        cont = 10
        print('-' * 30)
    if n < 0:
        print('O número digitado é negativo.')
        break
print('FIM.')