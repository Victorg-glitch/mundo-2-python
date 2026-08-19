'''nome = []
idade = []
sexo = []
menor21 = []

for c in range(4): #passando informações de cada pessoa
    nome.append(input('Digite o seu nome: '))
    idade.append(int(input('Digite sua idade: ')))
    sexo.append(input('M ou H: ').upper())

#Criando o perfil de cada usuario
pessoa1 = [nome[0], idade[0], sexo[0]]
pessoa2 = [nome[1], idade[1], sexo[1]]
pessoa3 = [nome[2], idade[2], sexo[2]]
pessoa4 = [nome[3], idade[3], sexo[3]]

#Vendo qual mulher tem menos de 21
if idade[0] < 21 and sexo[0] == 'M':
    menor21.append(idade[0])
if idade[1] < 21 and sexo[1] == 'M':
    menor21.append(idade[1])
if idade[2] < 21 and sexo[2] == 'M':
    menor21.append(idade[2])
if idade[3] < 21 and sexo[3] == 'M':
    menor21.append(idade[3])

# Pegando a media das idades
media = (idade[0] + idade[1] + idade[2] + idade[3]) / 4 

#Descobrindo quem tem a maior idade
if idade[0] > idade[1] and idade[0] > idade[2] and idade[0] > idade[3]: #pessoa1
    maior_idade = nome[0]
elif idade[1] > idade[0] and idade[1] > idade[2] and idade[1] > idade[3]: #pessoa2
    maior_idade = nome[1]
elif idade[2] > idade[0] and idade[2] > idade[1] and idade[2] > idade[3]: #pessoa3
    maior_idade = nome[2]
elif idade[3] > idade[0] and idade[3] > idade[1] and idade[3] > idade[2]: #pessoa4
    maior_idade = nome[3]

print(f'A pessoa que tem a maior idade é {maior_idade}
{len(menor21)} tem menos de 21 anos.
e  a media de idade das pessoas é de {media} anos')'''#Minha resposta

#Resposta do professor
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} menores de 20 anos')