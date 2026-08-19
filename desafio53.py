'''
frase = input('Digite uma frase:  ').strip().lower()
#tratamento dos dados
palavra = frase.split() #transformando em tabela
frase_noespaco = ''.join(palavra) #tirando os espaços
palindromo = frase_noespaco[:3] #pegando as primeiras 3 letras da frase
frase_invertida = frase_noespaco[::-1] #invertendo as frases
palindromo_invertido = frase_invertida[:3] #pegando as ultimas 3 letras invertidas.

print(palindromo)

#condição para saber se é um palindromo
if palindromo == palindromo_invertido:
    print('Essa palavra é um palindromo')
else:
    print('Essa palavra não é um palindromo')
print(frase)
'''#Minha resposta

#Reposta do professor
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase não é um palindromo')