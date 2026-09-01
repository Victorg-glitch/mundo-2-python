soma = cont = n = 0
while True:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        break
    cont += 1
    soma += n 
print(f'Você digitou {cont} números, a soma ficou {soma}.')