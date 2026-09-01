<<<<<<< HEAD
from random import randint
computador = randint(0, 10)
print('Sou seu computado... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
=======
import random
from time import sleep
print('A maquina vai pensar em número de 1 a 5 e você terá que acerta ele.')

n_maquina = random.randrange(5)
n_jogador = input('Digite qual número você acha que a maquina escolheu: ')

while n_jogador != str(n_maquina):
    n_jogador = input('Você errou. Tente novamente: ')
print(f'Você acertou! O número da maquina era {n_maquina}')
>>>>>>> 523ff6ddd18b79c540f5f781a7db0379be1c8992
