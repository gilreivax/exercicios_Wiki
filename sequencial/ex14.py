# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
quilos = float(input("Informe quantos kg você pesou: "))
if quilos > 50.00:
    quilos -= 50
    multa = quilos * 4
    print(f"Excedeu {quilos} kg a multa é de: {multa} reais.")
else:
    print(f"Limite não atingido, você não pagara multa.")