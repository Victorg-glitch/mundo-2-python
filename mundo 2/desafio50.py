for c in range(6):
    numero = int((input("Digite um número: ")))
    if numero % 2 == 0:
        numero += c
    print(numero)