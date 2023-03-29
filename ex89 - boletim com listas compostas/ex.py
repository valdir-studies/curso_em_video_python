# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
while True:
    nome = input('Nome: ').capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    alunos.append([nome, (n1+n2) / 2, [n1, n2]])
    opt = input('Quer continuar? [S/N]: ')
    if opt in 'nN': break

print('\nBOLETIM')
for index, aluno in enumerate(alunos):
    print(f'{index} - Nome: {aluno[0]}; Média: {aluno[1]}')
while True:
    opt = int(input('\nQual aluno você quer checar? (999 interrompe): '))
    if opt == 999: break
    if opt <= len(alunos) - 1: print(f'As notas de {alunos[opt][0]} são {alunos[opt][2]}')
