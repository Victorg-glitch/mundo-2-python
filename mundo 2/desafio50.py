"""for c in range(6):
    numero = int((input("Digite um número: ")))
    if numero % 2 == 0:
        numero += c
    print(numero)""" #=====MINHA RESPOSTA=====

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Você informou {cont} números pares e a soma foi {soma}')