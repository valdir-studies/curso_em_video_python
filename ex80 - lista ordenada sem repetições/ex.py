# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista_num = []
menor = 0
for i in range(0, 5):
    num = int(input(f'Digite um número: '))
    if i == 0 or num > lista_num[-1]: 
        lista_num.append(num)
        print(f'{num} inserido ao final da lista')
    else:
        pos = 0
        while pos < len(lista_num):
            if num <= lista_num[pos]: 
                lista_num.insert(pos, num)
                print(f'{num} adicionado na posição {pos}')
                break
            pos += 1

print(f'\n{lista_num}')

