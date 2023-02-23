from random import shuffle

def sorteando_aleatorio(*args):
    lista_alunos = list(args)
    shuffle(lista_alunos)
    return lista_alunos

print(sorteando_aleatorio('Maria', 'Joãozinho', 'Pedro', 'Ana'))