n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
print(n)
for c in range(10):
    pa = n + r
    n += r
    print(pa)