# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def calcula_area(l, c): return l * c

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

print(f'A área de um terreno {largura}x{comprimento} é de {calcula_area(largura, comprimento)}m²')
