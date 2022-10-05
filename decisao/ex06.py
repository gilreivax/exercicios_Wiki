numUm = int(input("Informe o primeiro núemro: "))
numDois = int(input("Informe o segundo núemro: "))
numTres = int(input("Informe o terceiro núemro: "))
if numUm> numDois and numUm > numTres:
    print(f"Maior :{numUm}")
elif numDois > numUm and numDois > numTres:
    print(f"Maior {numDois}")
else:
    print(f"Maior: {numTres}")