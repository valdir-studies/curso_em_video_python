# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
while True:
    jogador = dict()
    jogador['nome'] = input('Nome do jogador: ').capitalize()
    jogador['gols'] = list()
    jogador['partidas_qtd'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['total_gols'] = 0

    for i in range(0, jogador['partidas_qtd']):
        jogador['gols'].append(int(input(f'Na {i+1}ª partida, quantos gols fez? ')))
        jogador['total_gols'] += jogador['gols'][-1]
    time.append(jogador)
    opt = input('Quer continuar? [S/N]: ')
    if opt in 'nN': break

for i, v in enumerate(time):
    print(f'{i}- Nome: {v["nome"]}; Gols: {v["gols"]};Total: {v["total_gols"]}')

while True:
    opt = int(input('\nMostrar dados de qual jogador? (999 para parar): '))
    try:
        print(time[opt])
    except IndexError:
        print(f'Não existe jogador com o número {opt}! Tente novamente')
    if opt == 999: break
    