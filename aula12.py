nome = str(input("Qual é o seu nome? "))

print(f"Tenha um bom dia {nome}")
if nome == "Victor":
    print("Nome bonito!")
elif nome == "Gustavo" or nome == "Sophia" or nome == "João":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana Cláudia Jessica Juliana":
    print("Belo nome feminino")
print(f"Tenha um bom dia, {nome}!")