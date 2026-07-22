from datetime import date
ano = 0
idade = 0
menores18 = []
maiores18 = []
tem18 = []
falta18 = []
anos18 = []
anosp18 = []
passou18 = []
for c in range(7):
    ano = int(input('Digite o seu ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 18:
        falta18 = 18 - idade
        anos18.append(falta18)
        menores18.append(ano)
    elif idade > 18:
        passou18 = idade - 18
        anosp18.append(passou18)
        maiores18.append(ano)
    else:
        tem18.append(idade)
print(f'Os que são menores de 18 nasceram em {menores18}. Para voces faltam {anos18}.')
print(f'Os que são maiores de 18 nasceram em {maiores18}. Vocês ja passaram {anosp18} anos.')
print(f'Todos que nasceram em 2008 tem 18 anos')
