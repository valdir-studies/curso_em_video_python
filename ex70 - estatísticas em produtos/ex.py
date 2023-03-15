# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = totmil = cont = menor = 0
barato = 0
while True:
    cont += 1
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    
    if resp == 'N':
        break
print(f'O valor total da compra foi de R${total:.2f}')
print(f'Da compra, {totmil} produtos custa/m mais de R$1000.00')
print(f'O produto mais barato foi o(a) {barato.capitalize}, que custa R${menor:.2f}')
