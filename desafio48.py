soma = 0
for c in range(0, 501):
    if c % 3 == 0:
        soma += c
print(f'A soma de todos os valores impares multiplos de 3 é de {soma}')