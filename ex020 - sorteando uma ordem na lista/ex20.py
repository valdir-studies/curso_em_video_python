# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

def sorteando_aleatorio(*args):
    lista_alunos = list(args)
    shuffle(lista_alunos)
    return lista_alunos

print(sorteando_aleatorio('Maria', 'Joãozinho', 'Pedro', 'Ana'))
