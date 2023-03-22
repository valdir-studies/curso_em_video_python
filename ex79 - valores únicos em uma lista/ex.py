# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = []

while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso! ')
    else:
        print('Esse valor já existe, não vou adicionar ')
    opt = str(input('Quer continuar? [S/N] '))
    if opt in 'Nn':
        break
    elif opt not in 'Ss':
        opt = str(input('Opção inválida! Digite [S] pra sim e [N] pra não, abestado '))
num.sort()
print(f'Os números digitados foram {num}')