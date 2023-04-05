"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0: passo = 1
    if passo < 0: passo *= -1

    cont = inicio

    if inicio > fim: 
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= passo
    else:
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += passo
    print()

contador(1, 10, 1)
contador(10, 0, 2)

print('\nAgora é sua vez!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(inicio, fim, pas)
