# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

text = input('Digite uma frase: ').replace(' ', '').strip().upper()
rtl = text[::-1]

if text == rtl:
    print('A frase citada É um palíndromo')
else: 
    print('A frase citada NÃO é um palíndromo')
