from random import randint

matrizA = []
matrizB = []

for linha in range(10):
    linha = []

    for coluna in range(10):
        linha.append(randint(0, 10000))

    matrizA.append(linha)

for linha_matriz in matrizA:
    print(linha_matriz)
    for i in linha_matriz:
        outro = i*3
        print(outro)

        matrizB.append(outro)

    print(matrizB)
