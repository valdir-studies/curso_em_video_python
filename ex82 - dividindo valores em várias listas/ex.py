# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_num =  []
lista_pares = []
lista_impares = []

while True:
    lista_num.append(int(input('Digite um número: ')))
    opt = input('Quer continuar? [S/N]: ')
    if opt in 'Nn': break

print(f'A lista com os números que você digitou foi: {lista_num}')

for n in lista_num:
    if n % 2 == 0: lista_pares.append(n)
    else: lista_impares.append(n)

print(f'A lista com números pares é {lista_pares}')
print(f'A lista com números ímpares é {lista_impares}')

