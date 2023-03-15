# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = cont = media = menor = maior = 0
opt = 'S'


while opt == 'S':
    
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opt = input('Quer continuar? [S/N]').strip().upper()[0]
    
media = soma / cont
print(f'Você digitou {cont} números e a média deles é {media}')
print(f'O maior valor é {maior} e o menor é {menor}')
