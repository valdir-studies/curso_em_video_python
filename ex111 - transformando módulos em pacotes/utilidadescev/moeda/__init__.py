# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

def aumentar(preco, taxa, format=False):
    res = preco + (preco * taxa / 100)
    return res if not format else moeda(res)

def diminuir(preco, taxa, format=False):
    res = preco - (preco * taxa / 100)
    return res if not format else moeda(res)

def dobro(preco, format=False):
    res = preco * 2
    return res if not format else moeda(res)

def metade(preco, format=False):
    res = preco / 2
    return res if not format else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
    
def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
