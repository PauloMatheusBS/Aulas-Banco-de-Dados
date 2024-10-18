def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2


num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
operacao = input("Digite a operação desejada (soma ou subtracao): ")

if operacao == "soma":
    resultado = soma(num1, num2)
elif operacao == "subtracao":
    resultado = subtracao(num1, num2)
else:
    print("Operação inválida.")    

print("O resultado da", operacao, "é:", resultado)