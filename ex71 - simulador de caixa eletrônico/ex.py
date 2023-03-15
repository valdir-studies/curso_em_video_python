#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input("Que valor você quer sacar? "))
notas = [50, 20, 10, 1]
cedulas = []
cont = 0

while saque > 0:
    for val in notas:
        cedulas.append(saque // val)
        saque = saque % val
#        print(f"{cedulas[counter]} notas de R${val}")
        cont += 1
cont = 0

for item in cedulas:
    if item > 0:
        print(f"{item} cédulas de R${notas[cont]}")
    cont += 1
