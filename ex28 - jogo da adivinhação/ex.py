# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint

num = int(input('Pensei em um número de 0 a 5, tente adivinhar! '))

if not num in [0,1,2,3,4,5]:
    print('ô seu infeliz, eu disse de 0 a 5 >:(')
    exit()

escolhido = randint(0, 5)

print('Carregando...')
sleep(2)
if num == escolhido:
    print(f'Parabéns, eu pensei no número {num} mesmo!')

else:
    print(f'Errou! Eu pensei no número {escolhido}.')
