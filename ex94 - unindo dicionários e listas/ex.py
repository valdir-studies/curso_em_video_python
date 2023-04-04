"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
"""
media_idade = 0
pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ').title()
    while True: 
        pessoa['sexo'] = input('Sexo: [M/F]: ').title()
        if pessoa['sexo'] in 'MF': break
        print('Modernidade detectada! Digite M para masculino ou F para feminino!')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa)
    opt = input('Quer continuar? [S/N]: ')
    if opt in 'Nn': break



print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

print(f'B) A média de idade é de ')

print('As mulheres são: ', end='')
mulheres = list(map(lambda p: p == 'F', pessoas))
for mulher in mulheres: print(mulher, end=' ')