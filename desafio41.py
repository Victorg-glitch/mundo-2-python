from datetime import date

ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = date.today().year - ano_nascimento

if idade <= 9:
    print("Você está na categoria MIRIM")
elif idade <= 14:
    print("Você está na categoria INFANTIL")
elif idade <= 19: 
    print("Você está na categoria JUNIOR")
elif idade <= 20:
    print("Você está na categoria SÊNIOR")
else: 
    print("Você está na categoria MASTER")