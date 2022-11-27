import requests
import json

x = 0
API_KEY = input("Digite a key a ser utilizada:")
arquivo_desejado = input("Digite o nome do arquivo a ser lido:")

dados = []
with open(arquivo_desejado, "r", encoding="utf-8") as arquivo:
    for linha in arquivo.readlines():
        novo_formato = linha.split(",")
        dados.append(novo_formato)

info = dados[x]
for info in dados:
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={info[3]}&lon={info[2]}&appid={API_KEY}'
    resposta = requests.get(url)

    print(f'Gerando: {info[0]}.json')
    with open(info[0] + '.json', 'w', encoding='UTF-8') as arquivo:
        dados_json = json.dumps({info[1]: resposta.json()}, indent=4)
        arquivo.write(dados_json)
        x += 1
