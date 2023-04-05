# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*args):
    m = 0
    for i, v in enumerate(args):
        if i == 0: m = v
        else:
            if v > m: m = v
    return m

print(maior(1,4,3,2,1,2,87))
print(maior(10,4,7))
print(maior())
