# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

count = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0, count):
    lista = []
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista: 
            lista.append(num)
            cont += 1
        if cont == 6: break
    lista.sort()
    print(f'Jogo {i+1}: {lista}')
    sleep(1)

print('\nBoa sorte! :) lembre-se que a probabilidade de ganhar na mega sena é 1 em 50.063.860!')
