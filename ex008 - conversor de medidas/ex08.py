# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

distancia = float(input('Digite a distância em metros: '))

print(f'\n\nA medida de {distancia}m corresponde a:')
print(f'{distancia / 1000}km \n{distancia/100}hm \n{distancia/10}dam \n{distancia*10}dm \n{distancia*100}cm \n{distancia*1000}mm')
