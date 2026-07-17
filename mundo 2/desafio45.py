from random import randint
from time import sleep

"""escolha_usuario = input("Escolha entre pedra, papel e tesoura: ").lower()
escolhas = ["pedra", "papel", "tesoura"]
escolha_maquina = random.choice(escolhas)

print(escolha_maquina)
if escolha_maquina == "papel" and escolha_usuario == "pedra":
    print("A maquina venceu")
elif escolha_maquina == "papel" and escolha_usuario == "tesoura":
    print("Você venceu")
elif escolha_maquina == "papel" and escolha_usuario == "papel":
    print("Deu empate")

if escolha_maquina == "pedra" and escolha_usuario == "tesoura":
    print("A maquina venceu")
elif escolha_maquina == "pedra" and escolha_usuario == "papel":
    print("Você venceu")
elif escolha_maquina == "pedra" and escolha_usuario == "pedra":
    print("Deu empate")

if escolha_maquina == "tesoura" and escolha_usuario == "papel":
    print("A maquina venceu")
elif escolha_maquina == "tesoura" and escolha_usuario == "pedra":
    print("Você venceu")
elif escolha_maquina == "tesoura" and escolha_usuario == "tesoura":
    print("Deu empate")"""

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input("Qual é a sua jogada: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÓ")
sleep(1)
print("-=" * 15)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-=" * 15)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCEU!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA!")