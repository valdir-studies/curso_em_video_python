# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

list_num = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    list_num[n%2].append(n)

list_num[0].sort()
list_num[1].sort()
print(f'\nOs números pares são {list_num[0]}')
print(f'Os números ímpares são {list_num[1]}')
