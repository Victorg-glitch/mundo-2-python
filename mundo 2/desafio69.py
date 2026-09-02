idade = cont = mais18 = h = m = menos20 = 0
parar = sexo = ''

print('-=-' * 10)
print('Analise de adultos')
print('-=-' * 10)

while True:
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite um sexo: [H/M] ')).upper().strip()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'H':
        h += 1
    if sexo == 'M' and idade < 20:
        menos20 += 1
    cont += 1
    parar = str(input('Deseja parar? [S/N] ')).upper().strip()[0]
    if parar == 'S':
        break
if h and mais18 and menos20 > 1:
    print(f'Você cadastrou {cont} pessoas, e nelas tinham {mais18} maiores de 18, {h} homens , {menos20} mulheres menores de 20 anos.')
else:
    print(f'Você cadastrou {cont} pessoa, e nelas tinham {mais18} maior de 18, {h} homen , {menos20} mulher menor de 20 anos.')