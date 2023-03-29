# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()

jogador['nome'] = input('Nome do jogador: ').capitalize()
jogador['gols'] = list()
jogador['partidas_qtd'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['total_gols'] = 0

for i in range(0, jogador['partidas_qtd']):
    jogador['gols'].append(int(input(f'Na {i+1}ª partida, quantos gols fez? ')))
    jogador['total_gols'] += jogador['gols'][-1]

#dicionário completo
print('\n', jogador)

#por chaves e valores
print()
for k, v in jogador.items():
    print(f'{k.title()} tem o valor {v}')

#print completo
print(f'\nO jogador {jogador["nome"]} completou {jogador["partidas_qtd"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols')
print(f'\nFoi um total de {jogador["total_gols"]} gols')