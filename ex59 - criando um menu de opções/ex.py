# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
finalizado = False
while not finalizado:
    print("""O que você deseja fazer com esses dois valores?
    [1] | Somar
    [2] | Multiplicar
    [3] | Maior
    [4] | Novos números
    [5] | Finalizar programa""")
    opcao = int(input('Qual será sua opção? '))
    match opcao:
        case 1:
            print(f'A soma de {n1} com {n2} é {n1+n2}')
        case 2:
            print(f'A multiplicação de {n1} com {n2} é {n1*n2}')
        case 3:
            if n1 < n2:
                print(f'O maior número é {n2}')
            elif n1 > n2:
                print(f'O maior número é {n1}')
            else:
                print('Os dois números são iguais')
        case 4:
            n1 = int(input('Informe um novo número: '))
            n2 = int(input('Mais um: '))
        case 5:
            finalizado = True
        case _:
            print('Essa opção não é válida! Escolha novamente, de 1 a 5')
    
    sleep(2)

print('Programa finalizado! Tenha um bom dia!')
