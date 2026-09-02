nome_produto = escolha = baraton = ''
preço = preço_baixo = cont = total = produto_caro = 0
print('-=-' * 10)
print('Calculadora de supermercado')
print('-=-' * 10)
preço_baixo = preço
while True:
    nome_produto = str(input('Digite o nome do produto escolhido: '))
    preço = float(input('Digite o preço do produto escolhido: '))
    cont += 1
    preço_novo = preço
    total += preço
    escolha = str(input('Deseja colocar outro produto? [S/N] ')).upper().strip()[0]
    if preço > 1000:
        produto_caro += 1
    if preço < preço_baixo:
            baraton = nome_produto
            preço_baixo = preço
    if escolha == 'N':
        break
print(f'Temos {produto_caro} acima de R$1000.')
print(f'Você escolheu {cont} produtos, e vai custa R${total}, o produto mais barato foi {baraton} e custou R${preço_baixo}')