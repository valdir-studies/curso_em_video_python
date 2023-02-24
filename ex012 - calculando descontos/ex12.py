# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Adaptação -> O usuário pode escolher qual é a taxa.

def desconto(preco, taxa):
    preco = preco - (preco * ((taxa) / 100))
    return preco

preco = float(input('Digite o preço do produto: '))
taxa = int(input('Digite a taxa de desconto: '))

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de {taxa}% vai custar R${desconto(preco, taxa):.2f}')
