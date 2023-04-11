# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário')
            break
        else: return n

def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário')
            break
        else: return n

n = leia_int('Digite um número inteiro: ')
n2 = leia_float('Digite um número real: ')
print(f'Você digitou o número {n} e {n2}')
