preco_produto = float(input("Digite o preço das compras: "))
print("-=-" * 10)
print("FORMAS DE PAGAMENTO")
print("-=-" * 10)
print("1. Dinheiro ou Cheque \n2. À vistá no cartão \n3. Até 2x no cartão \n4. 3x ou mais no cartão")
condicao_pagamento = int(input("Digite o número da opção de pagamento que você desejar: "))

if condicao_pagamento == 1:
    valor = preco_produto - (preco_produto * 0.1)
    print(f"O produto vai custar \033[32mR${valor:.2f}\033[m.")
elif condicao_pagamento == 2:
    valor = preco_produto - (preco_produto * 0.05)
    print(f"O produto vai custar \033[32mR${valor:.2f}\033[m.")
elif condicao_pagamento == 3:
    print(f"O produto vai custar \033[32mR${preco_produto}\033[m.")
elif condicao_pagamento == 4:
    valor = preco_produto + (preco_produto * 0.2)
    tempo = int(input("Quantas parcelas? "))
    if tempo >= 3:
        print(f"Ficou em {tempo} parcelas de {valor / tempo}")
        print(f"O produto vai custar \033[32mR${valor:.2f}\033[m")
    else:
        print(f"Ficou em {tempo} parcelas de {preco_produto}")
        print(f"O produto vai custar \033[32mR${preco_produto}\033[m")
else: 
    print("\033[31mDigite um valor válido.\033[m")