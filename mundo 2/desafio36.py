print("\033[34m-=-" * 20)
print("Calculadora de emprestimo")
print("-=-" * 20, "\033[m")

casa_valor = float(input("Digite o valor da casa: "))
salario = float(input("Qual o seu salario: "))
anos_pagar = int(input("Em quantos anos pretende pagar: "))

valor_mensal = casa_valor / (anos_pagar * 12)

if valor_mensal > (0.30 * salario):
    print("\033[31mSeu emprestimo foi recusado\033[m")
else:
    print(f"\033[32mSeu emprestimo foi aprovado e suas parcelas vão ficar no valor de R${valor_mensal:.2f}\033[m")