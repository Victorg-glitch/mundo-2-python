nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("\033[32mAprovado\033[m")
elif media >= 5:
    print("\033[33mRecuperação\033[m")
else:
    print("\033[31mReprovado\033[m")