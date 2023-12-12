def salvar_dados(restaurantes, pedido):
    with open('dados.txt', 'w') as arquivo:
        for restaurante in restaurantes:
            arquivo.write(f"{restaurante[0]}\n")
            for prato in restaurante[1]:
                arquivo.write(f"{prato[0]},{prato[1]},{prato[2]}\n")

    with open('pedido.txt', 'w') as arquivo_pedido:
        for item in pedido:
            arquivo_pedido.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")


def carregar_dados():
    restaurantes = []
    pedido = []

    try:
        with open('dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

            i = 0
            while i < len(linhas):
                nome_restaurante = linhas[i].strip()
                i += 1

                cardapio = []
                while i < len(linhas) and linhas[i].strip():
                    dados_prato = linhas[i].strip().split(',')
                    prato = [dados_prato[0], int(
                        dados_prato[1]), float(dados_prato[2])]
                    cardapio.append(prato)
                    i += 1

                restaurantes.append([nome_restaurante, cardapio])

    except FileNotFoundError:
        pass

    try:
        with open('pedido.txt', 'r') as arquivo_pedido:
            linhas_pedido = arquivo_pedido.readlines()

            for linha in linhas_pedido:
                dados_item = linha.strip().split(',')
                item = [dados_item[0], int(dados_item[1]), int(
                    dados_item[2]), float(dados_item[3])]
                pedido.append(item)

    except FileNotFoundError:
        pass

    return restaurantes, pedido


def cadastrar_restaurante(restaurantes):
    nome = input("Olá Parceiro, diga o nome do seu restaurante: ")
    restaurante = [nome, []]
    restaurantes.append(restaurante)
    print("Restaurante cadastrado com sucesso!\n")


def cadastrar_cardapio(restaurante):
    nome_prato = input("Digite o nome do prato: ")
    tempo_entrega = int(input("Digite o tempo de entrega (minutos): "))
    preco_prato = float(input("Digite o preço do prato: "))

    prato = [nome_prato, tempo_entrega, preco_prato]
    restaurante[1].append(prato)
    print(f"Prato '{nome_prato}' cadastrado com sucesso!")


def ver_cardapio(restaurante):
    print(f"Cardápio do Restaurante {restaurante[0]}")

    if restaurante[1]:
        for prato in restaurante[1]:
            print(
                f"Nome: {prato[0]}, Tempo de Entrega: {prato[1]} minutos, Preço: R${prato[2]:.2f}")
    else:
        print("O restaurante ainda não possui itens no cardápio.")


def mudar_cardapio(restaurante):
    print("Mudar Cardápio")

    if not restaurante[1]:
        print("O restaurante ainda não possui itens no cardápio.")
        return

    nome_prato = input("Digite o nome do prato que deseja alterar: ")

    for prato in restaurante[1]:
        if prato[0] == nome_prato:
            print("Prato encontrado. Informe os novos dados:")
            prato[0] = input("Digite o novo nome do prato: ")
            prato[1] = int(input("Digite o novo tempo de entrega (minutos): "))
            prato[2] = float(input("Digite o novo preço do prato: "))
            print("Prato alterado com sucesso!")
            return

    print("Prato não encontrado.")


def excluir_restaurante(restaurantes):
    print("Excluir Restaurante")

    if not restaurantes:
        print("Não há restaurantes cadastrados.")
        return

    nome_restaurante = input(
        "Digite o nome do restaurante que deseja excluir: ")

    for restaurante in restaurantes:
        if restaurante[0] == nome_restaurante:
            restaurantes.remove(restaurante)
            print(f"Restaurante '{nome_restaurante}' excluído!")
            return

    print("Restaurante não encontrado.")


def listar_restaurantes(restaurantes):
    for i, restaurante in enumerate(restaurantes, start=1):
        print(f"Restaurante {i}: {restaurante[0]}")
        print("------------------------")


def listar_pratos(restaurante):
    print(f"Restaurante: {restaurante[0]}")
    print("Pratos disponíveis:")
    for prato in restaurante[1]:
        print(
            f"Nome: {prato[0]}, Tempo de Entrega: {prato[1]} minutos, Preço: R${prato[2]:.2f}")


def listar_pedido(pedido):
    print("Seu pedido:")
    for item in pedido:
        nome = item[0]
        quantidade = item[1]
        tempo_entrega = int(item[2])
        preco = item[3]

        print(
            f"Nome: {nome}, Quantidade: {quantidade}, Tempo de Entrega: {tempo_entrega} minutos, Preço: R${preco:.2f}")


def cancelar_pedido(pedido):
    print("Pedido cancelado!")
    pedido.clear()


def main():
    restaurantes, pedido = carregar_dados()

    while True:
        print("Olá, bem-vindo ao iFood!\n")
        print("Para entender melhor o que você deseja, escolha uma das opções abaixo e ti ajudaremos:\n")
        print("1- Quero entrar como prestador de serviços!\n")
        print("2- Quero entrar como cliente!\n")
        print("3- Quero sair!\n")

        opcao_menu_principal = int(input("Escolha a opção: "))

        if opcao_menu_principal == 1:
            while True:
                print("Menu para Prestador de Serviços\n")
                print("1- Sou novo por aqui, quero cadastrar meu restaurante!\n")
                print("2- Agora sou parceiro, quero cadastrar meu cardápio!\n")
                print("3- Já fiz as duas opções acima, quero ver meu cardápio!\n")
                print("4- Desejo ajustar meu cardápio!\n")
                print("5- Quero excluir meu restaurante!\n")
                print("6- Terminei tudo quero sair\n")

                opcao_menu_prestador = int(input("Escolha a opção: "))

                if opcao_menu_prestador == 1:
                    cadastrar_restaurante(restaurantes)
                elif opcao_menu_prestador == 2:
                    cadastrar_cardapio(restaurantes[-1])
                elif opcao_menu_prestador == 3:
                    ver_cardapio(restaurantes[-1])
                elif opcao_menu_prestador == 4:
                    mudar_cardapio(restaurantes[-1])
                elif opcao_menu_prestador == 5:
                    excluir_restaurante(restaurantes)
                elif opcao_menu_prestador == 6:
                    print("Saindo dessa opção. Até a próxima!!")
                    break
                else:
                    print("Opção inválida. Digite um valor entre 1 a 6!")

        elif opcao_menu_principal == 2:
            nome_cliente = input("Por favor, digite seu nome: \n")
            while True:
                print(f"Bem-vindo, {nome_cliente}!\n")
                print("Menu para Clientes\n")
                print("1- Sou novo por aqui, quero conhecer os restaurantes!\n")
                print("2- Já sou cliente, quero fazer meu pedido!\n")
                print("3- Quero ver meu pedido!\n")
                print("4- Quero cancelar meu pedido!\n")
                print("5- Terminei tudo, quero sair\n")

                opcao_menu_cliente = int(input("Escolha a opção: "))

                if opcao_menu_cliente == 1:
                    listar_restaurantes(restaurantes)
                elif opcao_menu_cliente == 2:
                    nome_restaurante = input(
                        "Digite o nome do restaurante para ver os pratos: ")
                    restaurante_escolhido = None

                    for restaurante in restaurantes:
                        if restaurante[0] == nome_restaurante:
                            restaurante_escolhido = restaurante
                            break

                    if restaurante_escolhido:
                        listar_pratos(restaurante_escolhido)
                        nome_prato = input(
                            "Digite o nome do prato que deseja pedir: ")
                        quantidade = int(
                            input("Digite a quantidade desejada: "))

                        prato_escolhido = None
                        for prato in restaurante_escolhido[1]:
                            if prato[0] == nome_prato:
                                prato_escolhido = prato
                                break

                        if prato_escolhido:
                            preco_total = prato_escolhido[2] * quantidade
                            pedido.append(
                                [nome_prato, quantidade, prato_escolhido[1], preco_total])
                            print("Pedido adicionado com sucesso!")
                        else:
                            print("Prato não encontrado.")
                    else:
                        print("Restaurante não encontrado!")

                elif opcao_menu_cliente == 3:
                    listar_pedido(pedido)
                elif opcao_menu_cliente == 4:
                    cancelar_pedido(pedido)
                elif opcao_menu_cliente == 5:
                    print("Saindo dessa opção. Até a próxima!!")
                    break
                else:
                    print("Opção inválida. Digite um valor entre 1 a 5!")

        elif opcao_menu_principal == 3:
            print("Saindo do programa. Até a próxima!!")
            break
        else:
            print("Opção inválida. Digite um valor entre 1 a 3!")

    salvar_dados(restaurantes, pedido)


if __name__ == "__main__":
    main()