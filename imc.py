massa = float(input("Diga seu peso em quilogramas:"))
altura = float(input("Diga a sua altura em metros:"))
imc = (massa/(altura**2))
if imc <18.5:
  print(f"Seu IMC é de {imc:.2f}")
  print("Abaixo do peso, procure um espicialista!")
elif 18.5 < imc < 24.99:
 print(f"Seu IMC é de {imc:.2f}")
 print("Peso normal")
elif 25 < imc < 30.00:
 print(f"Seu IMC é de {imc:.2f}")
 print("Sobrepeso, procure um especialista!")
else:
 print(f"Seu IMC é de {imc:.2f}")
 print("Próxima parada: Cárdiaca")