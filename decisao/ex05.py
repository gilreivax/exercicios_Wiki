notaUm = float(input("Nota 1: "))
notaDois = float(input("Nota 2: "))
media = (notaUm + notaDois) / 2
if media >= 7.00:
    print("Aprovado!")
elif media < 7.00:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção!")