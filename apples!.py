quantas = int(input("Quantas maçãs você quer?"))

apple = 1.30

dozen = 1.00

if quantas < 12:
    print(f"Custará R${apple * quantas:.2f}")
elif quantas >= 12:
    print(f"Custará R${dozen * quantas:.2f}")
else:
    print("Peça maçãs!")