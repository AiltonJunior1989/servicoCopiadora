def escolha_servico():
    while True:
        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('>> ')
        if servico == 'dig':
            return 1.1
            break
        elif servico == 'ico':
            return 1
            break
        elif servico == 'ipb':
            return 0.4
            break
        elif servico == 'fot':
            return 0.2
            break
        else:
            print('Opss!!! Opção inválida')
            print('Entre com o tipo de serviço desejado novamente\n')
            continue

def qtd_pag():
    while True:
        try:
            paginas = int(input('Entre com a quantidade de páginas a serem copiadas: '))
            if paginas < 20:
                return paginas
            elif paginas >= 20 and paginas < 200:
                com_desconto = paginas * 0.85
                return com_desconto
            elif paginas >= 200 and paginas < 2000:
                com_desconto = paginas * 0.80
                return com_desconto
            elif paginas >= 2000 and paginas < 20000:
                com_desconto = paginas * 0.75
                return com_desconto
            else:
                print('Não aceitamos pedidos nesta quantidade de página.')
                continue
        except ValueError:
            print('Valor não corresponde a um número')
            continue

def servico_extra():
    while True:
        print('Deseja adicionar mais algum serviço ?')
        print('1 - Encadernação Simples - R$10,00')
        print('2 - Encadernação Capa Dura - R$25,00')
        print('0 - Não desejo mais nada')
        try:
            servico = int(input('>>'))
            if servico == 1:
                return 10
            elif servico == 2:
                return 25
            elif servico == 0:
                return 0
            else:
                print('Opcão inválida. Tente novamente')
                continue
        except ValueError:
            print('Opção deve ser um número')
            continue



# programa principal
print('Bem vindo a Copiadora do Ailton RU:4651421')
servico = escolha_servico()
num_pagina = qtd_pag()
extra = servico_extra()
total = servico * num_pagina + extra
print('Total de R${:.2f} (servico: R${} * paginas: {} + extra(s): R${}'.format(total, servico, num_pagina, extra))



