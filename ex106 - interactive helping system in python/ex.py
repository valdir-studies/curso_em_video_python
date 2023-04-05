# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores. (não usarei, obrigado)

def ajuda(com):
    help(com)

while True:
    command = str(input('Função ou biblioteca > '))
    if command.upper() == 'FIM': break
    else: ajuda(command)