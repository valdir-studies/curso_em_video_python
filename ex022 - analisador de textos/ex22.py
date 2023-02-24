# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()

minusculo = nome.lower()
maiusculo = nome.upper()
tamanho = len(nome.replace(" ", ""))
primeiro_nome = nome.split()[0]

print(f'\nSeu nome com letras em maiúsculo fica: {maiusculo}')
print(f'Seu nome com letras em minúsculo fica: {minusculo}')
print(f'Seu nome tem ao todo {tamanho} letras')
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras')
