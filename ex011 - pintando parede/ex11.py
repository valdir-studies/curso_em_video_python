# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura (em metros) da parede: '))
altura = float(input('Digite a altura (em metros) da parede: '))

area = largura * altura

# Cada 2m² é necessário 1L de tinta
tinta_qtd = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é {area}m²')
print(f'Para pintar essa parede, você precisará de {tinta_qtd}L de tinta')
