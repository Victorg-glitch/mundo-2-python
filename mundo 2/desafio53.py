
frase = input('Digite uma frase:  ').strip().lower()
palavra = frase.split()
palindromo = ''.join(palavra)
ultletra = len(palindromo) - 3
print(len(palindromo))
if palindromo[0:2] == palindromo[ultletra:]:
    print('Essa palavra é um palindromo')
else:
    print('Essa palavra não é um palindromo')
print(frase)
