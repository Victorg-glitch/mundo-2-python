from datetime import date

genero = int(input("""1. Masculino
2. Feminino             
Qual o seu genero: """))
data_nascimento = int(input("Digite a sua data de nascimento: "))

idade = date.today().year - data_nascimento

print("\033[34m-=-" * 10)
print("-=-" * 10, "\033[m")

if genero == 1:
    if idade < 18:
        print(f"Você ainda não está na hora de alistar, falta {idade -  18} anos, para se alistar.")
        print(f"Seu alistamento vai ser em {(idade - 18) + date.today().year}")
    elif idade == 18:
        print(f"Já está na hora de alistar. \033[32mVocê ja tem {idade}\033[m")
    else:
        print(f"\033[31mJá passou da hora de alistar. Você ja tinha que ter se apresentado a {idade - 18} anos\033[m")
        print(f"Seu alistamento foi em {(idade - 18) - date.today().year }")
elif genero == 2:
    print("Você não precisa participar do alistamento obrigatório.")
else:
    print("Digite 1 ou 2 para escolher o genêro")