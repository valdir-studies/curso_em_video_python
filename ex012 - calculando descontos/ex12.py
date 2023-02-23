def desconto(preco, taxa):
    preco = preco - (preco * ((taxa) / 100))
    return preco

preco = float(input('Digite o preço do produto: '))
taxa = int(input('Digite a taxa de desconto: '))

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de {taxa}% vai custar R${desconto(preco, taxa):.2f}')
