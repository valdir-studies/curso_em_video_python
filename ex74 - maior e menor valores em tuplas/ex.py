# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros_aleatorios = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),
                      randint(1,10))

print(f'Os números sorteados foram: {numeros_aleatorios}')
print(f'O maior valor da tupla é {max(numeros_aleatorios)}')
print(f'O menor valor da tupla é {min(numeros_aleatorios)}')
