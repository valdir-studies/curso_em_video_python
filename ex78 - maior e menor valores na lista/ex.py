# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = []

for i in range(0,5):
    num.append(int(input(f'Digite um número para a posição {i}: ')))

menor = min(num)
maior = max(num)

print(f'\nO menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(i, end=' ')

print(f'\nO maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(i, end=' ')
