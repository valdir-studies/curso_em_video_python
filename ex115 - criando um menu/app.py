# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair do sistema'])
    match resposta:
        case 1:
            print('opção 1')
        case 2:
            print('opção 2')
        case 3:
            print('Saindo do sistema... até logo!')
            break
        case _:
            print('Erro! Digite uma opção válida!')
    sleep(2)