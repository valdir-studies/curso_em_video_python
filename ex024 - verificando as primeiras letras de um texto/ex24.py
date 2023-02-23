# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Em que cidade você nasceu? ').strip().upper().split()

if cidade[0] == 'SANTO':
    print('Sim, começa com Santo')
else: 
    print('Não, não começa com Santo')

