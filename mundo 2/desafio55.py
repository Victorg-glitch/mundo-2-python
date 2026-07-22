peso = 0
maior = []
for c in range(5):
    peso = float(input('Digite o seu peso: '))
    maior.append(peso)

if maior[0] > maior[1] and maior[0] > maior[2] and maior[0] > maior[3] and maior[0] > maior[4]:
    print(f'O maior peso é {maior[0]}')
elif maior[1] > maior[0] and maior[1] > maior[2] and maior[1] > maior[3] and maior[1] > maior[4]:
    print(f'O maior peso é {maior[1]}')
elif maior[2] > maior[0] and maior[2] > maior[1] and maior[2] > maior[3] and maior[2] > maior[4]:
    print(f'O maior peso é o {maior[2]}')
elif maior[3] > maior[0] and maior[3] > maior[1] and maior[3] > maior[2] and maior[3] > maior[4]:
    print(f'O peso maior é {maior[3]}')
else:
    print(f'O peso maior é {maior[4]}')
print(maior)
