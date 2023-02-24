# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
# Adaptação -> estrutura de repetição já foi usada

def tabuada(n):
    for i in range(11):
        print(f'{n} x {i} = {i*n}')

tabuada(9)
# 9 x 0 = 0
# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90
