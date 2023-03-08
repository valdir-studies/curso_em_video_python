# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ADAPTAÇÃO -> uso de recursão (visto no livro grokking algorithms)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('Informe um número: '))
print(f'O fatorial de {n} é {factorial(n)}')
