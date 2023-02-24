# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

def impar_par(num):
    if num % 2 == 0:
        return 'par'
    else: 
        return 'ímpar'

numero = int(input('Digite um número: '))
print(f'O número {numero} é {impar_par(numero)} ')
