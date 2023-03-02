# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

jogadas = ('Pedra', 'Papel', 'Tesoura')
opcao_computador = jogadas[randint(0, 2)]
opcao_jogador = int(input('''ESCOLHA UMA OPÇÃO! \n
1- Pedra
2- Papel
3- Tesoura\n
Escolha: '''))
if opcao_jogador not in [1,2,3]:
    print('Por favor, escolha uma opção válida!')
    exit()

opcao_jogador = jogadas[opcao_jogador - 1]

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!!')

print(f'\nO Computador escolheu {opcao_computador}')
print(f'O jogador escolheu {opcao_jogador}')

if opcao_jogador == opcao_computador:
    cond = 'EMPATE'

elif opcao_computador == 'Pedra':
    if opcao_jogador == 'Papel':
        cond = 'Jogador ganhou'
    elif opcao_jogador == 'Tesoura':
        cond = 'Computador ganhou'

elif opcao_computador == 'Papel':
    if opcao_jogador == 'Tesoura':
        cond = 'Jogador ganhou'
    elif opcao_jogador == 'Pedra':
        cond = 'Computador ganhou'

elif opcao_computador == 'Tesoura':
    if opcao_jogador == 'Papel':
        cond = 'Computador ganhou'
    elif opcao_jogador == 'Pedra':
        cond = 'Jogador ganhou'


print(f'\nO resultado final foi: {cond}')