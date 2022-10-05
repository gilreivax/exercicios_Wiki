# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
metros = int(input("Tamanho em metros a ser pintado: "))
litros = metros * 6
latasNecessarias = metros / 18
if latasNecessarias < 1:
    latasNecessarias = 1
print(f"Você vai pintar {metros} metros e precisa de {latasNecessarias:.2f} lats  que custa {latasNecessarias * 80 :.2f} reais.")