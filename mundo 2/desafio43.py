altura = float(input("Altura: "))
peso = float(input("Peso: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("\033[33mVocê está abaixo do peso.\033[m")
elif imc < 25:
    print("\033[32mVocê está no peso ideal.\033[m")
elif imc < 30:
    print("\033[33mVocê está no sobrepeso.\033[m")
elif imc < 40:
    print("\033[31mVocê está na obesidade.\033[m")
else:
    print("\033[2;31mVocê está na obesidade morbida.\033[m")
    