dias = int(input("Quantos dias alugados?"))
km = float(input("Quantos quilômetros rodados?"))
valor= (dias*60)+(km*0.15)
print(f"O custo do aluguel do carro foi de R${valor:.2f}")