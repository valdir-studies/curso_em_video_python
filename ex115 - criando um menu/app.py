# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

from lib.interface import *
from lib.arquivo import *

from time import sleep

arq = 'users.txt'

if not arquivo_existe(arq): criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair do sistema'])
    match resposta:
        case 1: ler_arquivo(arq)
        case 2:
            cabecalho('Novo cadastro')
            nome = input('Nome: ')
            idade = leia_int('Idade: ')
            cadastrar(arq, nome, idade)
        case 3:
            print('Saindo do sistema... até logo!')
            break
        case _:
            print('Erro! Digite uma opção válida!')
    sleep(2)
