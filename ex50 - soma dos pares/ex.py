# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}° número:'))
    if n % 2 == 0:
        soma += n

print(f'A soma de todos os números PARES informados é {soma}')
