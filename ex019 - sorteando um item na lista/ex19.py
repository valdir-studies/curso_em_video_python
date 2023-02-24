# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

def sorteando_aleatorio(*args):
    return choice(args)

print(sorteando_aleatorio('Maria', 'Joãozinho', 'Pedro', 'Ana'))
