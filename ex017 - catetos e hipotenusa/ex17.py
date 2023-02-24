# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto1 = int(input('Digite o valor do primeiro cateto: '))
cateto2 = int(input('Digite o valor do segundo cateto: '))
print(f'A hipotenusa vale {hypot(cateto1, cateto2):.2f}')