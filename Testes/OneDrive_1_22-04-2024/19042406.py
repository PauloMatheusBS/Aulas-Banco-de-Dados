precos = {
    "Azul": 20,
    "Laranja": 30,
    "Roxo": 40,
    "Marrom": 50
}

# Solicita a cor do CD ao usuário
cor = input("Digite a cor do CD (Azul, Laranja, Roxo ou Marrom): ")

# Verifica se a cor está no dicionário e exibe o preço correspondente
if cor in precos:
    preco = precos[cor]
    print("O preço do CD na cor", cor, "é", preco, "Reais.")
else:
    print("Cor inválida.")