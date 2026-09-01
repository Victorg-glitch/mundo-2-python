sexo = input('Digite o seu sexo [M/F]: ')
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite M ou F: ').upper()
    print(f'Certo então o seu sexo é {sexo}')
