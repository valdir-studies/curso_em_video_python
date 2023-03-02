# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))
base_numerica = int(input('Agora escolha uma base numérica: \n\n1- Binário\n2- Octal\n3- Hexadecimal\n'))

match base_numerica:
    case 1:
        base = 'BINÁRIO'
        num_convertido = bin(num)
    case 2:
        base = 'OCTAL'
        num_convertido = oct(num)
    case 3:
        base = 'HEXADECIMAL'
        num_convertido = hex(num)
    case _:
        print('A base numérica informada não corresponde à lista')

num_convertido = num_convertido[2:]

print(f'O número {num} convertido para {base} fica {num_convertido}')