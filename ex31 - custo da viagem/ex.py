# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Digite a distância em km: '))

if distancia <= 200:
    custo = distancia * 0.5
else: 
    custo = distancia * 0.45

print(f'O custo da viagem com {distancia}km de distância é de R${custo:.2f}')
