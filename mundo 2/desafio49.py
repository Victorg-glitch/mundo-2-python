"""numero = int(input("Digite um número: "))
tabuada = 0
print("-=" * 20)
print(f"\033[32mTABUADA do {numero}\033[m")
print("-=" * 20)
for c in range(0,11):
    tabuada = numero * c
    print(tabuada)""" # ======MINHA RESPOSTA======

num = int(input('Digite um numero para ver a sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')