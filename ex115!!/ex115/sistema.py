from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'CadastroDePessoas.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Programa'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('SAINDO DO SISTEMA.... até logo')
        break
    else:
        print('\033[31mERRO: Digite uma opçao valida\033[m')
    sleep(0.5)
