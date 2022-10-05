# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salarioHora= float(input("Salário hora: "))
horasTrabalhadas = int(input("Horas trabalhadas: ")) 
salarioTotal = salarioHora * horasTrabalhadas
print(f"Seu sálario é: {salarioTotal:.2f} reais.")