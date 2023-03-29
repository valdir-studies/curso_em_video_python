# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = input('Nome: ').capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] < 5: aluno['situação'] = 'REPROVADO'
elif aluno['média'] < 7: aluno['situação'] = 'EM RECUPERAÇÃO'
else: aluno['situação'] = 'APROVADO'

print()
for k, v in aluno.items():
    print(f'{k.capitalize()} é igual a {v}')
