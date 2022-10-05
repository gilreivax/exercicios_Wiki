# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo
numeroUm = int(input("Informe o primeiro número: "))
numeroDois = int(input("Informe o segundo número: "))
numeroTres = int(input("Informe o terceiro número: "))
produto = (numeroUm * 2) + (numeroDois / 2)
triplo = (numeroUm * 3) + numeroTres
cubo = numeroTres ** 3 
print(f"o produto do dobro do primeiro com metade do segundo = {produto}\n a soma do triplo do primeiro com o terceiro = {triplo} \n  o terceiro elevado ao cubo = {cubo}")