import math

x1 = float(input("Digite o valor de x1"))
y1 = float(input("Digite o valor de y1"))
x2 = float(input("Digite o valor de x2"))
y2 = float(input("Digite o valor de y2"))

D = math.sqrt((x1-y1)**2 + (x2 - y2)**2)

print(f"A distância dos pontos {x1},{y1},{x2} e {y2} é de {D}")