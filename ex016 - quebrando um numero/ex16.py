# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('Digite um número: '))
print(f'O valor digitado foi {num} e sua parte inteira é {trunc(num)}')
