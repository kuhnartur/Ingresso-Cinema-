import time
import qrcode 

while True:
    print("Bem vindo ao cinema CineUni")
    print("Vendemos dois tipos de ingressos:")
    print("Digite 1 para Inteiro R$ 30,00 e 2 para Meia R$15,00")

    ingressos = {'1': 30, '2': 15}

    # Seleção do tipo de ingresso
    opcao_ingresso = ''
    while opcao_ingresso not in ingressos.keys():
        opcao_ingresso = input('Qual tipo de ingresso você deseja comprar: ')
        if opcao_ingresso not in ingressos.keys():
            print('Escolha uma opção inválida!')

    tipo_ingresso = 'Inteiro' if opcao_ingresso == '1' else 'Meia'
    valor_ingresso = ingressos[opcao_ingresso]

    print(f"Opção de ingresso escolhida foi {
          tipo_ingresso}, no valor de R${valor_ingresso},00 cada")

    # Seleção da quantidade de ingresso
    print("\nVocê pode comprar até 6(seis) ingressos")
    while True:
        quantidade_ingressos = input('Quantos ingressos você deseja comprar: ')
        if not quantidade_ingressos.isdigit():
            print('Digite um valor inteiro para a quantidade de ingressos!')
            continue

        quantidade_ingressos = int(quantidade_ingressos)
        if quantidade_ingressos < 1 or quantidade_ingressos > 6:
            print('Quantidade inválida!')
            continue

        if quantidade_ingressos > 1:
            print(f'Você selecionou a compra de {
                  quantidade_ingressos} ingressos\n')
        else:
            print(f'Você selecionou a compra de {
                  quantidade_ingressos} ingresso\n')

        valor_total = quantidade_ingressos * valor_ingresso
        print(f"O total da sua compra foi de R${valor_total},00")
        break

    # Seleção da forma de pagamento
    formas_pagamento = {'1': 'Elo', '2': 'Visa', '3': 'Débito', '4': 'Pix'}
    print('Escolha uma opção de pagamento:')
    for key, value in formas_pagamento.items():
        print(f'{key}: {value}')

    opcao_pagamento = ''
    while opcao_pagamento not in formas_pagamento.keys():
        opcao_pagamento = input('Qual a forma de pagamento: ')
        if opcao_pagamento not in formas_pagamento.keys():
            print(
                'Opção inválida! Digite um valor numérico correspondente a uma das formas de pagamento.')

    forma_pagamento_escolhida = formas_pagamento[opcao_pagamento]
    print(f'Forma de pagamento escolhida: {forma_pagamento_escolhida}')

    aguarde = 'Aguarde a Confirmação'
    imagem= qrcode.make("Pagamento registrado!")

    if forma_pagamento_escolhida in ['Elo', 'Visa', 'Débito']:
        print('Insira seu cartão na máquina')
        time.sleep(5)
        print('Digite sua senha')
        time.sleep(5)
        time.sleep(5)
        print('Pagamento realizado com sucesso')
    else:
        print('Realize o pagamento com Pix. Aguarde o QR code aparecer na tela\n')
        imagem.save("pix.jpg")
        time.sleep(1)
        time.sleep(5)
        time.sleep(5)
        print('Pagamento realizado com sucesso')

    time.sleep(5)  # Espera 5 segundos para aprovar o pagamento
    print('Retire seu ingresso.')
    print('Desejamos que você tenha uma ótima sessão e aproveite o filme!\n\n\n')
    time.sleep(10)  # Espera 10 segundos até o próximo cliente