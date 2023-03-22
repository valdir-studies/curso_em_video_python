# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
num = []
menor = 0
for i in range(0, 5):
    num = int(input(f'Digite um número: '))
