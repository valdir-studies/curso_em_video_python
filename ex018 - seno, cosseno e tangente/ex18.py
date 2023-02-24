# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import tan, sin, cos, radians

angulo = float(input('Digite o ângulo: '))

print(f'O seno de {angulo}° é {sin(radians(angulo)):.2f}, o cosseno é {cos(radians(angulo)):.2f} e a tangente é {tan(radians(angulo)):.2f}')