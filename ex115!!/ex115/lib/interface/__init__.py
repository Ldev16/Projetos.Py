def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, KeyError):
            print('\033[31mErro: tente uma opção valida!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mentrada de dados interrompida pelo usuario\033[m')
            break
        else:
            return n


def linha(tam=42):
    return '=' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32msua Opção: \033[m')
    return opc



