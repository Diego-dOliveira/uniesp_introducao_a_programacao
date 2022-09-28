cadastro=[]

botao=1000
while botao != 0:
    print("Digite 1 para cadastrar um novo usuário")
    print("Digite 2 para imprimir todos os usuários")
    print("Digite 0 para sair!")
    botao = int(input("Digite a opção desejada: "))

    if botao==1:
        nome = input("Digite o seu nome:")
        idade = int(input("Digite sua idade:"))
        email = input("Digite seu email:")
        #FOLHA DE CADASTRO
        dados = [nome, idade, email]
        #GUARDANDO A FOLHA NA PASTA
        cadastro.append(dados)

    elif botao == 2:
        for p in cadastro:
            print(p)

    elif botao == 0:
        print("Obrigado por acessar este Software!")

    else:
        print("Digite um número válido!")