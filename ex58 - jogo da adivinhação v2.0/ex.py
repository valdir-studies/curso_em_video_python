#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

escolha_computador = randint(1, 10)
cont = 0
print('Acabei de pensar em um número entre 0 e 10\nSerá que você consegue acertar?')
escolha_jogador = int(input('Qual é o seu palpite? '))

while escolha_jogador != escolha_computador:
    while escolha_jogador not in [1,2,3,4,5,6,7,8,9,10]:
        escolha_jogador = int(input('Por favor informe um número entre 1 e 10: '))

    escolha_jogador = int(input('ERROU!! mas eu sou bonzinho, te dou mais uma chance: '))
    cont += 1

if cont == 0:
    print('Acertou de primeira!')
elif cont == 1:
    print('Foi bem até... muito bom')
else:
    print(f'Depois de {cont} tentativas até minha vó consegue :v')
