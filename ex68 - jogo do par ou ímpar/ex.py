# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

v = 0
while True:
    opt = ' '
    while opt not in 'PI':
        opt = input('Par ou ímpar? [P/I]: ').strip().upper()[0]
    
    jogador = int(input(f'Você escolheu {opt}. Que número vc escolhe? '))
    computador = randint(0, 10)

    print(f'Você jogou {jogador} e o computador escolheu {computador}')
    if opt == 'P':
        if (jogador + computador) % 2 == 0:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    if opt == 'I':
        if (jogador + computador) % 2 == 1: 
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar de novo...')

print(f'GAME OVER! Você venceu {v} vezes')

