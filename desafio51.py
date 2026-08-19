"""n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
print(n)
for c in range(10):
    pa = n + r
    n += r
    print(pa)""" # MINHA RESPOSTA

#RESPOSTA DO PROFESSOR
primeiro = int(input('Pimeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range (primeiro ,decimo , razão ):
    print(f'{c}')