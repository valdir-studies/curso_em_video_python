# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um número: '))
num2 = int(input('Outro: '))
num3 = int(input('Mais um: '))
num4 = int(input('O último, onichan: '))

print(f'\nO maior valor é {max(num1,num2,num3,num4)}')
print(f'E o menor é {min(num1,num2,num3,num4)}')
