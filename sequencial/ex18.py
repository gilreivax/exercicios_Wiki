# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = float(input("Informe tamanho do arquivo (MB):"))
velocidade = float(input("Informe a velocidade do dowloand: "))
print (f"O tempo aprocimado do download é de {(tamanho / velocidade) * 60} minutos.")
