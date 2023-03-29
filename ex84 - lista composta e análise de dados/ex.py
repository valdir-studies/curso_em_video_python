"""""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.                                         
C) Uma listagem com as pessoas mais leves.
"""

pessoas = []
maior = menor = 0
while True:
    p_nome = input('Nome: ').capitalize()
    p_peso = float(input('Peso (kg): '))
    if len(pessoas) == 0: 
        maior = menor = p_peso
    else:
        if p_peso > maior: maior = p_peso
        if p_peso < menor: menor = p_peso
    pessoas.append([p_nome, p_peso])
    opt = input('Quer continuar? [S/N]: ')
    if opt in 'nN': break

print(f'\n{len(pessoas)} pessoas foram cadastradas')

print(f'O maior peso foi de {maior}kg, o peso de ', end='')
for p in pessoas:
    print(p[0] if p[1] == maior else '', end=' ')

print(f'\nO menor peso foi de {menor}kg, o peso de ', end='')
for p in pessoas:
    print(p[0] if p[1] == menor else '', end=' ')
