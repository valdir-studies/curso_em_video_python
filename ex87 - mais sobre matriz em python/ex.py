"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """

matriz = [[], [], []]
soma_pares = maior_segunda = soma_terceira = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um número para [{i}, {j}]: '))
        matriz[i].append(n)
        if n % 2 == 0: soma_pares += n # soma os pares

        if i == 1: # analisa o maior da segunda linha
            if j == 0: maior_segunda = n
            else:
                if n > maior_segunda: maior_segunda = n

        if j == 2: # soma a terceira coluna
            soma_terceira += n
                
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

print(f'\nA soma dos pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira}')
print(f'O maior valor da segunda linha é {maior_segunda}')
