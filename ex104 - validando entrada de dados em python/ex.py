# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leia_int(msg):
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric(): 
            valor = int(n)
            break
        else: print('Erro! Digite um número inteiro válido.')
    return valor

n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}')
