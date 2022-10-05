# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input("Informe sua altura em metros e centimentros: "))
pesoHomem = (72.7 * altura) - 58
pesoMulher = (62.1 * altura) - 44.7
print(f"O peso ideal para o homem é {pesoHomem}")
print(f"O peso ideal para a mulher é {pesoMulher}")