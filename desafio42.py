lado1 = float(input("Medida do primero lado: "))
lado2 = float(input("Medida do segundo lado: "))
lado3 = float(input("Medida do terceiro lado: "))

triangulo = lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1

if triangulo == True:
    if lado1 == lado2 and lado3:
        print("\033[34mÉ um triângulo equilátero.\033[m")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("\033[33mÉ um triângulo isósceles\033[m")
    else:
        print("\033[35mÉ um triangulo escaleno\033[m")
else:
    print("\033[31mNão da para fazer um triângulo\033[m")