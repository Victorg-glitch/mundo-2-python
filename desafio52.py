numero = int(input('Digite um número: '))
if numero == 2 or numero == 1:
    print(f'Esse numero {numero} é primo.')
elif numero % 2 == 0:
    print(f'Esse numero {numero} não é primo')
else:
    for c in range(1,(numero - 1)):
        if numero % c == 0:
            print(f'Número divisivel {c}')
            if c != numero and c > 1:
                print(f'Esse numero não é primo')
                break
            else:
                print("Esse número é primo")
            
