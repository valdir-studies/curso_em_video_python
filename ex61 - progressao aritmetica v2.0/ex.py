# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o primeiro termo de uma P.A: '))
razao = int(input('Agora, informe a razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1

print('FIM')
