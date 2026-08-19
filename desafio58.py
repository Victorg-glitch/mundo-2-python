import random
from time import sleep
print('A maquina vai pensar em número de 1 a 5 e você terá que acerta ele.')

n_maquina = random.randrange(5)
n_jogador = input('Digite qual número você acha que a maquina escolheu: ')

while n_jogador != str(n_maquina):
    n_jogador = input('Você errou. Tente novamente: ')
print(f'Você acertou! O número da maquina era {n_maquina}')