# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Qual seu nome completo? ').title().strip()

primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[len(nome.split()) - 1]

print(f'Olá, {nome}! Seu primeiro nome é {primeiro_nome} e seu último é {ultimo_nome}')
