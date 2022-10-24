# Questão 1
"""times = []

while True:
    clubes = input("Digite o nome de um Clube de futebol: ")

    if len(clubes) > 0:
        times.append(clubes)
        print(times)

    if len(times) > 10:
        print("Você já adicionou 10 clubes!")
        break

    for clubes in times:
        selecao = input("Quer que eu ache algum time?[S/N]: ")
        if selecao == "S":
            part2 = input("Qual time?:")
            indice = times.index(part2)
            print("Achei!")
        elif selecao == "N":
            break """

# Questão 2
from random import randint

numeros = []

for i in range(1, 31):
    numeros.append(randint(0, 30))

print(numeros)
num = int(input("Digite um número da lista: "))

if num in numeros:
    print(f"O número {num} aparece {numeros.count(num)} vezes na lista")
else:
    print(f"O numero {num} não aparece na lista")


