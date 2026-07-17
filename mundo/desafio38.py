n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))

if n1 > n2:
    print(f"\033[32m{n1}\033[m é o maior valor.")
elif n2 > n1: 
    print(f"\033[32m{n2}\033[m é o maior valor.")
else:
    print(f"Não existe valor maior.")
    