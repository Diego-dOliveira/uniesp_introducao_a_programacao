import requests
import json

API_KEY = "d27b7e096a39d56fb7fee8f23f9730f7"
cidade = []

URL = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

resposta = requests.request("GET", URL)
objetos = json.loads(resposta.text)

# for i in objetos:
#    print(f"{i}:{objetos[i]}\n")

file = "FINAL.txt"
Pais = objetos["sys"]["country"]
Nome = objetos["name"]
Longitude = objetos["coord"]["lon"]
# Longitude = float(input("Digite uma longitude:"))
Latitude = objetos["coord"]["lat"]
# Latitude = float(input("Digite uma lotitude:"))
print(f"A Latitude de {cidade} é {Latitude}")
print(f"A Longitude de {cidade} é {Longitude}")
print(f"Está cidade é {Nome}, e o seu país é {Pais}")

url = f'https://api.openweathermap.org/data/2.5/weather?lat={Latitude}&lon={Longitude}&appid={API_KEY}'
answers = requests.get(url)

with open(file + '.json', 'w', encoding='UTF-8') as arquivo:
    dados = json.dumps({Pais: answers.json()}, indent=4)
    arquivo.write(dados)

while True:
    op = input("1 - Cadastrar cidades\n"
               "2 - Cidades cadastradas\n"
               "3 - Sair")

    try:
        op == True
    except (ValueError, TypeError):
        print("Digite apenas o número das opções")

    if op == 1:
        qual = input("Qual a cidade desejada?:")
        cidade.append(qual)

    elif op == 2:
        for i in dados:
            print(i)

    elif op == 3:
        break

