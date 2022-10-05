# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
fahrenheit = int(input("Temperatura em fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f"Fahrenheit: {fahrenheit} graus, Celsius: {celsius:.3f} graus.")